# Creating a Python Virtual Environment

Bellow are the instructions that are enough get you up and running :)
You can also follow [this guide](How_to_set_up_python_virtual_environments.md) for a more in depth set of instructions that accomplish exactly the same thing.

:warning: **You should always be using a virtual environment to install python packages.** :warning: Otherwise you can overwrite packages in your system Python installation and break things.

You will need a virtual environment for each specialization (S01 - S06). We will use the _venv_ package to create the virtual environment and _pip_ (the reference Python package manager) to install and update packages.

**Step 1** Start by ensuring pip, setuptools, and wheel are up to date:

```bash
python3.12 -m pip install --user --upgrade pip setuptools wheel
```
If you get an error at this point, run the following command, then repeat the line above.
```bash
python3.12 -m ensurepip --upgrade
```

**Step 2** Create a virtual environment with the name `s01` for the specialization S01:

```bash
python3.12 -m venv ~/.virtualenvs/s01
```

**Step 3** Activate the environment

```bash
source ~/.virtualenvs/s01/bin/activate
```

>Note: after you activate your virtual environment you should see the name of your virtual environment surrounded by parenthesis at the beginning of your command line, like this:

```bash
mig@my-machine % source ~/.virtualenvs/s01/bin/activate
(s01) mig@my-machine %
```

Now if you use the `which` command it should output the location of your virtual environment's Python installation:

```bash
(s01) mig@my-machine % which python
/Users/mig/.virtualenvs/s01/bin/python
```

**Step 4** Now update pip.

```bash
(s01) pip install -U pip
```

And you're done!
