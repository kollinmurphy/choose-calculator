from math import factorial


def choose(total, choose):
    try:
        return int(factorial(total) / (factorial(choose) * factorial(total - choose)))
    except:
        return 0


def main():
    total_start = int(input("Total start: "))
    total_end = int(input("Total end: "))

    choose_start = int(input("Choose start: "))
    choose_end = int(input("Choose end: "))

    print("\n\t| ", end="")
    for j in range(choose_start, choose_end + 1):
        print(f"{j}\t| ", end="")
    print()

    for i in range(total_start, total_end + 1):
        print(f"{i}\t| ", end="")
        for j in range(choose_start, choose_end + 1):
            print(f"{choose(j, i)}\t| ", end="")
        print()


def printTable(table):
    colSize = 1
    for i in table:
        for j in table:
            if len(str(j)) > colSize:
                colSize = len(str(j))

    aboveHeader = "\u250f" + ("\u2501" * ((colSize + 3) * self.__size - 1)) + "\u2513"
    belowHeader = "\u2521" + (("\u2501" * (colSize + 2) + "\u252f") * self.__size)[:-1] + "\u2529"
    separator = "\u251c" + (("\u2500" * (colSize + 2) + "\u253c") * self.__size)[:-1] + "\u2524"
    lastLine = "\u2514" + (("\u2500" * (colSize + 2) + "\u2534") * self.__size)[:-1] + "\u2518"

    print(aboveHeader)
    label = f"Card #{self.__id + 1}"
    labelFormat = "{0:^" + str((colSize + 3) * self.__size - 2) + "} \u2503"
    print("\u2503" + labelFormat.format(label))
    print(belowHeader)
    for row in self.__nums:
        print("\u2502", end="")
        for num in row:
            print((" {0:^" + str(colSize) + "} \u2502").format(num), end="")
        if not row == self.__nums[-1]:
            print("\n" + separator)
    print("\n" + lastLine)


main()
