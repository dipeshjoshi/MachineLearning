
buy = []
sell = []



def stockBuySell(l):

    if len(l) > 1:
        index = 0
        count = 0
        while index < len(l)-1:

            while index < len(l)-1 and l[index] >= l[index+1]:
                index += 1

            print index
            if index == len(l)-1:
                break

            buy.append(index)

            index =+ 1

            while index < len(l)-1 and l[index] <= l[index + 1]:
                index += 1

            sell.append(index)
            index += 1

            count += 1

        if count == 0:
            print "No buy"
        else:
            for index in range(count):
                print buy[index], sell[index]





l = [100, 180, 260, 310, 40, 535, 695]
stockBuySell(l)
