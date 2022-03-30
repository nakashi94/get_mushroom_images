import os
from time import sleep

mushrooms = ["aa", "bb"]
pwd = os.getcwd()

for dir in mushrooms:
    os.makedirs(f"{pwd}\\{dir}", exist_ok=True)

print(3)
sleep(1)
print(2)
sleep(1)
print(1)
sleep(1)
print(0)
