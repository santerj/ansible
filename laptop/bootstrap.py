#!/usr/bin/python

import getpass
import os
import platform
import subprocess

def printc(text, color):
    # color output with ansi escape sequences
    if color == "red":
        seq = "\033[91m"
    elif color == "green":
        seq = "\033[92m"
    else:
        raise Exception("Check printc colors")
    end = "\033[0m"
    print(f"{seq}##### {text}{end}")

def run(cmd):
    code = subprocess.call(cmd, shell=True, executable='/bin/sh')
    if code != 0:
        printc(f"Error: received return code {code} from command {cmd}", "red")
        exit(0)
    return code

def main():
    print(f"Python {platform.python_version()} on {platform.machine()}")

    c = ""
    while c not in ("y", "n"):
        print("Ready to go? [y/n]", end=" ")
        c = input().lower()
        if c == "n":
            exit(0)
        elif c == "y":
            pw = getpass.getpass(prompt="Enter password (if none, press Enter):")
            print("Running complete bootstrap. This might take a while.")

    printc("Setting up virtualenv...", "green")
    run("python3 -m venv --system-site-packages venv")
    run("venv/bin/python -m pip install --upgrade -q --no-input pip")

    printc("Installing dependencies...", "green")
    run("venv/bin/python3 -m pip install -q --no-input ansible")
    run("venv/bin/ansible-galaxy collection install community.general ansible.posix")

    printc("Starting Ansible", "green")
    run(f"venv/bin/ansible-playbook playbook.yml \
        --extra-vars \"ansible_become_pass={pw}\" \
        --extra-vars \"ansible_python_interpreter=venv/bin/python\"")

    printc("Cleaning up...", "green")
    run("rm -rf venv")

    c = ""
    while c not in ("y", "n"):
        print("Done! Ready to reboot? [y/n]", end=" ")
        c = input().lower()
        if c == "n":
            exit(0)
        elif c == "y":
            os.system('reboot')

main()
