
import string
alphabets = string.ascii_lowercase
def print_rangoli(user_number):
    # user_number = int(input())
    lis = []

    for i in range(user_number):
        s = '-'.join(alphabets[i:user_number])
    #     print(s)
        lis.append(s[::-1]+s[1:])
    #     print(lis)

    width = len(lis[0])

    for i in range(user_number-1,0,-1):
        print(lis[i].center(width,'-'))

    for i in range(user_number):
        print(lis[i].center(width,'-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
