# LDSSA Learning Units

## 1. Structure of the batch-students repository
The repository has a directory for each specialization S01 - S06. Inside are the directories for the learning units. See the example below:

```
|--S01
   |-- requirements.txt
   |-- SLU01 - Pandas 101
       |-- media
           |-- some-image.csv
       |-- data
           |-- some-dataset.csv        
       |-- Examples notebook.ipynb
       |-- Exercise notebook.ipynb
       |-- Learning notebook.ipynb
       |-- README.md    
   |-- SLU02 - Subsetting Data in Pandas
       ...    
   |-- SLU03 - Visualization with Pandas and Matplotlib   
       ...           
```

The learning unit directory naming follows the convention

```markdown
<specialization ID> - <specialization name>/<learning unit ID> - <learning unit name>
```

The LU directory contains the `README` (a markdown file with the description of the unit), the `Learning notebook`, the `Exercise notebook`, and the `Examples notebook`. It may also contain a `media` directory with all the visual material, the `data` directory with the datasets, and a `utils.py` file with helper code.

The notebooks are all Jupyter notebooks, the same as you worked with during the admissions process. They contain text, interactive code, and tests for your solutions in the exercises.

The `requirements.txt` file in each specialization directory contains the packages to be installed in the virtual environment. 

Please keep this directory structure also in your workspace repository because the grader in the portal depends on it.

## 2. Get new learning material

You will need to follow this workflow whenever new learning material is released. Learning units release will be announced in the _#announcements_ channel on Slack.
At this point they will be available in this repository.
A new Learning Unit is usually released on Monday mornings.

To get the new material, enter your local copy of this repo and pull from the repo:

```bash
cd ~/projects/batch-students/
git pull
```

Copy the Learning Unit folder to your local `batch8-workspace`:

```bash
cp -r ~/projects/batch-students/"<specialization ID> - <specialization name>"/"<learning unit ID> - <learning unit name>" ~/projects/batch8-workspace/"<specialization ID> - <specialization name>"
```

For example, for the `S01 - Bootcamp and Binary Classification` and `SLU01 - Pandas 101`, it would look like this:

```bash
cp -r ~/projects/batch-students/"S01 - Bootcamp and Binary Classification"/"SLU01 - Pandas 101" ~/projects/batch8-workspace/"S01 - Bootcamp and Binary Classification"
```

:warning: It is important to copy just the newly release LU folders, otherwise you can overwrite your already solved Exercise notebooks.

## 3. Working on a Learning Unit

### 3.1 Create a virtual environment for the current specialization
You will need a new virtual environment for every specialization. You have already created one for S01 during the previous setup steps. Here we will repeat some of those steps so that you have a complete guide for when you start each specialization.
 
1. Open the terminal and create the virtual environment for the specialization:

```bash
python3.12 -m venv ~/.virtualenvs/s01
```
1. Activate the virtual environment of the specialization:

```bash
source ~/.virtualenvs/s01/bin/activate
```

1. Enter the directory of the specialization and install the requirements:

```bash
cd ~/projects/batch8-workspace/"S01 - Bootcamp and Binary Classification"
pip install -r requirements.txt
```

You will see a lot of output on the terminal while pip installs the packages. You can also notice possible errors.

### 3.2 Launch the Jupyter notebook

1. Enter the learning unit directory in your workspace directory (`batch8-workspace`).

    >Note: It is **VERY IMPORTANT** that you **ALWAYS** work on the files in your `batch8-workspace` repository, and **NEVER** change the files in the `batch-students` local repository! If you do change these files, you can have a merge conflict when you next pull from the GitHub repository.

```bash
cd ~/projects/batch8-workspace/"S01 - Bootcamp and Binary Classification"/"SLU01 - Pandas 101"
```

1. Activate the correct virtual environment 

```bash
source ~/.virtualenvs/s01/bin/activate
```

1. Run the Jupyter notebook:

```bash
jupyter notebook
```
If the previous command does not work, use this one:

```bash
jupyter notebook --NotebookApp.use_redirect_file=False
```

You should see something similar to this in your terminal:
![Open exercise notebook](/media/jupyter_terminal.png "Open exercise notebook")
Your browser should pop up with Jupyter open, however, if this does not happen, you can simply copy the link you see on your terminal (the one that contains `localhost`) and paste it in your browser's address bar:

![Open exercise notebook](/media/jupyter_terminal_link.png "Open exercise notebook")

>Note: If you see these scarry looking error messages, don't worry, you can just ignore them.

![Open exercise notebook](/media/jupyter_error_red.png "Open exercise notebook")

### 3.3 Solve the Exercise Notebook

After you have studied the Learning Notebook, do the exercises in the Exercise notebook. The notebook has cells where you should write your solutions followed by cells with tests for the solutions. The tests are series of `assert` statements. If all the asserts pass, that is if you don't get an `AssertionError` or any other kind of error, your solution is correct. 

The failing asserts usually give you a hint about the error. Other kinds of errors given by Python will produce a lot of tracebacks indicating the line where the error occured. 

Once you've solved all the exercises, we recommend to follow this simple
checklist to avoid unexpected surprises:

1. Save the notebook (again)
1. Run "Restart & Run All"
![Restart & Run All](/media/jupyter_clear_and_run.png "Restart & Run All")
1. At this point the notebook should have run without any failing assertions

If you want to submit your notebook before it is done all the way to
check intermediate progress, feel free to do so. The grader in the portal will run all your code, even if there are errors further up in the notebook.

Warning: if you use a different software, e.g. VSCode, to complete the exercise notebook, the portal might not be able to grade it. VSCode can add something to the notebook and the portal won't be able to recognize the notebook.

### 3.4 Commit and push the Exercise notebook to your repo

Now you have worked on the exercise notebooks, you should commit the changes to your local repository and transfer them to your GitHub repository. You can test this workflow with the notebooks from the admission process, SLU01, SLU02, and SLU03.

Using the terminal, commit and push the changes (from the LU directory):

```bash
git add .
git commit -m 'Completed SLU01'
git push
```

### 3.5 Grade the Exercise notebook

Now go to the portal and ask it to grade your notebook.

1. Go to the [_Portal_](https://portal.lisbondatascience.org) and select the learning unit
![Learning unit](/media/portal_sample_lu.png "Learning unit")
1. Select "Grade"
![Grade](/media/portal_grade.png "Grade")
1. The `Last Grade` status will change to `Sent`. The portal is now running your notebook. It can take some time, depending on the complexity of the code.
1. Your grade will appear next, e.g. 20/20.
1. If all the exercise asserts passed locally but the grader doesn't give you the expected
output head to [troubleshooting](https://github.com/LDSSA/LDSA-setup/blob/main/troubleshooting.md)
1. You can check the state of the notebook in the portal by clicking on the grade and selecting `Raw Data`. It will show the notebook in plain text and you can search for possible errors.

## 4. Updates to Learning Units

As much as we try and have processes in place to prevent errors and bugs in
the learning units some make it through to you.

If the problem is not in the exercise notebook you can just pull the new
version from the students repo and replace the file. Take care to not overwrite other files.

If the correction is in the exercise notebook, you can't just
replace the file because your work is there and you'll lose it!

When a new version of the exercise notebook is released two
things will happen.
If you submit an old version of the notebook it will be flagged as out of date
and not graded.
You will have to merge the work you've already done into the new version of the
notebook.

Our suggestion to merge the changes is:

1. Rename the old version
1. Copy the new exercise notebook to your workspace repo
1. Open both notebooks and copy-paste your solutions to the new notebook

We understand it's not ideal and are working on improving this workflow using
[_nbdime_](https://nbdime.readthedocs.io/).
If you are comfortable installing Python packages you can try it out, but
we offer no support for this at the moment.

## 4. Help

During the academy you will surely run into problems and have doubts about the
material.
We provide you with some different channels to ask for help.

### 4.1 Learning Unit

If you feel something is not clear enough or there is a bug in the learning
material please follow [these steps](https://ldssa.github.io/wiki/Starters%20Academy%20(LDSSA)/How-to-ask-for-and-give-help/). Remember, there is no such thing as a dumb question, and by asking questions publicly you will help others!

### 4.2 Portal

Are you getting different results locally than in the
Portal? If so we will first ask you to do a bit of troubleshooting:

1. Ensure that you have saved the changes in the notebook
1. Ensure that you have committed and pushed the changes
1. Ensure that you are not using packages that are not present in the original
`requirements.txt` file (changes to this file or your local environment have no
effect)
1. In the learning unit page in the [_Portal_](https://portal.lisbondatascience.org/)
you are able to download the exercise notebook with the results of the grader
by clicking on your grade. Have a look to figure out what went wrong.
![Download notebook](/media/portal_download_notebook.png "Download notebook")
If none of these steps helped go ahead and ask for help on Slack in the #devops channel.

Is the _Portal_ down or acting out in some unexpected way? Please report it in the #devops channel on Slack.

