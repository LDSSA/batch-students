# Creating a Python virtual environment

Batch 10 uses **Ubuntu 26.04 LTS** and **Python 3.14**. For a more detailed explanation, see [How to set up Python virtual environments](How_to_set_up_python_virtual_environments.md).

:warning: **Always use a virtual environment to install course packages.** Installing them into the operating system's Python can create dependency conflicts.

You need one virtual environment for each specialization, S01 through S06.

## 1. Install the required Ubuntu packages

On Ubuntu 26.04, run:

```bash
sudo apt update
sudo apt install python3.14 python3-pip python3.14-venv -y
```

If you use macOS, first install Python 3.14 by following the [macOS guide](macOS.md).

## 2. Create the S01 environment

```bash
python3.14 -m venv ~/.virtualenvs/s01
```

## 3. Activate the environment

```bash
source ~/.virtualenvs/s01/bin/activate
```

The environment name should now appear at the beginning of the prompt:

```text
student@computer:~$ source ~/.virtualenvs/s01/bin/activate
(s01) student@computer:~$
```

Confirm that the environment uses Python 3.14:

```bash
python --version
which python
```

The output should start with `Python 3.14` and point to `~/.virtualenvs/s01/bin/python`.

## 4. Update the packaging tools

```bash
python -m pip install --upgrade pip setuptools wheel
```

The environment is ready. Activate it whenever you work on S01, and repeat the process with `s02` through `s06` for the later specializations.
