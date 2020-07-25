# implementing the function of a simple calculator 
# using basic mathematical operations

def calc(numFirst, numSecond, operation):

    if operation == '+':
        return(str(numFirst) + ' ' + operation + ' ' + str(numSecond) + ' = ' + str(numFirst + numSecond))
    if operation == '-':
        return(str(numFirst) + ' ' + operation + ' ' + str(numSecond) + ' = ' + str(numFirst - numSecond))
    if operation == '*':
        return(str(numFirst) + ' ' + operation + ' ' + str(numSecond) + ' = ' + str(numFirst * numSecond))
    if operation == '/':
        return(str(numFirst) + ' ' + operation + ' ' + str(numSecond) + ' = ' + str(numFirst / numSecond))


def main():  # Wrapper function

    numFirst = int(input('Please type the first number: '))
    numSecond = int(input('Please type the second number: '))
    operation = input('What kind of operation would you like to do?Choose between "+, -, *, /" : ')

    if operation not in '+-*/':
        operation = input('Please only type one of these characters: "+, -, *, /"!  : ')


    print(calc(numFirst, numSecond, operation))

if __name__ == '__main__':
    main()