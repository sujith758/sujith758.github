import sys

# To ensure that arguments are passed
if not len(sys.argv) == 4:
    print("Provide arguments:operator,Num1,Num2!")
    sys.exit()
# Arguments must be given
arg1 = sys.argv[1]
arg2 = sys.argv[2]
arg3 = sys.argv[3]
# Giving variables to arguments
cal = arg1
num1 = arg2
num2 = arg3
result = 0
if not(arg2.isdigit()):
    print("Provide digit type<int>!")
    sys.exit(1)
if not(arg3.isdigit()):
    print("Provide digit type<int>")
    sys.exit(1)
# If condition for getting results and to perform add,multiply and division
if cal == 'add':
    result = int(num1) + int(num2)
    print("operation:", cal, num1, "and", num2, "output:", result)
elif cal == 'mul':
    result = int(num1) * int(num2)
    print("operation:", cal, num1, "and", num2, "output:", result)
elif cal == 'div':
    result = int(num1) / int(num2)
    print("operation:", cal, num1, "and", num2, "output:", result)
else:
    print("Provide correct operator:'add' or 'mul' or 'div'")