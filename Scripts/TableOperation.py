def ColumnToRow(mas, row, column):

    index = -1
    newMas = [[] for _ in range(row)]

    for j in range(row):
        for i in range(column):
            index += 1
            newMas[j].insert(i, mas[i][j])

    return newMas