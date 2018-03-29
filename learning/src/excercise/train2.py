s = "A bird in the hand..."

# for 반복문을 추가하세요
for c in s:
    if c in ('a', 'A'):
        print ('X',end='')
    else:
        print (c,end='')
print ('\n')
x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
print (zipped)

print (list(zipped))
x2, y2 = zip(*zip(x, y))
print (type(x2))
x == list(x2) and y == list(y2)
print (x2, y2)