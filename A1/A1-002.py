def exchange_money(amount):
    coins = [10, 5, 2, 1]
    coin_counts = {}
    for coin in coins:
        coin_counts[coin] = amount // coin
        amount %= coin
    return coin_counts

amount = int(input(""))

coin_counts = exchange_money(amount)

for coin, count in coin_counts.items():
    print(f"{coin} = {count}")