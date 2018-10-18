import collections
import arrow

tasks = collections.defaultdict(list)

def validate_date(f):
    def wrapper(date, *args):
        try:
            arrow.get(date,'DD.MM.YY')
        except arrow.parser.ParserError:
            raise ValueError["Incorrect date"]
        return f(date,  *args)
    return wrapper

@validate_date
def add_task(date, task):
   # validate_date(date)
    tasks[date].append[task]


@validate_date
def delete():
    # validate_date(date)
    date = input("Date?")
    index = input("index in list?")
    try:
        tasks[date].pop(int(index) - 1)
    except (KeyError, IndexError, ValueError):
        raise ValueError("incorrect input")

@validate_date
def list_tasks(date):
    # validate_date(date)
    if date in tasks and tasks[date]:
        try:
            tasks[date].pop(int() - 1)
        except (KeyError, IndexError, ValueError):
            raise ValueError("incorrect input")

#########  1
def date_input():
    date = input("Date?")
    task = input("Task?")
    if date not in tasks:
        tasks[date] = [task]
    else:
        tasks[date].append(task)

######### 2

def validate_date_exist(tasks):
    date = input("Task exist on the date?")
    if date in tasks and tasks[date]:
        for index, task in enumerate(tasks[date], 0):
            print(index, tasks)
        else:
            tasks[date].append(task)
    print("No tasks on this date")


#############  3

def pop_date_record(date, index):
    try:
        tasks[date].pop(index)
    except (KeyError, IndexError):
        print("incorrect input")

        ###########  4
def show_actions():
    return input("""input: 
                        a - add atask
                        v- validate date exist
                        l -List of tasks
                        d - delete task
                        q - quit
                        """).lower()

###############
#
# def composition(f, g):
#     return lambda x: f(g(x))

def check_function(action):
    if action == 'q':
        exit()
    elif action == 'a':
        add()
    elif action == 'l':
        list()
    elif action == 'd':
        delete()
    else:
        print("Incorrect action")

####################  main

while True:
    action = show_actions()
    check_function(action)
print(tasks)