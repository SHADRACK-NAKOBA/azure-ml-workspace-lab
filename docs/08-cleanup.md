# Step 8 – Clean up resources

[⬅ Previous: Share your learnings](07-share-your-learnings.md) | [Next: Troubleshooting ➡](09-troubleshooting.md)

Delete everything you created so you aren't charged for it any more. This also keeps your subscription tidy. Deleting the **resource group** deletes the workspace, storage account, key vault, Application Insights and everything else inside it, all in one go.

> ⚠️ Make sure your screenshots are saved first. Deleting can't be undone.

## 8.1 Stop anything still running (only if you created extra compute)

The serverless compute used by AutoML stops by itself. If you also created a **compute instance** (for example to run the notebook in the studio):

1. In the studio, go to **Manage → Compute → Compute instances**.
2. Tick your instance and click **Delete**. (Deleting the resource group in 8.2 also removes it, so this is just extra safety.)

## 8.2 Delete the resource group

1. Close the Azure Machine Learning studio tab.
2. Go to https://portal.azure.com.
3. On the **Home** page, click **Resource groups**. (Or type `Resource groups` in the search bar.)
4. Click **rg-dp100-labs**.
5. At the top of the **Overview** page, click **Delete resource group**.
6. If a checkbox called **Apply force delete for selected Virtual machines and Virtual machine scale sets** appears, you can leave it unticked.
7. In the **Enter resource group name to confirm deletion** box, type **`rg-dp100-labs`**.
8. Click **Delete**, then **Delete** again if asked to confirm.
9. Click the **bell icon** (Notifications) at the top right. After **5–10 minutes** it shows *Deleted resource group rg-dp100-labs*.

**Command-line alternative (Cloud Shell):**

```bash
bash scripts/99-cleanup.sh
```

## 8.3 Check that it's gone

1. Go to **Resource groups** again and click **Refresh**.
2. **rg-dp100-labs** should no longer be in the list.

## Good to know: repeating the lab later

When you delete a workspace, Azure keeps it in a **soft-deleted** state for **14 days** so it can be recovered. If you repeat the lab within 14 days using the **same resource group and workspace name**, creation can fail with a *"soft-deleted workspace with the same name"* error. Either use a new name (for example `mlw-dp100-labs-2`) or purge the old one. See [Troubleshooting E10](09-troubleshooting.md#e10-recreating-the-workspace-fails-because-a-soft-deleted-workspace-with-the-same-name-exists).

[⬅ Previous: Share your learnings](07-share-your-learnings.md) | [Next: Troubleshooting ➡](09-troubleshooting.md)
