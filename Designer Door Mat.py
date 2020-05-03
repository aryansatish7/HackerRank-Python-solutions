# Enter your code here. Read input from STDIN. Print output to STDOUT
x,y = map(int,input().split())
middle = '.|.'
greeting = 'WELCOME'
result =[]
for each in range(x//2):
    result.append((middle*(2*each + 1)).center(y,'-'))
print('\n'.join(result+[greeting.center(y,'-')]+ result[::-1]))
