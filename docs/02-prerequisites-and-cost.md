# Step 2 – Prerequisites and cost

[⬅ Previous: Overview](01-overview-and-concepts.md) | [Next: Provision the workspace ➡](03-provision-workspace.md)

Doing these checks now prevents the three most common errors in this lab: missing permissions, unregistered resource providers and missing VM quota.

## Prerequisites

- An Azure subscription (Free Trial, Pay-As-You-Go or paid). If you don't have one, create a free account at https://azure.microsoft.com/free.
- The **Owner** or **Contributor** role on that subscription.
- **Google Chrome** or **Microsoft Edge**. Safari and Firefox sometimes fail to upload folders in step 5.
- The `data/diabetes-data` folder from this repo on your computer ([step 0](00-get-the-repo.md)).

---

## 2.1 Check your role on the subscription

1. Sign in to https://portal.azure.com.
2. In the search bar at the top, type **`Subscriptions`** and click **Subscriptions** under *Services*.
3. Click the name of the subscription you will use.
4. In the left menu, click **Access control (IAM)**.
5. Click the **View my access** button (in the *My access* box).
6. Check that the list includes **Owner** or **Contributor**, either at this subscription or inherited from above it.

✅ If it does, continue. ❌ If it only shows *Reader*, or nothing, ask your Azure administrator to give you Contributor on the subscription. You cannot do this lab without it.

## 2.2 Register the resource providers (prevents the "subscription is not registered" error)

New subscriptions, especially Free Trials, often haven't turned on ("registered") the Azure services this lab uses. Registering them is free.

1. Still on your subscription's page, in the left menu, scroll to **Settings** and click **Resource providers**.
2. In the **Filter by name** box, type **`Microsoft.MachineLearningServices`**.
3. Look at the **Status** column.
   - If it says **Registered**, move on to the next provider.
   - If it says **NotRegistered**, click the row to select it, then click **Register** at the top. The status changes to *Registering* and then *Registered* (1–3 minutes; click **Refresh** to update).
4. Repeat for each of these providers:

   | Provider | Used for |
   |---|---|
   | `Microsoft.MachineLearningServices` | The Azure Machine Learning workspace and jobs |
   | `Microsoft.Storage` | The workspace storage account |
   | `Microsoft.KeyVault` | The workspace key vault |
   | `Microsoft.Insights` | Application Insights |
   | `Microsoft.OperationalInsights` | The Log Analytics workspace behind Application Insights |
   | `Microsoft.ContainerRegistry` | Container registry (used later, when deploying models) |

> **Prefer the command line?** Open Cloud Shell (the `>_` icon at the top of the portal, choose **Bash**) and run the provider block at the top of [`scripts/01-provision-workspace.sh`](../scripts/01-provision-workspace.sh), or the whole script.

## 2.3 Pick a region and check VM quota (prevents the "insufficient quota" error)

The AutoML job runs on a **Standard_DS3_v2** machine, which belongs to the **Standard DSv2 Family** and uses **4 vCPUs**. Your subscription needs at least 4 free vCPUs of that family in Azure Machine Learning **in the region you choose**.

1. In the portal search bar, type **`Quotas`** and click **Quotas**.
2. In the left menu, click **Machine learning** (under *Usage + quotas*, or on the *Overview* tiles).
3. Use the filters at the top: choose your **subscription** and the **region** you plan to use (for example *East US*).
4. In the search box, type **`DSv2`**.
5. Find **Standard DSv2 Family Cluster Dedicated vCPUs**. The **Usage** column shows something like `0 of 24`. You need the limit minus the current usage to be **4 or more**.

What to do with the result:
- **4 or more free:** use this region in step 3.
- **Less than 4 (often `0 of 0` on Free Trial):** change the region filter and try **East US**, **East US 2**, **West US 2**, **North Europe** or **West Europe**, and use whichever region has quota. You can also request more by clicking the pencil icon / **Request quota increase** (approval can take from minutes to a day).
- **Still none anywhere:** you can use a smaller VM in step 5 instead. See [Troubleshooting → Quota](09-troubleshooting.md#e7-the-compute-step-shows-insufficient-quota-or-the-job-fails-with-a-quota-error).

> Once your workspace exists, you can also check quota from inside the studio (**Manage → Compute → Quota** link) or with [`src/check_quota.py`](../src/check_quota.py).

---

## Cost to perform this lab

**Typical total: about US $0.10–$1.00**, as long as you delete the resource group at the end.

| What | When you pay | Rough cost |
|---|---|---|
| Serverless compute (`Standard_DS3_v2`) | Only while the AutoML job is running (about 15–30 minutes) | Cents to well under $1 |
| Storage account | For the data you store (a few MB) | Fractions of a cent per day |
| Key vault, Application Insights, Log Analytics | Per use; this lab barely uses them | Near zero |
| The workspace itself | No charge for the workspace resource | $0 |

Exact prices depend on your region and currency. See https://azure.microsoft.com/en-us/pricing/details/machine-learning/.

> 💡 **The most important cost rule:** do [step 8 – Clean up](08-cleanup.md) as soon as you finish. A forgotten resource group keeps billing storage, and a forgotten compute instance (if you create one for the notebook) bills every hour it is running.

[⬅ Previous: Overview](01-overview-and-concepts.md) | [Next: Provision the workspace ➡](03-provision-workspace.md)
