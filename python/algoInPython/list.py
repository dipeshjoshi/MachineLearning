#CRUD operations on LIST
#1. create
l = []
l1 = [1,6,4,7,8,7]
l2 = ['name', 'age', 'ph no.','salary','dept']
l3 = ['dipesh', 29, 9743754445, 739890, 'EDABI']
l5 = [1,7,6,4,8]

# Append and Insert
# If you know the index at which you want to insert the use insert. if you dont know index the use apped. Append will insert at the end.
l1.insert(3,2)
l1.append(5)


#2. retrieve
'''
print l1[0]
print l1[1:4]
print l1[1:] #from 1st evrything
print l1[:4] #till 4th everything
print l1[-3] #3rd last
print l1[-4:-1] # from last 4rth to second last


#3. updating list
print l1
l1[2] = 3
print l1


#4. delete list elements ->
# 1. del : if you know the index , 2. remove : if you dont know index or 3. pop : remove and returns last obkect from list.
print l1
del l1[2]
print l1
l1.remove(4)
l2.remove('salary')
l1.pop()
l2.pop()
print l1
print l2



# Basic list operations:

# lenght of list
len(l3)

#concatinaton of 2 lists -> (+ operator)
l4 = l1 + l2
print l4

#Repetition -> (* operator)
l4 = l2*3
print l4

#Membership -> (in oprator)
if 3 in l3:
    print "Yes"
else:
    print "No"

#Iteration
for i in l2:
    print i
'''

# BUILT IN LIST FUNCTIONS :

#Compare 2 lists ????????
print cmp(l5,l5)

#Max
print max(l1)

#Min
print min(l1)

#Append
l1.append(9)
print l1

#Count
print l1.count(7)

#Extend : Same as concating lists
l1.extend(l2)
print l1

#Index : Returns the lowest index in list that obj appears
print l1.index(7)

#Insert :
l1.insert(4, 3)
print l1

#Pop : Removes and Returns last object from list.
print l1.pop()

#Remove :
l1.remove(5)
print l1

#Reverse :
l1.reverse()
print l1

#Sort :
l1.sort()
print l1
