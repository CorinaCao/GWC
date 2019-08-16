def say_hello():
    print("Hello from a function")
say_hello()

def say_name(name):
    print("Hello %s" %(name))
say_name("Corina")
say_name("Cao")
    #Hello Corina
    #Hello Cao

list = ["Fran", "Seyla", "Corina"]
def print_names(names):
    for i in names:
        print(i)
print_names(list)

list1 = ["Kaitlyn", "Jacquie", "Grace"]
list2 = ["Panda", "Bear", 21]
list3 = ["Manhattan", "Hunter", "Brooklyn"]
def print_list(anyList):
    for name in anyList:
        print(name)
print_list(list1)
print_list(list2)
print_list(list3)

def add(num1, num2):
    sum = num1 + num2
    print(sum)
add(10, 5)
add(100, 400)


def add(num1, num2):
    sum = num1 + num2
    return sum #stores file
corinasAge = 2019 - add(2000, 3)
print(corinasAge)

a = 5 #global scope
def aVariable():
    a = 10 #local scoped
    sum = a + 10
    print(sum)
aVariable()

'''
    a = 10 #local scope
print(a)
'''
