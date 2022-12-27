firstNumber, secondNumber = input("Write 2 numbers with which you want to perform actions: ").split()

firstNumber = int(firstNumber)
secondNumber = int(secondNumber)

selectedAction = input("Write the action you want to do(*,/,+,-): ")

if(selectedAction == "*"):
    print(firstNumber * secondNumber)
if(selectedAction == "/"):
    print(firstNumber / secondNumber)
if(selectedAction == "+"):
    print(firstNumber + secondNumber)
if(selectedAction == "-"):
    print(firstNumber - secondNumber)