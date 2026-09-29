# Setup instructions for Windows 10/11

Batch 10 uses **Ubuntu 26.04 LTS** through Windows Subsystem for Linux (WSL) and **Python 3.14**. Run all Linux, Git, Python and Jupyter commands for the Academy inside the Ubuntu terminal.

## 1. Install WSL and Ubuntu 26.04

Follow the [WSL installation guide](Windows_Subsystem_for_Linux_Installation_Guide_for_Windows_10.md). Use the Ubuntu 26.04 distribution.

## 2. Install Git and Python 3.14

Open the Ubuntu terminal and run:

```bash
sudo apt update
sudo apt install git python3.14 python3-pip python3.14-venv -y
```

Confirm the installations:

```bash
git --version
python3.14 --version
```

The Python output must start with `Python 3.14`.

You are ready to return to the main README and continue with Git and GitHub setup.
