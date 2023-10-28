n=int(input('enter a nr : '))
counter=0
for i in range (1,n):
    if i%2!=0:
        counter+=i
print('the sum from 1 to ',n,'is : ',counter)