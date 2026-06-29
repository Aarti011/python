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

