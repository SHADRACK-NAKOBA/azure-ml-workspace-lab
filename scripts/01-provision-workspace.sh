#!/usr/bin/env bash
# -----------------------------------------------------------------------------
# Prince Hands-on Lab - Explore the Azure Machine Learning workspace
# Provision the resource group and Azure Machine Learning workspace with the CLI.
#
# Run in Azure Cloud Shell (Bash):
#     bash scripts/01-provision-workspace.sh [region]
#
# Examples:
#     bash scripts/01-provision-workspace.sh            # uses eastus
#     bash scripts/01-provision-workspace.sh westeurope
#
# Optional environment variables (defaults shown):
#     AZ_RESOURCE_GROUP=rg-dp100-labs
#     AZ_WORKSPACE=mlw-dp100-labs
# -----------------------------------------------------------------------------
set -euo pipefail

LOCATION="${1:-${AZ_LOCATION:-eastus}}"
RESOURCE_GROUP="${AZ_RESOURCE_GROUP:-rg-dp100-labs}"
WORKSPACE="${AZ_WORKSPACE:-mlw-dp100-labs}"

echo "==> Subscription in use:"
az account show --query "{name:name, id:id}" -o table
echo
echo "    Region:          ${LOCATION}"
echo "    Resource group:  ${RESOURCE_GROUP}"
echo "    Workspace:       ${WORKSPACE}"
echo

# 1. Register the resource providers this lab needs (safe to run more than once).
PROVIDERS=(
  Microsoft.MachineLearningServices
  Microsoft.Storage
  Microsoft.KeyVault
  Microsoft.Insights
  Microsoft.OperationalInsights
  Microsoft.ContainerRegistry
)
for p in "${PROVIDERS[@]}"; do
  state=$(az provider show --namespace "$p" --query registrationState -o tsv 2>/dev/null || echo "NotRegistered")
  if [[ "$state" == "Registered" ]]; then
    echo "==> Provider $p already registered"
  else
    echo "==> Registering provider $p (this can take a few minutes)..."
    az provider register --namespace "$p" --wait
  fi
done

# 2. Make sure the Azure ML CLI v2 extension ('ml') is installed and the old
#    v1 extension ('azure-cli-ml') is not, because the two conflict.
if az extension show -n azure-cli-ml >/dev/null 2>&1; then
  echo "==> Removing old azure-cli-ml (v1) extension"
  az extension remove -n azure-cli-ml
fi
echo "==> Installing/updating the Azure ML CLI extension (ml)"
az extension add -n ml --upgrade -y --only-show-errors

# 3. Resource group
echo "==> Creating resource group ${RESOURCE_GROUP} in ${LOCATION}"
az group create --name "$RESOURCE_GROUP" --location "$LOCATION" -o none

# 4. Workspace (creates storage account, key vault and Application Insights automatically)
if az ml workspace show -n "$WORKSPACE" -g "$RESOURCE_GROUP" -o none 2>/dev/null; then
  echo "==> Workspace ${WORKSPACE} already exists - skipping creation"
else
  echo "==> Creating workspace ${WORKSPACE} (about 3-5 minutes)..."
  az ml workspace create \
    --name "$WORKSPACE" \
    --resource-group "$RESOURCE_GROUP" \
    --location "$LOCATION" \
    -o none
fi

echo
echo "==> Done. Resources in ${RESOURCE_GROUP}:"
az resource list -g "$RESOURCE_GROUP" --query "[].{name:name, type:type}" -o table
echo
echo "Open the studio at: https://ml.azure.com  (select workspace '${WORKSPACE}')"
