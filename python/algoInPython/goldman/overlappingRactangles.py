




def ifOverlappingRectangles(l1, r1, l2, r2):
    #if rectangle is on left
    if(l1[0] > r2[0] or r1[0] < l2[0]):
        return "false"
    if(l2[1] < r1[1] or l1[1] < r2[1]):
        return "false"
    return "true"


l1 = [0,10]
r1 = [10,0]
l2 = [5,5]
r2 = [15,0]
output = ifOverlappingRectangles(l1, r1, l2, r2)
print output
