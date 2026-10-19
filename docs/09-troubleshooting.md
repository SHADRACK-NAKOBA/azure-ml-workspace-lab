# Step 9 – Troubleshooting

[⬅ Back to README](../README.md)

These are the errors learners most often hit in this lab, roughly in the order they happen. Find your error, read the cause, and apply the fix.

| # | Where it happens | Error |
|---|---|---|
| [E1](#e1-the-subscription-is-not-registered-to-use-namespace-microsoftmachinelearningservices) | Step 3 – create workspace | Subscription not registered to use namespace |
| [E2](#e2-authorizationfailed--you-do-not-have-permission-to-create-resources) | Step 3 – create workspace | AuthorizationFailed / no permission |
| [E3](#e3-deployment-fails-with-a-region-sku-or-policy-error) | Step 3 – create workspace | Region, SKU or policy error |
| [E4](#e4-the-uploaded-data-asset-does-not-appear-in-the-automl-wizard) | Step 5 – AutoML | Uploaded data asset not available in AutoML |
| [E5](#e5-mltable-file-not-found-or-next-is-greyed-out-on-the-mltable-selection-step) | Step 5 – data asset | MLTable file not found / Next greyed out |
| [E6](#e6-upload-fails-or-gets-stuck-authorization--403--network-error) | Step 5 – data asset | Upload fails, 403 or network error |
| [E7](#e7-the-compute-step-shows-insufficient-quota-or-the-job-fails-with-a-quota-error) | Step 5 – compute | Insufficient quota |
| [E8](#e8-the-automl-job-failed) | Step 6 – job | AutoML job failed |
| [E9](#e9-the-job-stays-in-not-started-or-queued-for-a-long-time) | Step 6 – job | Job stuck in Not started / Queued |
| [E10](#e10-recreating-the-workspace-fails-because-a-soft-deleted-workspace-with-the-same-name-exists) | Repeating the lab | Soft-deleted workspace with the same name |
| [E11](#e11-launch-studio-does-nothing) | Step 4 | Launch studio does nothing |
| [E12](#e12-code-path-errors-cloud-shell--python) | Appendix (code path) | Cloud Shell / Python errors |

---

### E1. The subscription is not registered to use namespace 'Microsoft.MachineLearningServices'

**Error:** `MissingSubscriptionRegistration: The subscription is not registered to use namespace 'Microsoft.MachineLearningServices'` (or `Microsoft.Insights`, `Microsoft.OperationalInsights`, `Microsoft.KeyVault`, `Microsoft.Storage`).

**Root cause:** New subscriptions don't have every Azure service turned on.

**Fix:** Register the provider named in the error. See [step 2.2](02-prerequisites-and-cost.md#22-register-the-resource-providers-prevents-the-subscription-is-not-registered-error): **Subscriptions → your subscription → Resource providers → search → Register**. Wait until it shows *Registered*, then go back to the create page and click **Create** again. (Or run `bash scripts/01-provision-workspace.sh` in Cloud Shell, which registers all of them.)

---

### E2. AuthorizationFailed / You do not have permission to create resources

**Error:** `AuthorizationFailed: The client '...' does not have authorization to perform action 'Microsoft.Resources/subscriptions/resourcegroups/write'` or similar.

**Root cause:** Your account is only a *Reader* (or has no role) on the subscription.

**Fix:** Ask the subscription owner to give you **Contributor** on the subscription (**Subscription → Access control (IAM) → + Add → Add role assignment → Contributor → your account**). Sign out and back in afterwards.

---

### E3. Deployment fails with a region, SKU or policy error

**Errors:** `RequestDisallowedByPolicy`, `LocationNotAvailableForResourceType`, `SkuNotAvailable`, or a validation failure on the storage account or key vault.

**Root causes and fixes:**
- **Policy** (common on company or school subscriptions): your organization blocks some regions or settings. The error names the policy. Pick a region the policy allows, or ask your administrator.
- **Region not available:** choose a common region such as **East US**, **East US 2**, **West Europe** or **North Europe**.
- If a deployment failed partway through, delete the half-created `rg-dp100-labs` resource group ([step 8](08-cleanup.md)) and start step 3 again.

---

### E4. The uploaded data asset does not appear in the AutoML wizard

**Error:** The training data you uploaded doesn't show up (or isn't selectable) in the *Task type & data* step.

**Root causes:**
- The data asset hadn't finished being created when you went back to the wizard.
- It was created as **File (uri_file)** or **Folder (uri_folder)** instead of **Table (mltable)**. AutoML only lists MLTable data assets.
- You uploaded the zip file, or the wrong folder, so the MLTable step didn't complete.
- The task type was reset after selecting data.

**Fixes:**
1. Click **Refresh** above the data list.
2. In a new tab, open **Assets → Data** and click your data asset. Check that **Type** says **Table (mltable)** and that the **Explore** tab shows a preview. If the type is wrong, create a new data asset ([step 5, Part A](05-train-with-automl.md#part-a--create-the-training-data-asset)) with the name `training-data-v2` and **Type: Table (mltable)**.
3. Make sure you uploaded the extracted **`diabetes-data` folder**, not `diabetes-data.zip` and not the CSV file on its own.
4. Select **Classification** again, then select your data asset again.
5. If it still doesn't appear, cancel the wizard (**Cancel**), reload the page (**F5**), and start a new Automated ML job.

---

### E5. "MLTable file not found" or Next is greyed out on the MLTable selection step

**Root cause:** The folder you uploaded doesn't have the `MLTable` file at its top level. Usually you picked the parent folder (`data`), a folder inside a zip, or used *Upload files* and picked only the CSV.

**Fix:**
1. On your computer, open the folder you're uploading. You must see **`MLTable`** and **`diabetes.csv`** directly inside it, not inside another folder.
2. **Windows:** if the path contains `.zip\`, you're inside a zip. Right-click the zip → **Extract All...**, then use the extracted folder.
3. **macOS:** check that Finder hasn't hidden a file extension and renamed `MLTable` to `MLTable.txt`. The file must be called exactly **`MLTable`**, with no extension. (Finder → **Settings → Advanced → Show all filename extensions** to check.)
4. In the wizard, click **Upload → Upload folder** and select the **`diabetes-data`** folder itself.

> Don't edit the `MLTable` file. If you opened and saved it in an editor that changed it, download a fresh copy of the repo. A correct MLTable looks like this:
> ```yaml
> paths:
>   - file: ./diabetes.csv
> transformations:
>   - read_delimited:
>         delimiter: ','
>         encoding: 'ascii'
> ```

---

### E6. Upload fails or gets stuck (authorization / 403 / network error)

**Root causes and fixes:**
- **Browser:** use **Chrome** or **Edge**. Turn off ad-blockers / privacy extensions for `ml.azure.com`, or try an InPrivate/Incognito window.
- **Company network / VPN** blocking `*.blob.core.windows.net`: try another network, or turn off the VPN for the upload.
- **Storage account key access disabled by policy** (some organization subscriptions): the error mentions *authorization* or *key based authentication is not permitted*. Ask your administrator, or use a personal / Free Trial subscription for this lab.
- **Firewall on the storage account:** in the portal, open the workspace's storage account → **Networking**. *Public network access* must be **Enabled from all networks** for this lab.

---

### E7. The compute step shows "insufficient quota", or the job fails with a quota error

**Error:** A warning such as *"You don't have enough quota for the selected VM size"*, or the job fails with `Insufficient quota` / `QuotaExceeded`.

**Root cause:** Your subscription has fewer than 4 free **Standard DSv2 Family** vCPUs for Azure Machine Learning in the workspace's region. This is common on **Free Trial** subscriptions.

**Fixes (try in order):**
1. **Pick another VM size that has quota.** In the compute step, click **Select from all options**. Sizes with available quota can be selected; others are greyed out or warned. Good choices for this small dataset: **Standard_DS2_v2** (2 vCPUs, slower but enough), **Standard_D4s_v3**, **Standard_D4ds_v4**, **Standard_D2s_v3**. Any small general-purpose CPU size works.
2. **Request more quota:** studio → **Manage → Compute** → **Quota** (or portal → **Quotas → Machine learning**) → choose your region → find *Standard DSv2 Family Cluster Dedicated vCPUs* → **Request quota increase** → ask for **8**.
3. **Use another region:** quota is per region. Delete the resource group and repeat step 3 in a region where you have quota (check with [step 2.3](02-prerequisites-and-cost.md#23-pick-a-region-and-check-vm-quota-prevents-the-insufficient-quota-error) or `python src/check_quota.py`).
4. **Free Trial:** if every size is blocked, upgrade to Pay-As-You-Go (**Subscriptions → your subscription → Upgrade**). You keep your remaining free credit.

> Code path: `python src/submit_automl_job.py --vm-size Standard_DS2_v2`

---

### E8. The AutoML job failed

**How to diagnose:** open the job → **Overview** to see the error message, then **Outputs + logs** (look in `user_logs/std_log.txt` if present). Also check the failed **child job**.

| Message contains | Cause | Fix |
|---|---|---|
| `QuotaExceeded`, `Insufficient quota` | No VM quota | See [E7](#e7-the-compute-step-shows-insufficient-quota-or-the-job-fails-with-a-quota-error) |
| `target column` / `Diabetic` not found | Wrong data asset or column | Check the data asset preview has a `Diabetic` column, and resubmit with **Target column = Diabetic** |
| `MLTable` / `could not read` / `UserErrorException` about data | Data asset created incorrectly | Recreate it as **Table (mltable)** from the `diabetes-data` folder ([E5](#e5-mltable-file-not-found-or-next-is-greyed-out-on-the-mltable-selection-step)), then resubmit |
| `Experiment timeout reached` | It hit the 60-minute limit | Usually still **Completed** with the best model found so far. If it failed, resubmit. Serverless start-up may have been slow. |
| `Canceled` | Someone cancelled it, or Cloud Shell closed (code path) | Resubmit |

**To resubmit quickly:** open the failed job → click **Edit and submit** (or **Clone**) at the top → change only what's needed → **Submit**.

---

### E9. The job stays in "Not started" or "Queued" for a long time

**Root cause:** Serverless compute is starting a VM for you. This normally takes **3–10 minutes**. Longer waits usually mean low capacity in the region or no quota.

**Fix:**
- Wait up to **15 minutes** and click **Refresh**.
- If it's still queued after 20 minutes, open the job's **Overview** and look for a quota or capacity message. Then see [E7](#e7-the-compute-step-shows-insufficient-quota-or-the-job-fails-with-a-quota-error). Cancel the job (**Cancel** at the top) and resubmit with another VM size.

---

### E10. Recreating the workspace fails because a soft-deleted workspace with the same name exists

**Error:** Something like *"A soft-deleted workspace with the same name exists"* when you repeat the lab within 14 days.

**Root cause:** Deleted workspaces are kept in a soft-deleted state for 14 days.

**Fix (pick one):**
- Use a different workspace name, for example `mlw-dp100-labs-2`. This is the easiest.
- Purge the old one: portal → **Azure Machine Learning** → **Recently deleted** (at the top of the list) → select the workspace → **Permanently delete**.

---

### E11. Launch studio does nothing

**Root cause:** The browser blocked the new tab as a pop-up.

**Fix:** Click the blocked pop-up icon at the right end of the address bar → **Always allow** → click **Launch studio** again. Or go directly to https://ml.azure.com and choose **mlw-dp100-labs**.

---

### E12. Code path errors (Cloud Shell / Python)

| Error | Fix |
|---|---|
| `az ml: 'ml' is misspelled or not recognized` | Run `az extension add -n ml --upgrade -y` (the provisioning script does this). |
| Conflict with `azure-cli-ml` | The old v1 extension is installed. Run `az extension remove -n azure-cli-ml`, then `az extension add -n ml -y`. |
| `ModuleNotFoundError: No module named 'azure.ai.ml'` | You're outside the virtual environment. Run `source .venv/bin/activate`, then `pip install -r requirements.txt`. |
| `error: externally-managed-environment` when running `pip install` | Create and activate the virtual environment first (appendix step 4). Don't install into the system Python. |
| `DefaultAzureCredential failed to retrieve a token` | Run `az login` (on your own computer) or reopen Cloud Shell. Then `az account show` to confirm the right subscription. |
| `ResourceNotFound` / workspace not found | The script uses `rg-dp100-labs` / `mlw-dp100-labs`. If you used other names, `export AZ_RESOURCE_GROUP=<rg> AZ_WORKSPACE=<ws>`. If you have several subscriptions: `az account set --subscription "<name or id>"`. |
| `bash: scripts/01-provision-workspace.sh: No such file or directory` | You're not in the repo folder. Run `cd ~/azure-ml-workspace-lab`. |
| `$'\r': command not found` when running a `.sh` file | The file got Windows line endings (edited on Windows). Run `sed -i 's/\r$//' scripts/*.sh` and try again. |

---

Still stuck? Post a screenshot of the **full error message** (hide your subscription ID) in the Prince community lab issues thread, together with the step number you were on.

[⬅ Back to README](../README.md)
