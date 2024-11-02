import random
import time

# healthy heart rate (60 - 100 bpm)

normalHRMin = 60
normalHRMax = 100

stressHRMin = 101
stressHRMax = 200

normalHRs = []
stressHRs = []

count = 5

def randomHRGenerator():

    for i in range (count):
        normalHRs.append(random.randint(normalHRMin, normalHRMax))
        time.sleep(3)

    for i in range (count):
        stressHRs.append(random.randint(stressHRMin, stressHRMax))
        time.sleep(3)

    return normalHRs, stressHRs

print(randomHRGenerator())


