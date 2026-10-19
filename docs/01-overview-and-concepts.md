# Step 1 – Overview and key concepts

[⬅ Previous: Get the repo](00-get-the-repo.md) | [Next: Prerequisites and cost ➡](02-prerequisites-and-cost.md)

## Introduction

In this lab you explore the Azure Machine Learning workspace and see how it acts as the central place for managing machine learning resources, assets and workloads.

1. You **provision a workspace** in the Azure portal. Azure automatically creates the supporting resources it needs: a storage account, a key vault and an Application Insights resource.
2. You **open Azure Machine Learning Studio** and look at how authoring tools, data, jobs, models and compute are organized.
3. You **train a classification model with AutoML** on diabetes data you upload.
4. You **review the job history** to see how Azure Machine Learning tracks your runs and outputs.

## How the pieces fit together

```
 Your computer                     Azure
 ─────────────                     ─────────────────────────────────────────────────────
 data/diabetes-data  ──upload──►  Storage account (workspaceblobstore)
                                        │
                                        ▼
                                  Data asset "training-data" (MLTable)
                                        │
                                        ▼
                                  AutoML job ──runs on──► Serverless compute (Standard_DS3_v2)
                                        │                     trains up to 10 candidate models
                                        ▼
                                  Jobs page: status, metrics, best model, outputs
```

## Key concepts

### Azure Machine Learning workspace
The central resource for managing machine learning assets, workloads and supporting infrastructure. In this lab it is where you store the data asset, run the AutoML job and review training history.

### Azure Machine Learning Studio
The web interface for working with a workspace, at https://ml.azure.com. In this lab you use it to explore the workspace, create a data asset, submit an AutoML job and review the results.

### Supporting resources
| Resource | What the workspace uses it for |
|---|---|
| Storage account | Stores uploaded data, job outputs, logs and models (the default datastore is called `workspaceblobstore`) |
| Key vault | Stores secrets such as connection keys |
| Application Insights | Monitors deployed models and endpoints |
| Container registry | Stores Docker images. Not created now; Azure creates one the first time it is needed |

### Data assets
A data asset is a named, versioned reference to data stored in or connected to the workspace. In this lab you create one by uploading the `diabetes-data` folder.

**MLTable** is a data asset type for tabular data. The small file called `MLTable` inside the folder tells Azure Machine Learning which file to read (`diabetes.csv`) and how to read it (comma-separated). AutoML needs tabular data in MLTable format, which is why you upload the **folder**, not just the CSV.

### Automated Machine Learning (AutoML)
AutoML tries many combinations of algorithms and data preprocessing for you and ranks them by a metric you choose. In this lab it runs a **classification** experiment and picks the best model by **Accuracy**.

### Jobs and experiment history
A job is a tracked run of work in Azure Machine Learning. Jobs are grouped into **experiments**. The Jobs page shows each job's status, settings, duration, metrics and outputs.

### Serverless compute
Lets you run a job without creating or managing a compute cluster yourself. Azure starts machines when the job begins and releases them when it ends, so you only pay while the job runs. In this lab the AutoML job uses serverless compute with the `Standard_DS3_v2` VM size (4 vCPUs, 14 GB RAM).

### Classification model selection
Classification predicts a category, here **diabetic (1)** or **not diabetic (0)**. Model selection means finding the algorithm and preprocessing that perform best. AutoML does this automatically. The optional notebook and `src/local_baseline.py` let you train simple models yourself and compare them with AutoML.

[⬅ Previous: Get the repo](00-get-the-repo.md) | [Next: Prerequisites and cost ➡](02-prerequisites-and-cost.md)
