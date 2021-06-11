from os import get_terminal_size
from os.path import exists
import math

def createDefaults(): #creates default file with default defaults
    readFile = open("DefaultsDefaults.py", "r")
    writeFile = open("Defaults.py", "w+")
    for line in readFile: #copy "DefaultsDefaults" to "Defaults"
        writeFile.write(line)
    readFile.close()
    writeFile.close()

if not exists("Defaults.py"): #create Defaults file only if it doesn't already exist
    createDefaults()
import Defaults

"""-----"""

userInput = ""
output = []
lineBuffer = ""

def printHelp():
    helpFile = open("Help.txt", "r")
    for line in helpFile:
        print(line)

def createOutput():
    out = []
    outputSize = str(get_terminal_size())
    outputSize = outputSize.replace("os.terminal_size(columns=", "")
    outputSize = outputSize.replace(",", "")
    outputSize = outputSize.replace("lines=", "")
    outputSize = outputSize.replace(")", "")
    outputSize = outputSize.split()
    outputSize[0] = int(outputSize[0])
    outputSize[1] = int(outputSize[1])

    #Defaults limit max size of rectangle
    if outputSize[0] >= Defaults.maxX and Defaults.maxX != -1: 
        outputSize[0] = Defaults.maxX
    if outputSize[1] >= Defaults.maxY and Defaults.maxY != -1:
        outputSize[1] = Defaults.maxY

    for a in range(int(outputSize[0]) - 1):
        out.append([])
        for e in range(int(outputSize[1]) - 1):
            out[a].append("E")

    out.append([])  #adds new lines
    for i in range(int(outputSize[1]) - 1):
        out[len(out) - 1].append("\n")

    out = list(zip(*out[::-1])) #possibly move to immediately before ultimate output
    return out

def inputAndClean():
    checkOperands = ["+", "-", "*", "/"]
    checkParentheses = ["(", ")"]
    operand = ""

    dirty = input()

    #alternate parentheses can be used, and are replaced
    dirty = dirty.replace("[", "(")
    dirty = dirty.replace("]", ")")
    dirty = dirty.replace("{", "(")
    dirty = dirty.replace("}", ")")
    #some more cleanup
    dirty = dirty.replace(" ", "")
    dirty = dirty.replace("^", "**")
    dirty = dirty.replace("sqrt", "math.sqrt")
    dirty = dirty.replace("ln", "math.log")
    dirty = dirty.replace("log", "math.log10")
    
    #trig
    dirty = dirty.replace("sin", "math.sin")
    dirty = dirty.replace("cos", "math.cos")
    dirty = dirty.replace("tan", "math.tan")
    dirty = dirty.replace("asin", "math.asin")
    dirty = dirty.replace("acos", "math.acos")
    dirty = dirty.replace("atan", "math.atan")
    #absolute value
    dirty = dirty.replace("abs", "math.fabs")
    while "|" in dirty: #gives error for unmatched pipes
        if dirty.count("|") % 2 != 0:
            raise Exception('Unmatched "|"')
        dirty = dirty.replace("|", "math.fabs(", 1)
        dirty = dirty.replace("|", ")", 1)
    
    #factorial
    while "!" in dirty: #replaces "!" with "math.fatorial" (uses correct order of opperations (I think))
        dirty = dirty.split("!", 1)
        closedParentheses = dirty[1].count(")") - dirty[1].count("(")
        dirty[0] = dirty[0][::-1] #flip dirty
        a = -1
        while closedParentheses != 0:
            a += 1
            if dirty[0][a] == ")":
                closedParentheses += 1
                dirty[0] = dirty[0].replace(")", "}", 1)
            elif dirty[0][a] == "(":
                closedParentheses -= 1
                if closedParentheses != 0:
                    dirty[0] = dirty[0].replace("(", "{", 1)
                
        b = dirty[0][a]
        dirty[0] = dirty[0].split(str(b), 1)
        dirty[0] = ")" + dirty[0][0] + "(lairotcaf.htam" + b + dirty[0][1] #math.factorial backwards
        dirty[0] = dirty[0][::-1] #flip back to right
        dirty = dirty[0] + dirty[1]
    dirty = dirty.replace("}", ")")
    dirty = dirty.replace("{", "(")

    cleaned = dirty #not strictly necesary, but I felt like it
    print("end:" + cleaned)
    return cleaned

def derivative(deriv): #takes into account all derivative rules (as far as I know)
    if deriv.count(")") == 0 and deriv.count("(") == 0:
        deriv = deriv.split("+")
        deriv = deriv.split("-")

if __name__ == "__main__":
    output = createOutput()
    lineBuffer = ""

    userInput = inputAndClean()

    if(userInput == "help"):
        printHelp()
        quit()

    for a in range(len(output)):
        for e in range(len(output[0])):
            lineBuffer += output[a][e]
    print(lineBuffer)