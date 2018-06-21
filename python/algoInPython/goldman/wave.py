
def sortWave(input_arr):
    flag = 0
    for index in range(len(input_arr)-1):
        if flag == 0 :
            if(input_arr[index] < input_arr[index+1]):
                temp = input_arr[index]
                input_arr[index] = input_arr[index+1]
                input_arr[index+1] = temp
            flag = 1
        elif flag == 1:
            if(input_arr[index] > input_arr[index+1]):
                temp = input_arr[index]
                input_arr[index] = input_arr[index+1]
                input_arr[index+1] = temp
            flag = 0
    print input_arr



input = [3, 6, 5, 10, 7, 20]
sortWave(input)
