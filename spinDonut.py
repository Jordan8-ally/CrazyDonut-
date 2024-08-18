import time

with open("spinningDonut.txt", "r") as f:
    frames = f.read().split("-"*50)
    
for frame in frames:
    print("\033[H\033[J", end="")
    print(frame)
    time.sleep(0.1)