# How to set up Python virtual environments

Batch 10 uses **Ubuntu 26.04 LTS** and **Python 3.14**. A virtual environment keeps the packages for each specialization separate from your operating system and from the other specializations.

Create one virtual environment for each specialization, named `s01` through `s06` in the examples below.

## 1. Install virtual-environment support

On Ubuntu 26.04, run:

```bash
sudo apt update
sudo apt install python3.14 python3-pip python3.14-venv -y
```

Mac users can skip this section after installing Python 3.14 through the [macOS guide](macOS.md).

Verify the interpreter before creating an environment:

```bash
python3.14 --version
```

The output must start with `Python 3.14`.

## 2. Create and activate an environment

Create the S01 environment:

```bash
python3.14 -m venv ~/.virtualenvs/s01
```

Activate it:

```bash
source ~/.virtualenvs/s01/bin/activate
```

The environment name should appear at the start of the prompt. Confirm that `python` now points inside the environment:

```bash
which python
python --version
```

Example output:

```text
/home/student/.virtualenvs/s01/bin/python
Python 3.14.x
```

Update pip inside the active environment:

```bash
python -m pip install --upgrade pip setuptools wheel
```

## 3. Install specialization packages

Every specialization contains its own `requirements.txt`. With the corresponding environment active, enter the specialization directory in `batch10-workspace` and install it. For S01:

```bash
cd ~/projects/batch10-workspace/"S01 - Bootcamp and Binary Classification"
python -m pip install -r requirements.txt
```

Install an individual package only when course instructions require it:

```bash
python -m pip install matplotlib pandas
```

Changes to your local packages do not change the packages used by the Portal grader. Do not edit `requirements.txt` unless instructors explicitly ask you to.

## 4. Leave, inspect or recreate an environment

Deactivate the active environment:

```bash
deactivate
```

List your environments:

```bash
ls ~/.virtualenvs
```

If an environment is broken, deactivate it, remove its directory, and recreate it from the specialization requirements:

```bash
deactivate
rm -r ~/.virtualenvs/s01
python3.14 -m venv ~/.virtualenvs/s01
source ~/.virtualenvs/s01/bin/activate
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r ~/projects/batch10-workspace/"S01 - Bootcamp and Binary Classification"/requirements.txt
```

Be certain that the path after `rm -r` is the intended virtual-environment directory before running the command.

## References

- [Python `venv` documentation](https://docs.python.org/3/library/venv.html)
- [Python Packaging User Guide](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
