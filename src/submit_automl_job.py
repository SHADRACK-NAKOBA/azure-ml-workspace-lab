"""Create the training data asset and submit the lab's AutoML classification job.

This is the code version of docs/05-train-with-automl.md. It uses exactly the same
settings as the portal steps:
    task: classification          target column: Diabetic
    primary metric: accuracy      max trials: 10
    experiment timeout: 60 min    iteration (trial) timeout: 15 min
    early termination: on         test data: train-test split, 10%
    compute: serverless, Standard_DS3_v2, 1 instance

Usage (Cloud Shell, inside the repo, with the virtual environment active):
    python src/submit_automl_job.py
    python src/submit_automl_job.py --vm-size Standard_DS2_v2     # if DSv3 quota is missing
    python src/submit_automl_job.py --wait                         # stream logs until it finishes
"""
import argparse
from pathlib import Path

from azure.ai.ml import Input, automl
from azure.ai.ml.constants import AssetTypes
from azure.ai.ml.entities import Data, ResourceConfiguration

from workspace import get_ml_client

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_FOLDER = REPO_ROOT / "data" / "diabetes-data"


def build_job(training_data: Input, experiment: str, vm_size: str):
    job = automl.classification(
        experiment_name=experiment,
        training_data=training_data,
        target_column_name="Diabetic",
        primary_metric="accuracy",
        test_data_size=0.1,               # Train-test split, 10% test data
        enable_model_explainability=True,
    )
    job.set_limits(
        max_trials=10,
        timeout_minutes=60,               # Experiment timeout
        trial_timeout_minutes=15,         # Iteration timeout
        enable_early_termination=True,
    )
    # No compute target set = serverless compute. Choose the VM size here.
    job.resources = ResourceConfiguration(instance_type=vm_size, instance_count=1)
    return job


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--data-name", default="training-data", help="data asset name")
    parser.add_argument("--experiment", default="mslearn-diabetes-automl")
    parser.add_argument("--vm-size", default="Standard_DS3_v2")
    parser.add_argument("--wait", action="store_true", help="stream the job until it finishes")
    args = parser.parse_args()

    if not (DATA_FOLDER / "MLTable").is_file() or not (DATA_FOLDER / "diabetes.csv").is_file():
        raise SystemExit(f"Expected MLTable and diabetes.csv in {DATA_FOLDER}. "
                         f"Re-clone the repo - these files must not be moved or renamed.")

    ml_client = get_ml_client()

    # 1. Create (or add a new version of) the MLTable data asset by uploading the folder.
    print(f"Uploading {DATA_FOLDER.relative_to(REPO_ROOT)} as data asset '{args.data_name}'...")
    data_asset = ml_client.data.create_or_update(
        Data(
            name=args.data_name,
            path=str(DATA_FOLDER),
            type=AssetTypes.MLTABLE,
            description="Diabetes training data (Prince Azure ML lab)",
        )
    )
    print(f"Data asset ready: {data_asset.name}, version {data_asset.version}")

    # 2. Build and submit the AutoML job.
    training_data = Input(type=AssetTypes.MLTABLE,
                          path=f"azureml:{data_asset.name}:{data_asset.version}")
    job = build_job(training_data, args.experiment, args.vm_size)
    returned_job = ml_client.jobs.create_or_update(job)

    print()
    print(f"Submitted job: {returned_job.name}")
    print(f"Experiment:    {args.experiment}")
    print(f"Status:        {returned_job.status}")
    print(f"Open in studio: {returned_job.studio_url}")
    print("It usually takes 15-30 minutes. Continue with docs/06-review-jobs.md.")

    if args.wait:
        ml_client.jobs.stream(returned_job.name)


if __name__ == "__main__":
    main()
