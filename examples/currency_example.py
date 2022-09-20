from bloxflip import Currency, Authorization
import random
import time

auth = ""
if not Authorization.validate(auth):
	print("Inavlid authorization")
	exit()

old = None

while True:
	affiliate = Currency.Affiliate(auth)
	balance = Currency.Balance(auth)
	if not affiliate == old:
		print(f"R$ {affiliate} available to claim.")
		print(f"R$ {balance} Robux in your balance")
		if affiliate >= 100:
			print("Claiming affiliate")
			Currency.ClaimAffiliate(auth, round(affiliate, 2))
			print("Withdrawing robux")
			Currency.Withdraw(auth, round(affiliate, 2))
		else:
			print("Not enough affiliate to claim")
		old = Currency.Affiliate(auth)
