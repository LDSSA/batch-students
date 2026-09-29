# Setup instructions for Linux

Batch 10 uses **Ubuntu 26.04 LTS** and **Python 3.14**.

## 1. Install Python 3.14

Ubuntu 26.04 provides Python 3.14 directly from its package repositories:

```bash
sudo apt update
sudo apt install python3.14 python3-pip python3.14-venv -y
```

Confirm the version:

```bash
python3.14 --version
```

The output must start with `Python 3.14`.

If `apt update` reports an error from an unrelated third-party repository, see [the troubleshooting guide](troubleshooting.md#6-when-installing-python-314-apt-update-reports-a-repository-error).

## 2. Install Git

```bash
sudo apt install git -y
```

Verify the required tools:

```bash
git --version
python3.14 --version
```

You are ready to return to the main README and continue with Git and GitHub setup.
