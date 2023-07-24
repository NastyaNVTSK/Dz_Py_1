
import random
def find_minimum(coins):
    reshka = 0
    gerb = 0
    
    for coin in coins:
        if coin == "решка":
            reshka += 1
        elif coin == "герб":
            gerb += 1
    
    return min(reshka, gerb)

n = int(input("Введите количество монеток: "))
tails = 0
eagle = 0
coins = [random.choice(["решка", "герб"]) for _ in range(n)]
print(coins)
min_value = find_minimum(coins)
print(f"Минимальное количество монет, которые нужно перевернуть:" , {min_value})


