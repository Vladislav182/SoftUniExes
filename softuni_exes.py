BEER_PRICE = 1.20
import math
name = input()
budget = float(input())
beer_count = int(input())
chips_count = int(input())

beers_price = BEER_PRICE*beer_count
chips_price = beers_price * 0.45
all_chips_price = math.ceil(chips_price*chips_count)
sum = beers_price + all_chips_price
diff = abs(sum - budget)
if budget >= sum:
    print(f"{name} bought a snack and has{diff: .2f} leva left ")
else:
    print(f"{name} се нуждае от {diff: .2f} още лева")