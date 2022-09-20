from bloxflip import Currency, Crash, Authorization
import time

auth = ""
if not Authorization.validate(auth):
	print("Inavlid authorization")
	exit()
betamount = 1
multiplier = 2

Connection = Crash.Websocket.Connect(auth)

for game in Crash.Crashpoints(amount=35, interval=0.01):

	time.sleep(1.5)
	balance = round(Currency.Balance(auth), 2)
	print(f"Balance: {balance}")
	print(f"Games: {game}")
	Crash.Websocket.Join(betamount, multiplier)
