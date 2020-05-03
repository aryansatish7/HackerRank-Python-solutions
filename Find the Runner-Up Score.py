if __name__ =='__main__':
    n = int(input())
    nums = input().split()
    runnerup =sorted(list(set(map(int,nums))))
    print(runnerup[-2])

    """n = int(input())
    print (sorted(list(set(map(int,input().split()))))[-2])"""
# one line solution
