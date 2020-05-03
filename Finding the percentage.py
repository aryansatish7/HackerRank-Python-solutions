if __name__ == '__main__':
    marks = {}
    n = int(input())
    for _ in range(n):
        scores = input().split()
        marks[scores[0]] = list(map(float,scores[1:]))
    print('%.2f'%(sum(marks[input()])/3))
