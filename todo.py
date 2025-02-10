#!/usr/bin/env python
import sys
from modules import *


def main():
    try:
        todo_cmd = sys.argv[1]
        if len(sys.argv) > 1:
            todo_task = " ".join(sys.argv[2:])
        else:
            raise Exception

        cmds_ls = ["-help", "add", "rm", "upd", "showall", "showdone", "shownow"]

        implement = {
            "-help": lambda: help(cmds_ls),
            "add": lambda: add_task(todo_task) if todo_task else "Error: No task provided!",
            "rm": lambda: rm_task(todo_task) if todo_task else "Error: No task provided!",
            "showall": sls,
            "showdone": sdone,
            "shownow": snow
        }

        if todo_cmd in implement:
            print(f"Process of command: [{todo_cmd}]../../\n{implement[todo_cmd]()}")

        else:
            print(
                "Your command doesn't exists.\nType command [-help] to check list of correct commands."
            )
            raise Exception
    except Exception:
        sys.exit(1)


if __name__ == "__main__":
    main()
