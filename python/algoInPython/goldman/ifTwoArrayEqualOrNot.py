

dict = {}
dict1 = {}

def ifArrayEqual(array1, array2):
    for item in array1:
        if item not in dict.keys():
            dict[item] = 1
        else:
            dict[item] += 1
    for item in array2:
        if item not in dict1.keys():
            dict1[item] = 1
        else:
            dict1[item] += 1

    if len(array1) > len(array2):
        max_array = array1
    else:
        max_array = array2


    for item in max_array:
        if item in dict.keys() and item in dict1.keys():
            if dict[item] != dict1[item]:
                return "No"
        else:
            return "No"
    return "Yes"


a = [2, 1, 4, 5, 0, 1, 2]
b = [1, 2, 5, 4, 0, 2, 2]

output = ifArrayEqual(a,b)
print output
