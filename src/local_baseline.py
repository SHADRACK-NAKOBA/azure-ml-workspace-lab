"""Train two quick baseline models on your own computer (free) to compare with AutoML.

Uses the same 90/10 train-test split idea as the AutoML job.

Usage (from the repo folder):
    python src/local_baseline.py
"""
from pathlib import Path

import pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

DATA = Path(__file__).resolve().parent.parent / "data" / "diabetes-data" / "diabetes.csv"


def main() -> None:
    df = pd.read_csv(DATA)
    print(f"Loaded {len(df):,} rows from {DATA.name}")

    # PatientID is an identifier, not a predictor, so drop it.
    X = df.drop(columns=["PatientID", "Diabetic"])
    y = df["Diabetic"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.10, random_state=42, stratify=y
    )

    models = {
        "Logistic regression": make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)),
        "Gradient boosting": HistGradientBoostingClassifier(random_state=42),
    }
    print(f"\n{'Model':<22}{'Accuracy':>10}{'AUC':>10}")
    for name, model in models.items():
        model.fit(X_train, y_train)
        acc = accuracy_score(y_test, model.predict(X_test))
        auc = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])
        print(f"{name:<22}{acc:>10.3f}{auc:>10.3f}")

    print("\nCompare these with the best model's Accuracy on your AutoML job's Overview tab.")


if __name__ == "__main__":
    main()
