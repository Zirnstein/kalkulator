operation = raw_input("Choose math operation (+, -, *, /): ")

x = int(raw_input("Enter the value for x: "))
y = int(raw_input("Enter the value for y: "))

# ce ni inta, jih da samo skup
# print(x+y)
# print(int("Hello"))
# x = 1
# y = x == 1
# print(x)
# print(y)

if operation == '+':
    print (x+y)
elif operation == '-':
    print(x-y)
elif operation == '*':
    print(x*y)
elif operation == '/':
    print(x/y)
else:
    print ('Not OK')
    raise ValueError('Wrong operation!')






