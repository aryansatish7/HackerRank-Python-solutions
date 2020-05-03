if __name__ == '__main__':
    result = []
    for i in range(int(input())):
        data = input().split(" ")
        command = data[0]
        if command == 'insert':
            result.insert(int(data[1]), int(data[2]))
        if command =='append':
            result.append(int(data[1]))
        if command =='sort':
            result = sorted(result)
        if command == 'pop':
            result.pop()
        if command == 'reverse':
            result = result[::-1]
        if command =='remove':
            result.remove(int(data[1]))
        if command =='print':
            print(result)
