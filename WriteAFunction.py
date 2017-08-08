if __name__ == '__main__':

    year = int(input())

    def is_leap(year):
        leap = False
        # Write your logic here
        if year % 4 == 0 and year % 100 != 0:
            leap = True
        elif year % 4 == 0 and year % 100 == 0:
            if year % 400 == 0:
                leap = True

        return leap

    print(is_leap(year))

