name=input("what's your name ?")
print("hello "+name)




def sum(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

x=float(input("first_number :"))
y=float(input("second_number :"))


print("Select operation.")

print("NOTICE!!!      Available operators are ( + , - , * , / )")


operator= input("which operator :")



if operator == '+':
    print("result is :",x,"+",y,"=", sum(x,y))
elif operator == '-':
    print("result is :",x,"-",y,"=", sub(x,y))
elif operator == '*':
    print("result is :",x,"*",y,"=", mul(x,y))
elif operator == '/':
    print("result is :",x,"/",y,"=", div(x,y))
else:
    print("format_invalid")