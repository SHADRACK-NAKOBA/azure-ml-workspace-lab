# Step 3 – Provision an Azure Machine Learning workspace

[⬅ Previous: Prerequisites and cost](02-prerequisites-and-cost.md) | [Next: Explore the studio ➡](04-explore-studio.md)

A workspace is the central place for all the resources and assets you need to train and manage models. You can create one in the Azure portal or with the Azure CLI. Production teams usually automate it with the CLI so it fits into a repeatable DevOps process. Here you use the **portal** so you can see every option. (The CLI version is in [`scripts/01-provision-workspace.sh`](../scripts/01-provision-workspace.sh) if you want to try it afterwards.)

## 3.1 Open the create page

1. Go to https://portal.azure.com and sign in.
2. Click the search bar at the top, type **`Azure Machine Learning`**, and under *Services* click **Azure Machine Learning**.
3. Click **+ Create** at the top left, then click **New workspace**.

   > Don't choose *New hub*, *New project* or *New registry*. Those are different resource types used in other labs.

## 3.2 Fill in the Basics tab

| Field | What to enter |
|---|---|
| **Subscription** | Your Azure subscription |
| **Resource group** | Click **Create new**, type **`rg-dp100-labs`**, click **OK** |
| **Name** (workspace name) | **`mlw-dp100-labs`** |
| **Region** | The region you chose in [step 2.3](02-prerequisites-and-cost.md#23-pick-a-region-and-check-vm-quota-prevents-the-insufficient-quota-error), the one where you have **DSv2 quota**. If you skipped that check, choose **East US**. |
| **Storage account** | Leave the default **(new) ...**. Just note its name. |
| **Key vault** | Leave the default **(new) ...**. Just note its name. |
| **Application insights** | Leave the default **(new) ...**. Just note its name. |
| **Container registry** | Leave it as **None**. Azure creates one automatically the first time you deploy a model to a container. |

> 💡 **Why the region matters:** the AutoML job runs in the same region as the workspace. If that region has no VM quota for you, the job cannot start. Choosing a region with quota now saves you from rebuilding later.

## 3.3 Leave the other tabs as they are

The **Networking**, **Encryption**, **Identity** and **Tags** tabs have advanced options, such as restricting access through a private endpoint or encrypting data with your own keys. You won't use them in this lab, but it's worth knowing they exist. Leave every default as it is.

> ⚠️ Don't change **Networking** to *Private* or *Disabled*. The studio and your browser upload won't be able to reach the workspace, and steps 4–6 will fail.

## 3.4 Create it

1. Click **Review + create** at the bottom.
2. Wait for **Validation passed** at the top. If validation fails instead, read the red message and see [Troubleshooting E1–E3](09-troubleshooting.md#e1-the-subscription-is-not-registered-to-use-namespace-microsoftmachinelearningservices).
3. Click **Create**.
4. Wait for **Your deployment is complete**. This usually takes **3–5 minutes**. Leave the page open; it updates by itself.
5. Click **Go to resource**.

## Check before you continue

- [ ] The deployment page says **Your deployment is complete**.
- [ ] You can see the **mlw-dp100-labs** workspace overview page.

[⬅ Previous: Prerequisites and cost](02-prerequisites-and-cost.md) | [Next: Explore the studio ➡](04-explore-studio.md)
