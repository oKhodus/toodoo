import json


def add_task(task):
    try:
        with open("data.json", "r") as file:
            tasks = json.load(file)
            if not isinstance(tasks, dict):
                tasks = {}
    except json.JSONDecodeError:
        tasks = {}

    number = len(tasks) + 1
    name_key = f"task_{number}"
    tasks[name_key] = {"name": task, "number": number}

    with open("data.json", "w") as file:
        json.dump(tasks, file, indent=4)
    return f"Task was added in data.json"


def rm_task(task_name):
    try:
        with open("data.json", "r") as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = {}

    task_key = None
    for key, task in tasks.items():
        if task["name"] == task_name:
            task_key = key
            break

    if task_key:
        del tasks[task_key]

        with open("data.json", "w") as file:
            json.dump(tasks, file, indent=4)

        return f"Task was removed from data.json"
    else:
        return f"Task `{task_name}` not found"


def make_done(task_name):
    try:
        with open("data.json", "r") as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = {}

    task_key = None
    for key, task in tasks.items():
        if task["name"] == task_name:
            task_key = key
            break

    if task_key:
        completed_task = tasks[task_key]
# -----------------------------------------------------------------
        try:
            with open("data_done.json", "r") as file:
                done_tasks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            done_tasks = {}

        number = len(done_task) + 1
        name_key = f"task_{number}"
        done_tasks[name_key] = {"name": completed_task["name"], "number": number}

        with open("data_done.json", "w") as file:
            json.dump(done_tasks, file, indent=4)

        del tasks[task_key]

        with open("data.json", "w") as file:
            json.dump(tasks, file, indent=4)

        return f"Congrats' you've done task\nTask was removed from 'data.json' and added to 'data_done.json'"
    else:
        return f"Task `{task_name} not found in data.json`"

def sls():
    with open("data.json", "r") as read_file:
        file = json.load(read_file)
        ls = ""
        for task_name in file:
            ls += f"{file[task_name]["number"]}. {file[task_name]["name"]}\n"
        return f"\nList of tasks you need to do:\n{ls}".upper()


def sdone():
    with open("data_done.json", "r") as file:
        tasks = "\n".join(json.load(file))
        return f"\nList of tasks you've done:\n\n{tasks}".upper()


def snow():
    with open("data_inprogress.json", "r") as file:
        tasks = "\n".join(json.load(file))
        return f"\nList of tasks in progress:\n\n{tasks}".upper()


def help(cmds_ls):
    with open("help_doc.txt", "r") as file:
        return f"\n{file.read()}\nCheck full list of cmds:\n{cmds_ls}"
