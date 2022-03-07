from time import sleep

print('\n')
sleep(1)
print("----------------------------------------")
print("----------------------------------------")
print('...............iTok finder..............')
print('----------------------------------------')
print('a script that can help you find the result')
print("of a complix number ('0+1*i') raised to a power k")
print('----------------------------------------')
print('\n')

sleep(2)

k = input('Enter the power (k) : ')

if(k == 0 ):
     print("i to the power of " + str(k) + " is equal to : 0")
elif (k%4 == 0 ):
    print("i to the power of " + str(k) + " is equal to : 1")
elif(k%2 == 0  ):
    print("i to the power of " + str(k) + " is equal to : -1")
else:
    print("i to the power of " + str(k) + " is equal to : -i")
print('\n')
print("--------------------------------------")
print('\n')




