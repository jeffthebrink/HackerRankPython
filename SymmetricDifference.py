if __name__ == '__main__':
    lengthOfSetOne = input()
    setOne = set(input().split())

    lengthOfSetTwo = input()
    setTwo = set(input().split())

    listOne = list(map(int, setOne.difference(setTwo)))
    listTwo = list(map(int, setTwo.difference(setOne)))

    finalList = listOne.__add__(listTwo)
    finalList.sort()

    for element in finalList:
        print(element)
