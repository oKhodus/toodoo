import json


def add_task(task):
    try:
        with open("data.json", "r") as file:
            tasks = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
    tasks.append(task)

    with open("data.json", "w") as file:
        json.dump(tasks, file, indent=4)

    return f"Task was added in data.json"


def rm_task(task):
    try:
        with open("data.json", "r") as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []

    tasks.remove(task)

    with open("data.json", "w") as file:
        json.dump(tasks, file, indent=4)

    return f"Task was remove from data.json"


def sls():
    with open("data.json", "r") as file:
        tasks = "\n".join(json.load(file))
        return f"List of tasks you need to do:\n\n{tasks}".upper()


def help():
    with open("help_doc.txt", "r") as file:
        return file.read()
