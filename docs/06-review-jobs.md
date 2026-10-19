# Step 6 – Use Jobs to view your history

[⬅ Previous: Train a model with AutoML](05-train-with-automl.md) | [Next: Share your learnings ➡](07-share-your-learnings.md)

After you submit, the studio takes you to the job's page. **Jobs** keep track of the work you've run so you can compare runs. Each job belongs to an **experiment**, which groups related runs together.

## 6.1 Watch the job run

1. On the job's **Overview** tab, look at the **Properties** section:
   - **Status:** moves through *Not started* → *Queued* → *Running* → **Completed**
   - **Created by:** you
   - **Created on:** when you submitted it
   - **Duration:** how long it has been running
   - **Compute target:** serverless
2. A job usually takes **15–30 minutes**. The first few minutes are spent starting the serverless machine, so *Not started* or *Queued* for up to 10 minutes is normal.
3. The page doesn't always refresh by itself. Click **Refresh** at the top every few minutes.

> **Finding the job again later:** left menu → **Jobs** → **All experiments** tab → click **mslearn-diabetes-automl** (or your experiment name) → click your job's display name.

## 6.2 Explore the results once the status is Completed

1. **Overview tab:** in the **Best model summary** box, see the algorithm AutoML picked and its **Accuracy**. Expect something **around 0.9 or higher** (90%+ of test patients classified correctly). A *VotingEnsemble* or a boosted-tree model (*LightGBM*, *XGBoostClassifier*) usually comes out on top.
2. **Data guardrails tab:** the automatic checks AutoML ran on your data, such as class balancing, missing values and high-cardinality features. With this dataset, they should all be *Passed* or *Done*.
3. **Models + child jobs tab:** every model AutoML tried (up to 10), sorted by Accuracy. Click the **Algorithm name** of the top model to open its details, then:
   - **Metrics** tab: accuracy, AUC, precision/recall, plus charts such as the **confusion matrix** and **ROC curve**.
   - **Explanations** tab (if shown): which features mattered most. *PlasmaGlucose*, *Pregnancies*, *Age* and *BMI* are usually near the top.
4. **Child jobs** (in the Jobs list): the individual component runs, including outputs and logs.
5. **Outputs + logs tab** (on the parent job): the files the job produced and its logs. This is where you look first if a job fails.

## 6.3 Why this matters

Azure Machine Learning records every job's properties automatically. Using jobs you can:

- look back at what you and your colleagues have already tried,
- compare the models you trained during experimentation and pick the best,
- in production, check that automated workloads ran as expected.

> 💡 **Save your proof now.** Take screenshots of the **Overview** tab (with *Completed* and the best Accuracy) and the **Models + child jobs** tab. You'll use them in step 7.

## Check before you continue

- [ ] Your job status is **Completed** (or *Completed* with a short "early termination" note, which is fine).
- [ ] You know the best algorithm and its Accuracy.
- [ ] You've saved your screenshots.

If the job **Failed**, open **Outputs + logs** and then [Troubleshooting E8](09-troubleshooting.md#e8-the-automl-job-failed).

[⬅ Previous: Train a model with AutoML](05-train-with-automl.md) | [Next: Share your learnings ➡](07-share-your-learnings.md)
