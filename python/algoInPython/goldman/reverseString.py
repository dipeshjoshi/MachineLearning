







inString = "I love programming very much"
l = inString.split(" ")
rl = []
output = ""
for item in l:
    rl.append(item[::-1])

rl.reverse()
for item in rl:
    output = output +' '+item[::-1]
print output
