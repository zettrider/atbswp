tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(wordList):
    lenList = [[], [], []]
    colWidth = []
    for outer in range(len(wordList)):
        for inner in range(len(wordList[outer])):
            lenList[outer].append(len(wordList[outer][inner]))
        colWidth.append(max(lenList[outer]))
    for i in range(len(wordList[0])):
        print(wordList[0][i].rjust(8) + wordList[1][i].rjust(6) +
              wordList[2][i].rjust(6))

printTable(tableData)
