def hidden_numbers(sum, product):
 for X in range(1, sum // 2 + 1):
        Y = sum - X
        if X * Y == product:
            return X, Y
S = int(input("Введите сумму чисел: "))
P = int(input("Введите произведение чисел: "))
result = hidden_numbers(S, P)
print(f"Задуманные числа Петей:", {result})