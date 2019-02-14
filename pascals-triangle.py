rowstotal = int(input('rows? '))
a = [1,1]

def nextrow(l):
    """Generate nextrow in pascal's tri"""

    b = []

    for i in range(len(l) - 1):
        sum = l[i] + l[i+1]
        b.append(sum)

    l = [1] + b + [1]

    return l

def chartotal(l):
    """Find the numbertotal of char in a [1, '', 1] type printrow"""

    char = 0
    for i in l:

        if i == '':
            char += 2

        if type(i) == int:
            char += len(str(i))

        char += 2

    return char - 2 #comma , space  sequence exists for all except last term

def printrow(l, spacetotal, modify = False):
    """Format the list with '' and add space before print"""

    n = []

    for i, x in enumerate(l):
        n.append(x)
        if i != len(l) - 1:
            n.append('')

    l = n

    spacepartial = chartotal(l) #number of characters in row
    space = (spacetotal / 2) - (spacepartial / 2) #spacetotal depends on the number of row required

    if modify == True:
        return l

    else:
        print ' ' * space,
        print l

#1) find # of char
for i in range(rowstotal - 1):
    a = nextrow(a)

spacetotal = chartotal(printrow(a, 1, True)) #spacing is irrelevant, 1 is a placeholder
print spacetotal

#2) setup
printrow([1], spacetotal); printrow([1, 1], spacetotal)

#3) default printrow with space
a = [1,1]
for i in range(rowstotal - 1):
    a = nextrow(a)
    printrow(a, spacetotal)
