#this was is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#ok, that *args is actually pointless, we can just do this
###Definiálok egy függvényt, aminek 2 argumentuma van. A függvény 2 argumentumát
###alant határozom meg.
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

#this one takes no argument
def print_none():
    print("I got nothin'.")


print_two("Zed", "Shaw")
print_two_again("Zed1"," Shaw1")
print_one("First!")
print_none()
