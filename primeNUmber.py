number= int(input("Enter the number: "))
for i in range (2, number):
    if number%i ==0:
        flag = 1
        print(f'{number} is not a prime number')
        break
else:
    print(f'{number} is prime number')
    flag = 0
    


    