"""Shared helper: connect to the lab's Azure Machine Learning workspace.

Settings come from environment variables, with defaults that match the lab:
    AZ_SUBSCRIPTION_ID  - defaults to the subscription you are logged in to (az account show)
    AZ_RESOURCE_GROUP   - defaults to rg-dp100-labs
    AZ_WORKSPACE        - defaults to mlw-dp100-labs
"""
import os
import shutil
import subprocess
import sys

from azure.ai.ml import MLClient
from azure.identity import AzureCliCredential, DefaultAzureCredential

RESOURCE_GROUP = os.environ.get("AZ_RESOURCE_GROUP", "rg-dp100-labs")
WORKSPACE = os.environ.get("AZ_WORKSPACE", "mlw-dp100-labs")


def _subscription_id() -> str:
    sub = os.environ.get("AZ_SUBSCRIPTION_ID")
    if sub:
        return sub
    az = shutil.which("az")
    if not az:
        sys.exit("Azure CLI not found. Run this in Azure Cloud Shell, or install the "
                 "Azure CLI and run 'az login', or set AZ_SUBSCRIPTION_ID.")
    result = subprocess.run([az, "account", "show", "--query", "id", "-o", "tsv"],
                            capture_output=True, text=True)
    if result.returncode != 0 or not result.stdout.strip():
        sys.exit("Not logged in to Azure. Run 'az login' (or reopen Cloud Shell) and try again.")
    return result.stdout.strip()


def _credential():
    # The Azure CLI login works both in Cloud Shell and on your own computer after 'az login'.
    if shutil.which("az"):
        return AzureCliCredential()
    return DefaultAzureCredential()


def get_ml_client() -> MLClient:
    client = MLClient(
        credential=_credential(),
        subscription_id=_subscription_id(),
        resource_group_name=RESOURCE_GROUP,
        workspace_name=WORKSPACE,
    )
    try:
        ws = client.workspaces.get(WORKSPACE)
    except Exception as exc:  # give a friendly message instead of a long stack trace
        sys.exit(
            f"Could not open workspace '{WORKSPACE}' in resource group '{RESOURCE_GROUP}'.\n"
            f"  - Did you create it (step 3 or scripts/01-provision-workspace.sh)?\n"
            f"  - Using other names? export AZ_RESOURCE_GROUP=... AZ_WORKSPACE=...\n"
            f"  - Several subscriptions? az account set --subscription \"<name or id>\"\n"
            f"Details: {exc}"
        )
    print(f"Connected to workspace '{ws.name}' in {ws.location} (resource group {RESOURCE_GROUP})")
    client.location = ws.location
    return client
