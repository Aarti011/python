# Loading...
import time

for i in range(10):
    print("Loading" + "." * i, end="\n")
    time.sleep(0.5)

print("Done!")


# typing effect- prints one letter at a time like typnig
import time
text="This is not the planet for Aliens"
for i in text:
  print(i, end="", flush=True)
  time.sleep(0.2)

text="There could be more that five gollibles in this game"
for i in text:
  print(i, end="", flush =True)
  time.sleep(0.2)


# Bouncing effect
import time
for i in range(20):
    print(" " * i + "⚫", end="\r")
    time.sleep(0.1)

for i in range(20, 0, -1):
    print(" " * i + "⚫", end="\r")
    time.sleep(0.1)


# Matrix rain style
import random
import time
chars="0123456789"

for i in range(50):
    line=""
    for j in range(40):
        line+=random.choice(chars)
    print(line, end="\r")
    time.sleep(0.2)



















