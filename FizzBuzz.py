


def printArray():
    for i in range(1,100):
            arr= []
            if i%3 ==0 and i%5==0:
                print("FizzBuzz")

            elif  i%3 ==0:
                print("fizz")

            elif i%5 ==0:
                print("Buzz")

            else :
                print(i)

def toArray():
    arr = []
    for i in range(1,100):

            if i%3 ==0 and i%5==0:

                arr.append('FizzBuzz')
            elif  i%3 ==0:

                arr.append('Fizz')
            elif i%5 ==0:

                arr.append('Buzz')
            else :
                arr.append(i)
    print(arr)

userInput = str(input("Please Enter Your choice P To print the the Puzzle A For the make buzzle to array: "))
if userInput == 'P':
    print(printArray())
elif userInput == 'A':
    print(toArray())
