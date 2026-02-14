# Print the countdown before something "exciting" happens(like "Launching...." or "HAppy New Year!").

import time

count=int(input("Enter the counter num: "))

print("\n Countdown Starts Now:")

for i in range(count,0,-1):
    print(i)
    time.sleep(1)

print("\n Happy New Year!") 
