#!/usr/bin/env python
import sys, json

from modules import *


def main():
    todo_cmd = sys.argv[1]
    if len(sys.argv) > 1:
        todo_task = " ".join(sys.argv[2:])

    correct_cmds = ["-help", "add", "rm", "upd", "sls", "sls/d", "sls/p"]

    if todo_cmd in correct_cmds:
        print(f"your cmd was [{todo_cmd}]../../\n")
        if todo_cmd == "add":
            print(add_task(todo_task))
        elif todo_cmd == "rm":
            print(rm_task(todo_task))
        elif todo_cmd == "sls":
            print(sls())
        elif todo_cmd == "-help":
            print(help())
    else:
        print(
            "Your command doesn't exists.\nType [-help] to check list of correct commands."
        )


if __name__ == "__main__":
    main()
