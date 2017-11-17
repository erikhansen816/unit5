#Erik Hansen
#11/16/17
#stat.py - min,max,median,mode of inputted numbers

num = ''
l = []
while num != 'q':
    num = (input('Enter a number or q to stop: '))
    l.append(num)


del l[len(l)-1]

l1 = []
for n in l:
    l1.append(int(n))

middle = len(l1)
l1.sort()
if middle%2 == 0:
    print('Median:',(l1[middle/2-1] + l1[middle/2])/2)
else:
    print('Median:',l1[middle//2])

h = 0
j = 0
for n in l1:
    while j < len(l1):
        count = l1.count(l1[j])
        if count > h:
            h = count
            mode = l1[j]
        if h == 1 and len(l1) > 1:
            mode = "None"
        j += 1

print('Min:',min(l1))
print('Max:',max(l1))
print('Mean:',sum(l1)/len(l1))
print('Mode:',mode)
