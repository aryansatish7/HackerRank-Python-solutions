if __name__ == '__main__':
    each = input()
    print(any(i.isalnum() for i in each))
    print(any(i.isalpha() for i in each))
    print(any(i.isdigit() for i in each))
    print(any(i.islower() for i in each))
    print(any(i.isupper() for i in each))
