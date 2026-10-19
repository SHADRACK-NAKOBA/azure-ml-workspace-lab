# Step 4 – Explore Azure Machine Learning Studio

[⬅ Previous: Provision the workspace](03-provision-workspace.md) | [Next: Train a model with AutoML ➡](05-train-with-automl.md)

Azure Machine Learning Studio is the web portal for your workspace. You use it to manage every asset and resource in the workspace.

## 4.1 Look at what Azure created

1. In the Azure portal search bar, type **`rg-dp100-labs`** and click the resource group under *Resource Groups*.
   (Or: portal **Home** → **Resource groups** → **rg-dp100-labs**.)
2. On the **Overview** page, look at the **Resources** list. You should see:
   - the **Azure Machine Learning workspace** `mlw-dp100-labs`
   - a **Storage account**
   - a **Key vault**
   - an **Application Insights** resource
   - (usually) a **Log Analytics workspace**, which backs Application Insights

   > If the list looks incomplete, click **Refresh**. Resources can take a minute to appear after deployment.

## 4.2 Launch the studio

1. In the resource list, click **mlw-dp100-labs** (type: *Azure Machine Learning workspace*).
2. On the workspace **Overview** page, click the blue **Launch studio** button.
3. The studio opens in a **new browser tab** at `ml.azure.com`.

   > **Nothing happened?** Your browser probably blocked the pop-up. Look for a blocked pop-up icon at the right end of the address bar, click it, choose **Always allow pop-ups...**, and click **Launch studio** again. Or open https://ml.azure.com directly and pick your workspace from the list.

4. Close any welcome or tour pop-ups that appear in the studio (click **X** or **Skip**).

## 4.3 Tour the left-hand menu

If you only see icons on the left, click the **☰** (hamburger) icon at the top left to show the page names.

### Authoring – three ways to build models

| Page | What it is for |
|---|---|
| **Notebooks** | Write and run Python code in Jupyter notebooks inside the studio |
| **Automated ML** | Let Azure try many algorithms for you and pick the best (you use this in step 5) |
| **Designer** | Build training pipelines by dragging and dropping components, with no code |

### Assets – what you use and create when training

| Page | What it is for |
|---|---|
| **Data** | Data assets and datastores (your training data goes here in step 5) |
| **Jobs** | The history of every training run (step 6) |
| **Components**, **Pipelines**, **Environments** | Reusable building blocks for training |
| **Models** | Trained, registered models |
| **Endpoints** | Deployed models you can call |

Assets can be **versioned**, so you can keep track of how they change over time.

### Manage – the infrastructure

| Page | What it is for |
|---|---|
| **Compute** | Compute instances (personal VMs for notebooks), compute clusters and attached compute |
| **Monitoring**, **Data labeling**, **Linked services**, **Connections** | Other workspace-level tools |

> 💡 Click each page once to see what is on it. You won't break anything by looking. Just **don't create a compute instance** unless a step asks you to. Compute instances are billed every hour they are running.

## Check before you continue

- [ ] The studio is open in a browser tab and the workspace name **mlw-dp100-labs** is shown at the top right.
- [ ] You can find **Automated ML**, **Data**, **Jobs** and **Compute** in the left menu.

[⬅ Previous: Provision the workspace](03-provision-workspace.md) | [Next: Train a model with AutoML ➡](05-train-with-automl.md)
