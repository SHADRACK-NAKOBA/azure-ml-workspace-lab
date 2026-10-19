# Prince Hands-on Lab: Explore the Azure Machine Learning Workspace

Learn how Azure Machine Learning gives you one place to create, manage and track machine learning assets, resources and training jobs. You will build a workspace, look around Azure Machine Learning Studio, upload a dataset, train a diabetes classification model with **Automated ML (AutoML)**, and review the job history.

**Who this is for:** data scientists, AI engineers, ML engineers, cloud engineers and AI enthusiasts who want hands-on practice with Azure Machine Learning.

| | |
|---|---|
| **Time** | 60–90 minutes (about 20 of those are spent waiting for the AutoML job) |
| **Cost** | Usually under US $1 if you delete everything at the end (see [cost](docs/02-prerequisites-and-cost.md#cost-to-perform-this-lab)) |
| **Level** | Beginner |
| **You need** | An Azure subscription where you are **Owner** or **Contributor**, and the Chrome or Edge browser |

---

## Project overview

**Scenario.** You are getting started with Azure Machine Learning and want to understand how its workspace, resources and studio are organized before moving on to deeper model development and MLOps. You explore the core workspace components, then use AutoML to train a classification model that predicts whether a patient is diabetic, and review the resulting job history.

**What you will build**

```
Azure subscription
└── Resource group: rg-dp100-labs
    ├── Azure Machine Learning workspace: mlw-dp100-labs
    ├── Storage account        (created automatically - stores your data and outputs)
    ├── Key vault              (created automatically - stores secrets)
    ├── Application Insights   (created automatically - monitoring)
    └── Log Analytics workspace (created automatically - backs Application Insights)

Inside the workspace
├── Data asset: training-data  (the diabetes-data folder from this repo, as an MLTable)
└── Job: AutoML classification (10 trials on serverless compute, best model chosen by Accuracy)
```

**The dataset.** [`data/diabetes-data/`](data/diabetes-data) holds 10,000 patient records (`diabetes.csv`) and an `MLTable` file that tells Azure Machine Learning how to read the CSV. The column to predict is **`Diabetic`** (1 = diabetic, 0 = not). About 33% of the rows are diabetic.

| Column | Meaning |
|---|---|
| PatientID | Patient identifier (not a useful predictor) |
| Pregnancies | Number of pregnancies |
| PlasmaGlucose | Plasma glucose concentration |
| DiastolicBloodPressure | Diastolic blood pressure |
| TricepsThickness | Triceps skin-fold thickness |
| SerumInsulin | Serum insulin |
| BMI | Body mass index |
| DiabetesPedigree | Diabetes pedigree function (family history score) |
| Age | Age in years |
| **Diabetic** | **Target: 1 = diabetic, 0 = not diabetic** |

---

## Lab steps

Follow these in order. Every page is click by click.

| # | Step | What you do |
|---|---|---|
| 0 | [Get this repo onto your computer](docs/00-get-the-repo.md) | Clone or download the repo so you have the dataset folder |
| 1 | [Overview and key concepts](docs/01-overview-and-concepts.md) | Read the ideas behind the lab (5 minutes) |
| 2 | [Prerequisites and cost](docs/02-prerequisites-and-cost.md) | Check your subscription, role and quota **before** you start |
| 3 | [Provision the workspace](docs/03-provision-workspace.md) | Create the workspace in the Azure portal |
| 4 | [Explore Azure Machine Learning Studio](docs/04-explore-studio.md) | Tour the Authoring, Assets and Manage sections |
| 5 | [Train a model with AutoML](docs/05-train-with-automl.md) | Upload the data and submit the AutoML job |
| 6 | [Use Jobs to view your history](docs/06-review-jobs.md) | Read the results and find the best model |
| 7 | [Share your learnings](docs/07-share-your-learnings.md) | Post your result on LinkedIn and in the community |
| 8 | [Clean up resources](docs/08-cleanup.md) | **Delete everything so you stop paying** |
| 9 | [Troubleshooting](docs/09-troubleshooting.md) | Fixes for every common error in this lab |

> **Stuck?** Go straight to [Troubleshooting](docs/09-troubleshooting.md). Each error there is listed with the exact message, why it happens and how to fix it.

### Optional: do it with code instead of clicks

The portal steps above are the main lab. If you also want to see the same work done as code (the way it is done in real DevOps/MLOps projects), use these. Everything runs in **Azure Cloud Shell**, so you don't need to install anything on your computer.

| File | What it does |
|---|---|
| [`scripts/01-provision-workspace.sh`](scripts/01-provision-workspace.sh) | Registers the needed resource providers and creates the resource group and workspace (replaces step 3) |
| [`src/check_quota.py`](src/check_quota.py) | Shows whether you have enough quota for `Standard_DS3_v2` in your region |
| [`src/submit_automl_job.py`](src/submit_automl_job.py) | Uploads the data asset and submits the same AutoML job (replaces step 5) |
| [`src/local_baseline.py`](src/local_baseline.py) | Trains a quick scikit-learn model on your own computer, for comparison with AutoML (free) |
| [`notebooks/explore-diabetes-data.ipynb`](notebooks/explore-diabetes-data.ipynb) | Explores the dataset and trains two baseline models in a notebook (free when run locally) |
| [`scripts/99-cleanup.sh`](scripts/99-cleanup.sh) | Deletes the resource group and everything in it (replaces step 8) |

How to run them: [Appendix: the code path](docs/05-train-with-automl.md#appendix-the-code-path-optional).

---

## Repository layout

```
azure-ml-workspace-lab/
├── README.md                     <- you are here
├── data/
│   ├── diabetes-data/            <- UPLOAD THIS FOLDER in step 5
│   │   ├── MLTable
│   │   └── diabetes.csv
│   └── diabetes-data.zip         <- same data, zipped (backup copy)
├── docs/                         <- the click-by-click lab guide (steps 0-9)
├── scripts/                      <- Azure CLI scripts (bash, for Cloud Shell)
├── src/                          <- Python scripts (Azure ML SDK v2 + scikit-learn)
├── notebooks/                    <- optional data exploration notebook
└── requirements.txt
```

## Documentation links

- Azure Machine Learning documentation: https://learn.microsoft.com/en-us/azure/machine-learning/
- Azure Machine Learning studio: https://ml.azure.com
- Automated Machine Learning: https://learn.microsoft.com/en-us/azure/machine-learning/concept-automated-ml
- Data assets: https://learn.microsoft.com/en-us/azure/machine-learning/how-to-create-data-assets
- Pricing: https://azure.microsoft.com/en-us/pricing/details/machine-learning/

## Summary

In this lab you provision a workspace, explore its resources and the studio, create a managed data asset, run an AutoML training job, and use tracked jobs to understand and manage experiments. This is the foundation for every later Azure Machine Learning and MLOps lab.

---

*Prince Hands-on Labs. The diabetes dataset comes from Microsoft Learn's open-source DP-100 lab repository ([MicrosoftLearning/mslearn-azure-ml](https://github.com/MicrosoftLearning/mslearn-azure-ml)).*
