from bloxflip import Currency, Mines, Authorization
import random
import time

auth = ""
if not Authorization.validate(auth):
	print("Inavlid authorization")
	exit()
betamount = 5
mines = 5

while True:
	Mines.Create(betamount, mines, auth)
	time.sleep(0.5)

	choice = random.choice(list(range(0, 24)))
	balance = round(Currency.Balance(auth), 2)
	print(f"Balance: {balance}")
	print(f"Choosing {choice}")
	if Mines.Choose(choice, auth):
		print("Cashing out")
		Mines.Cashout(auth)
	else:
		print("Mine exploded")
