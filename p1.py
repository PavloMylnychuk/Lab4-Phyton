# Завдання 1: Сформувати файл F1
with open("F1.txt", "w") as f1:
    numbers = [10, -15, 6, 3, -30, 8, -9, 25, 18, -12]
    for num in numbers:
        f1.write(str(num) + "\n")

# Завдання 2: Виконати завдання згідно з варіантом
with open("F1.txt", "r") as f1, open("F2.txt", "w") as f2, open("F3.txt", "w") as f3:
    # Завдання 1.1
    for line in f1:
        num = int(line.strip())
        if num % 5 == 0:
            f2.write(str(num) + "\n")
        if num < 0 and num % 3 == 0:
            f3.write(str(num) + "\n")

    # Завдання 2.1
    f1.seek(0)
    first_line = f1.readline()
    print("(а) Перший символ першого рядка:", first_line[0])
    print("(б) П'ятий символ першого рядка:", first_line[4])
    print("(в) Перші 10 символів першого рядка:", first_line[:10])

    # Завдання 2.2
    s1, s2 = 2, 5
    print("(г) Символи з s1-го по s2-й в першому рядку:", first_line[s1-1:s2])

    # Завдання 2.3
    second_line = f1.readline()
    print("(д) Перший символ другого рядка:", second_line[0])

    # Завдання 2.4
    n, k = 2, 3
    f1.seek(0)
    for i in range(n):
        line = f1.readline()
    print("(е) k-й символ n-го рядка:", line[k-1])
