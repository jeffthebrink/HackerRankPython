if __name__ == '__main__':
    numOfCommands = int(input())
    list = []
    for _ in range(numOfCommands):
        s = input().split()
        command = s[0]
        argument = s[1:]
        if command != "print":
            command = command + "(" + ",".join(argument) + ")"
            eval("list." + command)
        else:
            print(list)
