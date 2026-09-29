# Troubleshooting

> **Workspace repository name:** Batch 10 uses `batch10-workspace`. Confirm this name on your Portal profile under **Course workspace setup**. This is a private repository in your own GitHub account, separate from `LDSSA/batch-students`.

[1. When I open Windows Explorer through Ubuntu, it goes to a different folder than in the guide](#1-when-i-open-windows-explorer-through-ubuntu-it-goes-to-a-different-folder-than-in-the-guide)
[2. Ubuntu on Windows 10/11 has high CPU usage or crashes](#2-ubuntu-on-windows-1011-has-high-cpu-usage-or-crashes)
[3. When I pull from the `batch-students` repository, I get an error](#3-when-i-pull-from-the-batch-students-repository-i-get-an-error)
[4. When I try to open a Jupyter notebook, I get an error](#4-when-i-try-to-open-a-jupyter-notebook-i-get-an-error)
[5. When I use the `cp` command the `>` sign appears and the command does not execute](#5-when-i-use-the-cp-command-the--sign-appears-and-the-command-does-not-execute)
[6. When installing Python 3.14, `apt update` reports a repository error](#6-when-installing-python-314-apt-update-reports-a-repository-error)
[7. Nothing happens when I type my password](#7-nothing-happens-when-i-type-my-password)
[8. I still have a NotImplemented error](#8-i-still-have-a-notimplemented-error)
[9. Tutorial videos from Prep Course 2020](#9-tutorial-videos-from-prep-course-2020)
[10. Error 0x80370102 when installing WSL](#10-error-0x80370102-when-installing-wsl)
[11. Errors when installing WSL on Windows](#11-errors-when-installing-wsl-on-windows)

### 1. When I open Windows Explorer through Ubuntu, it goes to a different folder than in the guide

Please make sure:

- you are running the command `explorer.exe .` including the dot at the end.
- you are running Windows 10 version `2004`, build `19041`, or newer, or Windows 11.

### 2. Ubuntu on Windows 10/11 has high CPU usage or crashes

- Make sure you are running Windows 10 version `2004`, build `19041`, or newer, or Windows 11.
- Follow Microsoft's [WSL troubleshooting guide](https://learn.microsoft.com/windows/wsl/troubleshooting).

### 3. When I pull from the `batch-students` repository, I get an error

If you get an error like the following when pulling:

```
error: Your local changes to the following files would be overwritten by merge:
<some files>
Please commit your changes or stash them before you merge.
Aborting
```

What `git` is telling you is that you changed files in the `~/projects/batch-students` folder. Git does not pull the instructors' changes because doing so would overwrite your local changes.

To fix this do the following:

1. Make sure that any changes you made in `~/projects/batch-students` that you want to keep are saved in `~/projects/batch10-workspace` (refer to [Updates to Learning Units](ldssa-workflow.md#4-updates-to-learning-units)). If you don't want to keep those changes, continue to the next step.
2. Go to the `~/projects/batch-students` folder and run:

    ```bash
    cd ~/projects/batch-students
    git stash
    ```

3. Now you can pull from the `batch-students` repository:

    ```bash
    git pull
    ```

### 4. When I try to open a Jupyter notebook, I get an error

Make sure that your virtual environment is activated **before** opening the Jupyter notebook.

```bash
source ~/.virtualenvs/s01/bin/activate
```

### 5. When I use the `cp` command the `>` sign appears and the command does not execute

```bash
cp -r ~/projects/batch-students/"S01 - Bootcamp and Binary Classification"/"SLU01 - Pandas 101" ~/projects/batch10-workspace/"S01 - Bootcamp and Binary Classification"/
>
```

Make sure to use this type of quotes `"` and not this one `“`.

### 6. When installing Python 3.14, `apt update` reports a repository error

If `sudo apt update` reports a GPG, signature or release-file error for a third-party repository, that repository must be corrected or disabled before Ubuntu can install packages reliably.

The error is not caused by Python. Do not add the Deadsnakes PPA on Ubuntu 26.04, and do not import an unknown key globally with the deprecated `apt-key` command. Ask in `#devops` if you are unsure which third-party source is safe to change.

### 7. Nothing happens when I type my password

When you type your password in the terminal, it is not visible. This is normal, just type the password and hit <kbd>enter</kbd>.

### 8. I still have a NotImplemented error

I've completed the exercise in the Exercise Notebook but when I run the cell I get a **NotImplementedError**.

Solution:
The `raise NotImplementedError()` is added to the exercise cell as a placeholder for where you're supposed to add your solution/code. It is meant to be removed!

### 9. Tutorial videos from Prep Course 2020

🎁🎬 Check the **tutorial videos** if you have any doubts after following this tutorial. These videos were made for the **Prep Course of year 2020**, so there may be some differences.

- [Setup guide for Windows - Part 1](https://www.youtube.com/watch?v=fWi3bYoHW18)
- [Setup guide for Windows - Part 2](https://www.youtube.com/watch?v=bnJOQHh9pJ4)
- [Setup guide for Mac](https://www.youtube.com/watch?v=qs0z4ibMFdU)
- [Updates to Learning Units guide for Windows 10](https://www.youtube.com/watch?v=Q2Cezm6ufrE)
- [Updates to Learning Units guide for Mac](https://www.youtube.com/watch?v=-fzIDfNBZ0I)

### 10. Error 0x80370102 when installing WSL
Follow the steps [here](https://support.microsoft.com/en-us/windows/enable-virtualization-on-windows-11-pcs-c5578302-6e43-4b4b-a449-8ced115f58e1).

### 11. Errors when installing WSL on Windows
See the troubleshooting guide from [Microsoft](https://learn.microsoft.com/en-us/windows/wsl/troubleshooting).
