import json


def add_task(task):
    try:
        with open("data.json", "r") as file:
            tasks = json.load(file)
            # print(task)
            tasks.append(task)
            return task

        
        # n = 1
        # new_task = {task: n}

        # with open("data.json", "w") as file:
        #     json.dump(tasks, file, indent=4)
    except Exception as e:
        print("nea", e)
    # return f"Task was added in data.json"


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
        # tasks = "\n".join(json.load(file))
        tasks = json.load(file)
        return f"\nList of tasks you need to do:\n\n{tasks}".upper()

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
        return f"{file.read()}\nCheck full list of cmds:\n{cmds_ls}"
