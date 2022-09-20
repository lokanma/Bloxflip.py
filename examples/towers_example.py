from bloxflip import Currency, Towers, Authorization
import random
import time

auth = ""
if not Authorization.validate(auth):
	print("Inavlid authorization")
	exit()
betamount = 5
difficulty = "easy"

while True:
	Towers.Create(betamount, difficulty, auth)
	time.sleep(0.5)

	choice = random.choice(list(range(0, 2)))
	balance = round(Currency.Balance(auth), 2)
	print(f"Balance: {balance}")
	print(f"Choosing tile {choice}")
	if Towers.Choose(choice, auth):
		print("Cashing out")
		Towers.Cashout(auth)
	else:
		print("Mine exploded")
