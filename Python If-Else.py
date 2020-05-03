
user = int(input().strip())#taking input from the user
if user%2==0:
    if 2<user<5:
        print('Not Weird')
    elif 5<user<21:
        print('Weird')
    else:
        print('Not Weird')
else:
    print('Weird')
