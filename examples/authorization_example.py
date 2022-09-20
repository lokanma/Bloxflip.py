from bloxflip import Currency, Crash, Authorization
import time

cookie = ""
auth = Authorization.Generate(cookie)
if not Authorization.validate(auth):
	print("Inavlid authorization")
	exit()

balance = round(Currency.Balance(auth), 2)
print(f"Balance: {balance}")
