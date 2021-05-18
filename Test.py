"""
#factorial part from Grapher
dirty = dirty + "$" #used to prevent the split from being at the absolute end of the string
        dirty = dirty.split("!", 1)
        dirty[0] = dirty[0] + "$"
        dirty[0] = dirty[0][::-1] #reverse order

        for a in range(len(dirty[0])): #check each character of dirty
            if dirty[0][a] in checkOperands: #if the factorial-ed thing is a number or variable without any power
                operand = dirty[0][a]
                dirty[0] = dirty[0].split(operand, 1)
                dirty[0][0] = ")" + dirty[0][0] + "(lairotcaf.htam" #"math.factorial(" backwards
                dirty[0] = dirty[0][0] + operand + dirty[0][1] #un-split and add back in the operand
                break
            elif dirty[0][a] in checkParentheses:
                for e in range(len(dirty[0])):
                    if dirty[0][e] == ")":
                        dirty[0] = dirty[0].replace(")", "}", 1)
                    elif dirty[0][e] == "(":
                        dirty[0] = dirty[0].replace("(", "{", 1)
                    elif(dirty[0].count("{") == dirty[0].count("}") and dirty[0].count("{") != 0):
                        dirty[0] = dirty[0] + "$"
                        dirty[0] = dirty[0][::-1] #unflip
                        print(dirty)
                        dirty[0] = dirty[0].split("{", 1)
                        print(dirty)
                        dirty[0] = dirty[0][0] + "math.factorial{" + dirty[0][1]
                        dirty[0] = dirty[0].replace("{", "(")
                        dirty[0] = dirty[0].replace("}", ")")
                        dirty[0] = dirty[0][::-1] #reflip
                        break
                if(dirty[0].count("{") == dirty[0].count("}") and dirty[0].count("{") != 0):
                    dirty[0] = dirty[0] + "$"
                    dirty[0] = dirty[0][::-1] #unflip
                    print(dirty)
                    dirty[0] = dirty[0].split("{", 1)
                    print(dirty)
                    dirty[0] = dirty[0][0] + "math.factorial{" + dirty[0][1]
                    dirty[0] = dirty[0].replace("{", "(")
                    dirty[0] = dirty[0].replace("}", ")")
                    dirty[0] = dirty[0][::-1] #reflip
                break
            if a == len(dirty[0]) - 1: #if it is at the end character
                dirty[0] = ")" + dirty[0] + "(lairotcaf.htam" #"math.factorial(" backwards
        dirty[0] = str(dirty[0][::-1]) #reverse order (back to right way)
        dirty = dirty[0] + dirty[1]
        dirty = dirty.replace("$", "") #remove the PESKY temporary space
"""






"""
# A utility function to calculate area
# of triangle formed by (x1, y1),
# (x2, y2) and (x3, y3)
 
def area(x1, y1, x2, y2, x3, y3):
 
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)
 
 
# A function to check whether point P(x, y)
# lies inside the triangle formed by
# A(x1, y1), B(x2, y2) and C(x3, y3)
def isInside(x1, y1, x2, y2, x3, y3, x, y):
 
    # Calculate area of triangle ABC
    A = area (x1, y1, x2, y2, x3, y3)
 
    # Calculate area of triangle PBC
    A1 = area (x, y, x2, y2, x3, y3)
     
    # Calculate area of triangle PAC
    A2 = area (x1, y1, x, y, x3, y3)
     
    # Calculate area of triangle PAB
    A3 = area (x1, y1, x2, y2, x, y)
     
    # Check if sum of A1, A2 and A3
    # is same as A
    if(A == A1 + A2 + A3):
        return True
    else:
        return False
 
# Driver program to test above function
# Let us check whether the point P(10, 15)
# lies inside the triangle formed by
# A(0, 0), B(20, 0) and C(10, 30)
if (isInside(0, 0, 20, 0, 10, 30, 10, 15)):
    print('Inside')
else:
    print('Not Inside')
 
# This code is contributed by Danish Raza
"""