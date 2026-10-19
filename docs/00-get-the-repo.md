# Step 0 – Get this repo onto your computer

[⬅ Back to README](../README.md) | [Next: Overview and key concepts ➡](01-overview-and-concepts.md)

You need the files on your own computer because in step 5 you will upload the **`data/diabetes-data`** folder from your computer into Azure Machine Learning. Pick **one** of the three options below.

---

## Option A – Download ZIP (easiest, no tools needed)

1. Open this repository's page on GitHub in your browser.
2. Click the green **`<> Code`** button near the top right of the file list.
3. Click **Download ZIP** at the bottom of the menu that opens.
4. Open your **Downloads** folder and extract the file:
   - **Windows:** right-click the downloaded `.zip` file → **Extract All...** → **Extract**.
   - **macOS:** double-click the `.zip` file. A folder appears next to it.
5. Open the extracted folder. Inside it, go to **`data`** → **`diabetes-data`**. You should see exactly two files: **`MLTable`** and **`diabetes.csv`**.

> ⚠️ **Windows users:** Windows shows a preview of a `.zip` file's contents if you double-click it, but that is **not** extracted. If the address bar shows something like `...\Downloads\azure-ml-workspace-lab-main.zip\...`, you are still inside the zip. Go back and use **Extract All...**. Uploading from inside a zip is the most common reason step 5 fails.

## Option B – Clone with Git (command line)

1. Install Git if you don't have it: https://git-scm.com/downloads (on Windows, accept all the defaults in the installer).
2. Open a terminal:
   - **Windows:** press the **Start** key, type `Git Bash`, press **Enter**.
   - **macOS:** press **Cmd + Space**, type `Terminal`, press **Enter**.
3. On the GitHub page of this repo, click the green **`<> Code`** button, make sure the **HTTPS** tab is selected, and click the **copy** icon next to the URL.
4. In the terminal, type `git clone ` (with a space at the end), paste the URL, and press **Enter**. It will look like this:

   ```bash
   git clone https://github.com/SHADRACK-NAKOBA/azure-ml-workspace-lab.git
   ```

5. Go into the folder and check the data is there:

   ```bash
   cd azure-ml-workspace-lab
   ls data/diabetes-data
   ```

   You should see `MLTable  diabetes.csv`.

## Option C – GitHub Desktop

1. Install GitHub Desktop from https://desktop.github.com and sign in.
2. On the GitHub page of this repo, click **`<> Code`** → **Open with GitHub Desktop**.
3. Choose a local path you will remember (for example `Documents\GitHub`) and click **Clone**.
4. In GitHub Desktop, click **Repository** → **Show in Explorer** (Windows) or **Show in Finder** (macOS), then open `data` → `diabetes-data`.

---

## Check before you continue

- [ ] I can see a folder called **`diabetes-data`** on my computer (not a `.zip` file).
- [ ] It contains **`MLTable`** and **`diabetes.csv`**, and nothing else.
- [ ] I know where this folder is, so I can find it again in step 5.

> **Why the repo already includes the extracted folder:** the original lab asked you to download a zip file and extract it yourself. That is where most upload errors came from (wrong folder level, uploading the zip itself, missing `MLTable`). The folder in this repo is ready to upload as it is. The zip is still included in `data/diabetes-data.zip` in case you want it.

[⬅ Back to README](../README.md) | [Next: Overview and key concepts ➡](01-overview-and-concepts.md)
