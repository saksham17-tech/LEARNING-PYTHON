#COUNTDOWN TIMER
import time
import math

my_time = int(input("Enter time in seconds: "))

for i in range (my_time, 0, -1):
    sec = i%60
    min = int(i/60)%60
    hrs = math.floor(i/3600)
    print(f"{hrs:02}:{min:02}:{sec:02}")
    time.sleep(1)

print("TIME'S UP!!!")