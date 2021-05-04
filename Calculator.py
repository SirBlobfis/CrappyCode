import math

userInput = input()

def pythonConversion():
    global userInput
    userInput = userInput.replace("^", "**")
    userInput = userInput.replace("sqrt", "math.sqrt")
    #trig
    userInput = userInput.replace("sin", "math.sin")
    userInput = userInput.replace("cos", "math.cos")
    userInput = userInput.replace("tan", "math.tan")
    userInput = userInput.replace("asin", "math.asin")
    userInput = userInput.replace("acos", "math.acos")
    userInput = userInput.replace("atan", "math.atan")

    userInput = userInput.replace("[", "(")
    userInput = userInput.replace("]", ")")
    userInput = userInput.replace("{", "(")
    userInput = userInput.replace("}", ")")
    while("|" in userInput):
        userInput = userInput.replace("|", "math.fabs(", 1)
        userInput = userInput.replace("|", ")", 1)
    
    #DEFINITELY INCOMPLETE
    while("!" in userInput):
        userInput = userInput.replace("!", "math.factorial(!", 1)
        userInput = userInput.split("!", 1)
        for i in range(len(userInput[1])):
            if(userInput[1][i] != ("0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or ".")):
                userInput[1] = userInput[1][:(i + 1)] + ")" + userInput[1][(i + 1):]
                break
            else:
                pass
        userInput = userInput[0] + userInput[1]

    print(userInput)
    userInput = userInput.replace("int", "math.floor")

    userInput = userInput.replace("log0", "math.log0")
    userInput = userInput.replace("log1", "math.log1")
    userInput = userInput.replace("log2", "math.log2")
    userInput = userInput.replace("log3", "math.log3")
    userInput = userInput.replace("log4", "math.log4")
    userInput = userInput.replace("log5", "math.log5")
    userInput = userInput.replace("log6", "math.log6")
    userInput = userInput.replace("log7", "math.log7")
    userInput = userInput.replace("log8", "math.log8")
    userInput = userInput.replace("log9", "math.log9")

    userInput = userInput.replace("log(", "math.log10(")
    userInput = userInput.replace("ln(", "math.log(")
    #constants
    userInput = userInput.replace("e", "math.e")
    userInput = userInput.replace("pi", "math.pi")
    userInput = userInput.replace("tau", "math.tau")

def graph():
    global userInput
    graphDisplay = []

    userInput = userInput.replace("graph(", "")
    userInput = userInput.split("):")
    graphRange = str(userInput[0])
    userInput = str(userInput[1])
    userInput = userInput.replace("y=", "")
    userInput = userInput.replace("y = ", "")
    userInput = userInput.replace("y =", "")

    graphRange = graphRange.replace("(", "")
    graphRange = graphRange.replace(")", "")
    graphRange = graphRange.replace(" ", "")
    graphRange = graphRange.split(",")

    limX1 = graphRange[0]
    limX2 = graphRange[1]
    limY1 = graphRange[2]
    limY2 = graphRange[3]

    for Y in range(10):
        graphDisplay.append([])
        for X in range(50):
            graphDisplay[Y].append(0)

    for Y in range(10):
        for X in range(50):
            try:
                if(((int(round(eval(userInput, {"math": math}, {"x": X}), 1))) < 0) or ((int(round(eval(userInput, {"math": math}, {"x": X}), 1))) > 9)):
                    pass
                else:
                    graphDisplay[int(round(eval(userInput, {"math": math}, {"x": X}), 2))][X] = 1
            except ZeroDivisionError:
                pass
    graphDisplay.reverse()
    displayGraph(graphDisplay)

def displayGraph(graphDisplay):
    buffer = ""
    for i in range(10):
        buffer += str(graphDisplay[i])
        buffer += "\n"
    print(buffer)

def simpleSolver():
    print(userInput)
    try:
        print(eval(userInput))
    except SyntaxError:
        print("Syntax Error")
    except NameError:
        print("NameError")

def commands():
    if("g(" in userInput):
        graph()
    else:
        simpleSolver()

def commandConverter():
    global userInput
    userInput = userInput.replace("graph", "g")
    userInput = userInput.replace("deriv", "d")
    userInput = userInput.replace("derive", "d")
    userInput = userInput.replace("derivative", "d")
    userInput = userInput.replace("integral", "i")
    userInput = userInput.replace("integrate", "i")

pythonConversion()
commandConverter()
commands()