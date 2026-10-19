#!/usr/bin/env bash
# -----------------------------------------------------------------------------
# Prince Hands-on Lab - delete everything this lab created.
#
# Run in Azure Cloud Shell (Bash):
#     bash scripts/99-cleanup.sh
#
# Deletes the whole resource group (workspace, storage, key vault, App Insights).
# Add --purge to also permanently delete the soft-deleted workspace, so you can
# re-create one with the same name straight away:
#     bash scripts/99-cleanup.sh --purge
# -----------------------------------------------------------------------------
set -euo pipefail

RESOURCE_GROUP="${AZ_RESOURCE_GROUP:-rg-dp100-labs}"
WORKSPACE="${AZ_WORKSPACE:-mlw-dp100-labs}"
PURGE="${1:-}"

if [[ "$(az group exists --name "$RESOURCE_GROUP")" != "true" ]]; then
  echo "Resource group ${RESOURCE_GROUP} does not exist - nothing to delete."
  exit 0
fi

echo "This will permanently delete resource group '${RESOURCE_GROUP}' and everything in it:"
az resource list -g "$RESOURCE_GROUP" --query "[].{name:name, type:type}" -o table
echo
read -r -p "Type the resource group name to confirm: " CONFIRM
if [[ "$CONFIRM" != "$RESOURCE_GROUP" ]]; then
  echo "Names don't match - cancelled."
  exit 1
fi

if [[ "$PURGE" == "--purge" ]]; then
  az extension add -n ml --upgrade -y --only-show-errors
  if az ml workspace show -n "$WORKSPACE" -g "$RESOURCE_GROUP" -o none 2>/dev/null; then
    echo "==> Permanently deleting workspace ${WORKSPACE} (no 14-day soft delete)..."
    az ml workspace delete -n "$WORKSPACE" -g "$RESOURCE_GROUP" --permanently-delete --yes
  fi
fi

echo "==> Deleting resource group ${RESOURCE_GROUP} (5-10 minutes)..."
az group delete --name "$RESOURCE_GROUP" --yes
echo "==> Deleted. Nothing from this lab is billing any more."
