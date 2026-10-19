# Step 5 – Train a model using AutoML

[⬅ Previous: Explore the studio](04-explore-studio.md) | [Next: Use Jobs to view your history ➡](06-review-jobs.md)

To see how the workspace's assets and resources work together, you'll train a model. AutoML is a quick way to find the best model for your data.

> Pop-ups and tips may appear in the studio along the way. Close them and stick to these steps.

### What changed from the original lab, and why

The original lab created the data asset in the middle of the AutoML wizard. Many learners then found that the new data asset **didn't appear** in the wizard's list. To avoid that, this guide does it in two parts:

- **Part A:** create the data asset first from the **Data** page and wait until it exists.
- **Part B:** create the AutoML job and simply select that data asset.

The result is the same, with no missing-data error. (If you'd rather use the inline **+ Create** button inside the wizard, the screens are the same as Part A, steps 3–10.)

---

## Part A – Create the training data asset

1. Have the **`data/diabetes-data`** folder from this repo ready on your computer ([step 0](00-get-the-repo.md)). It must be a normal folder (not a `.zip`) containing **`MLTable`** and **`diabetes.csv`**.
2. In the studio's left menu, under **Assets**, click **Data**.
3. Make sure the **Data assets** tab is selected, then click **+ Create**.
4. **Data type** step:
   - **Name:** `training-data`
   - **Description:** `Diabetes training data` (optional)
   - **Type:** open the drop-down and choose **Table (mltable)**. ⚠️ This is important. The default is *File (uri_file)*, and AutoML can't use that type.
   - Click **Next**.
5. **Data source** step: choose **From local files**. Click **Next**.
6. **Destination storage type** step:
   - **Datastore type:** **Azure Blob Storage**
   - In the datastore list, select **workspaceblobstore** (it's usually already selected).
   - Click **Next**.
7. **MLTable selection** step: click **Upload** and choose **Upload folder** (not *Upload files*).
8. In the window that opens, go to your copy of the repo, open **`data`**, click **once** on the **`diabetes-data`** folder to select it, and click **Upload** (Windows: **Select Folder**).

   > Choose the `diabetes-data` folder **itself**, not the `data` folder above it and not the files inside it. The `MLTable` file has to be at the top level of what you upload.

9. Your browser asks something like *"Upload 2 files to this site?"*. Click **Upload**. Wait until both **MLTable** and **diabetes.csv** are listed with a green tick or 100%, then click **Next**.

   > ❌ If you see *"MLTable file not found"* or the **Next** button stays grey, you picked the wrong folder level. See [Troubleshooting E5](09-troubleshooting.md#e5-mltable-file-not-found-or-next-is-greyed-out-on-the-mltable-selection-step).

10. **Review** step: check that **Type** is *Table (mltable)*, then click **Create**.
11. You're taken to the **training-data** page. Click the **Explore** tab. After a few seconds you should see a preview of the table with columns `PatientID ... Diabetic`. This shows the data asset was created correctly.

---

## Part B – Create and submit the AutoML job

### Basic settings

1. In the left menu, under **Authoring**, click **Automated ML**.
2. Click **+ New Automated ML job**.
3. **Basic settings** step:
   - **Job name:** keep the generated name, or type something unique such as `diabetes-automl-01`.
   - **Experiment name:** select **Create new** and type `mslearn-diabetes-automl`, or keep the default.
   - **Description / Tags:** leave empty.
   - Click **Next**.

### Task type & data

4. **Select task type:** choose **Classification**.
5. **Select data:** in the list, click the radio button next to **training-data**.

   > Don't see it? Click **Refresh** above the list. Still missing? Check that its type is *Table (mltable)* in **Data**. See [Troubleshooting E4](09-troubleshooting.md#e4-the-uploaded-data-asset-does-not-appear-in-the-automl-wizard).

6. Check that **Classification** is still selected. Selecting data sometimes resets the task type, so select **Classification** again if it changed. Click **Next**.

### Task settings

7. **Target column:** choose **Diabetic**.

   > The label next to it may say *(Integer)* or *(Boolean)*, depending on how the studio reads the 0/1 values. Either is fine. Just select **Diabetic**.

8. Click **View additional configuration settings**. In the panel that opens:
   - **Primary metric:** choose **Accuracy**.
   - Leave everything else as it is.
   - Click **Save**.
9. Expand **Limits** and set:

   | Setting | Value |
   |---|---|
   | **Max trials** | `10` |
   | **Max concurrent trials** | leave the default |
   | **Experiment timeout (minutes)** | `60` |
   | **Iteration timeout (minutes)** | `15` |
   | **Enable early termination** | ✅ checked |

   > Type the numbers into the boxes. If a box shows a red outline, click elsewhere on the page to confirm the value.

10. Expand **Validate and test** (it may be labelled *Validation and test*):
    - **Validation type:** leave **Auto**.
    - **Test data:** choose **Train-test split**.
    - **Percentage test of data:** check it is **10**.
11. Click **Next**.

### Compute

12. **Select compute type:** **Serverless**.
13. **Virtual machine type:** **CPU**. **Virtual machine tier:** **Dedicated**.
14. **Virtual machine size:** select **Standard_DS3_v2**. If it isn't already shown, click **Select from all options** and search for `DS3_v2`.
15. **Number of instances:** `1`.
16. Click **Next**.

> **Quota message?** If you see a warning that you don't have enough quota for this size, choose another 4-vCPU general-purpose size that shows available quota, such as **Standard_D4s_v3** or **Standard_D4ds_v4**, or a smaller one such as **Standard_DS2_v2** (slower, but enough for this small dataset). See [Troubleshooting E7](09-troubleshooting.md#e7-the-compute-step-shows-insufficient-quota-or-the-job-fails-with-a-quota-error).

### Review and submit

17. On the **Review** step, check:
    - Task type: **Classification**
    - Data: **training-data**
    - Target column: **Diabetic**
    - Primary metric: **Accuracy**
    - Max trials **10**, experiment timeout **60**, iteration timeout **15**, early termination **on**
    - Test data: **Train-test split, 10%**
    - Compute: **Serverless, Standard_DS3_v2** (or the size you picked)
18. Click **Submit training job**.

You're taken to the job's page. Continue to [step 6](06-review-jobs.md) while it runs.

---

## Appendix: the code path (optional)

The same work done with the Azure ML Python SDK v2. Everything runs in **Azure Cloud Shell**, so there's nothing to install on your computer. Do this **instead of** steps 3 and 5 if you want to practise the code-first approach, or **after** the lab for extra practice. (Running both creates a second job and costs a few cents more.)

1. In the Azure portal, click the **Cloud Shell** icon (`>_`) in the top bar. If asked, choose **Bash**. For storage, either choose **No storage account required** or let it create one.
2. Clone the repo and go into it:

   ```bash
   git clone https://github.com/SHADRACK-NAKOBA/azure-ml-workspace-lab.git
   cd azure-ml-workspace-lab
   ```

3. Create the workspace (skip this if you already did step 3 in the portal). Change `eastus` to your region:

   ```bash
   bash scripts/01-provision-workspace.sh eastus
   ```

4. Create a Python virtual environment and install the SDK (takes 1–3 minutes):

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

5. (Optional) Check your quota for the VM size:

   ```bash
   python src/check_quota.py
   ```

6. Upload the data and submit the AutoML job:

   ```bash
   python src/submit_automl_job.py
   ```

   The script prints a **studio link**. Open it to watch the job. Options: `python src/submit_automl_job.py --help` (for example `--vm-size Standard_DS2_v2` if you lack DSv2 quota).

7. (Optional, free) Train a quick local baseline for comparison:

   ```bash
   python src/local_baseline.py
   ```

> The scripts read the subscription from your Cloud Shell login and default to `rg-dp100-labs` / `mlw-dp100-labs`. To use other names: `export AZ_RESOURCE_GROUP=... AZ_WORKSPACE=...` before running them.

> Cloud Shell ends the session after about 20 minutes without activity. If that happens, open it again and run `cd azure-ml-workspace-lab && source .venv/bin/activate`.

[⬅ Previous: Explore the studio](04-explore-studio.md) | [Next: Use Jobs to view your history ➡](06-review-jobs.md)
