
dict = {}

def firstNonreapetingchar(inString):
    for index in range(len(inString)):
        if inString[index] not in dict.keys():
            dict[inString[index]] = 1
        else:
            dict[inString[index]] += 1

    for index in range(len(inString)):
        if(dict[inString[index]] == 1):
            print inString[index]
            break


s = "geeksforgeeks"
firstNonreapetingchar(s)
