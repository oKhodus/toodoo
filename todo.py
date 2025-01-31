#!/usr/bin/env python
import sys

def new():
    todo = sys.argv[0]
    correct_cmds = ["add", "rm", "upd", "sls",]
    cmd = input("Enter your cmd: ")
    print(f"your cmd in {todo} was {cmd}")
new()