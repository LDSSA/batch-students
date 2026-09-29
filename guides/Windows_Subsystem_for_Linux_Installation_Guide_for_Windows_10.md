# Windows Subsystem for Linux installation guide

Batch 10 uses Ubuntu through Windows Subsystem for Linux (WSL). These instructions apply to Windows 11 and to Windows 10 version 2004 or later, build 19041 or later.

## 1. Check Windows Update

Install pending Windows updates and restart before installing WSL. On Windows 10, run `winver` and confirm that the build is at least 19041.

## 2. Install WSL and Ubuntu 26.04

Open PowerShell as Administrator and list the available Linux distributions:

```powershell
wsl --list --online
```

Install Ubuntu 26.04 using the exact distribution name shown by that command. Normally this is:

```powershell
wsl --install -d Ubuntu-26.04
```

Restart Windows if requested. If WSL is already installed, the same command adds Ubuntu 26.04 without removing another distribution.

If `wsl --install` is unavailable or fails, follow Microsoft's current [manual WSL installation instructions](https://learn.microsoft.com/windows/wsl/install-manual). For error `0x80370102`, enable virtualization by following [Microsoft's virtualization instructions](https://support.microsoft.com/windows/enable-virtualization-on-windows-11-pcs-c5578302-6e43-4b4b-a449-8ced115f58e1).

## 3. Create the Ubuntu user

Launch **Ubuntu 26.04** from the Start menu. The first launch completes installation and asks you to create a Linux username and password.

The Linux username does not need to match your Windows username. Password characters are not displayed in the terminal; this is normal. Remember the password because Ubuntu requests it when you run commands with `sudo`.

## 4. Open the Ubuntu terminal

Whenever this course asks you to open a terminal on Windows, open **Ubuntu 26.04** from the Start menu or open a Windows Terminal tab using the Ubuntu profile.

Update the Ubuntu package catalogue after the first launch:

```bash
sudo apt update
sudo apt upgrade -y
```

## 5. Open WSL files in Windows Explorer

Inside the Ubuntu terminal, enter the directory you want to view and run:

```bash
explorer.exe .
```

The final dot means “the current directory” and must be included. Keep course repositories inside your Linux home directory, for example `~/projects`, rather than under `/mnt/c`, for better Linux tool and file-permission behavior.

You are ready to return to the [Windows setup guide](WINDOWS.md) and install Git and Python 3.14.
