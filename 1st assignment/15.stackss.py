def push(x):
    stack.append(x)
def empty():
    if (len(stack) == 0):
        return True
    else:
        False
def pop():
    if empty():
        print("its's empty")
    else:
        stack.pop()
def check_empty():
    if empty():
        print("the stack is empty")
    else:
        print("the stack is not empty")
stack=[]
push(5)
push(10)
pop()
check_empty()