# Bloxflip.py
An API Wrapper for bloxflip

# Usage
There are 5 main bloxflip attributes
 - Authorization
 - Crash
 - Currency
 - Mines
 - Towers
 Each with their own example showing how to use them in the examples folder

# Examples

Simple Crash joiner:
```py
from bloxflip import Currency, Crash
import time

auth = ""
betamount = 1
multiplier = 2

Connection = Crash.Websocket.Connect(auth)

for game in Crash.Crashpoints(amount=35, interval=0.01):

	time.sleep(1.5)
	balance = round(Currency.Balance(auth), 2)
	print(f"Balance: {balance}")
	print(f"Games: {game}")
	Crash.Websocket.Join(betamount, multiplier)
```
For more detailed examples check the examples folder
