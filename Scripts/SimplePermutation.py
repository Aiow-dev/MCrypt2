def SimplePermutation(message, row, column):  # Шифруемая фраза "Прилетаю седьмого в полдень"
    message = message.replace(' ', '').upper()  # Строки - 4, Столбцы - 6 Результат - "ПЕСМВДРТЕОПЕИАДГОНЛЬЮОЛЬ"
    if (len(message) != row * column):
        return "Ошибка заполнения таблицы. Проверьте количество строк и столбцов"

    mas = [[] for _ in range(row)]

    index = -1

    for j in range(column):
        for i in range(row):
            index += 1
            mas[i].insert(j, message[index])

    shifr = ""

    for i in range(row):
        for j in range(column):
            shifr += mas[i][j]

    return shifr

print(SimplePermutation("Прилетаю седьмого в полдень", 4, 6))