q = int(input().strip())
command_list = [[x for x in map(str, input().split())] for _ in range(q)]

s = 0
def add_(x):
    global s
    s |= (1 << x)

def delete_(x):
    global s
    s &= ~(1 << x)

def print_(x):
    global s
    print((s >> x) & 1)

def toggle_(x):
    global s
    s = s ^ (1 << x)

def clear_():
    global s
    s = 0

for command in command_list:
    if command[0] == "add":
        add_(int(command[1]))
    elif command[0] == "delete":
        delete_(int(command[1]))
    elif command[0] == "print":
        print_(int(command[1]))
    elif command[0] == "toggle":
        toggle_(int(command[1]))
    elif command[0] == "clear":
        clear_()
