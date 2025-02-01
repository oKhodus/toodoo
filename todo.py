#!/usr/bin/env python
import sys, json

from modules import *

def new():
    todo_cmd = sys.argv[1]
    if len(sys.argv) > 1:
        todo_task = " ".join(sys.argv[2:])

    correct_cmds = ["add", "rm", "upd", "sls"]

    if todo_cmd in correct_cmds:
        print(f"your cmd was [{todo_cmd}]../../\n")
        if todo_cmd == "add": print(add_task(todo_task))
        if todo_cmd == "rm": print(rm_task(todo_task))
        if todo_cmd == "sls": print(sls())
        
    
new()