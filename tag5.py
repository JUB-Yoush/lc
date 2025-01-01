import random

coin = [0,1,1,1,1,1]
output = ""
def pick():
    choice = random.choice(coin)
    return str(choice)

for i in range(1000):
    output += pick()
print(output)
