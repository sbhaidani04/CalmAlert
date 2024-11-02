import random
import time

# healthy heart rate (60 - 100 bpm)
normalHRMin = 60
normalHRMax = 100
normalHRAvg = int((normalHRMin + normalHRMax) / 2) # average of the 2 min and max

stressHRMin = 150
stressHRMax = 220
stressHRAvg = int((normalHRMin + stressHRMax) / 2) # average of the normal min and stress max

# # NORMAL
# simulating normal heart rate by generating a random integer between the theoretical min and max HRs
# parameters: normalHRMin, normalHRMax
def normalHRGenerator(pastVal):
    
    if (pastVal == normalHRMin | pastVal == (normalHRMin + 3) | pastVal == (normalHRMin - 3)): # if pastVal equals the min, then generate value slightly higher than min but <= avg
        normalHR = random.randint(normalHRMin + 3, normalHRAvg)
    elif (pastVal == normalHRAvg): # if pastVAL equal to the peak, then generate value slightly higher than avg but <= max 
        normalHR = random.randint(normalHRAvg + 3, normalHRMax)
    elif (pastVal == normalHRMax | pastVal == (normalHRMax + 3) | pastVal == (normalHRMax - 3)): # if pastVal approx. equals the max, then generate value slightly lower than max but <= avg
        normalHR = random.randint(normalHRAvg, normalHRMax -3)
    elif (normalHRMin < pastVal < normalHRAvg): # if pastVal bless than peak, then generate value slightly higher than pastVal but <= avg
        if (pastVal + 3 <= normalHRAvg):
            normalHR = random.randint(pastVal + 3, normalHRAvg)
        else:
            normalHR = random.randint(normalHRAvg + 3, normalHRMax)
    elif (normalHRAvg < pastVal < normalHRMax): # if pastVal greater than peak, then generate value slightly higher than pastVal but <= max
        if (pastVal + 3 <= normalHRMax):
            normalHR = random.randint(pastVal + 3, normalHRMax)
        else:
            normalHR = random.randint(normalHRAvg, pastVal)
    else:
        normalHR = random.randint(normalHRMin, normalHRMax)    
    return normalHR

# STRESS 
# simulating normal heart rate by generating a random integer between the theoretical min and max HRs
# parameters: normalHRmin, stressHRMax
def stressHRGenerator(pastVal):
    
    if (pastVal == normalHRMin | pastVal == (normalHRMin + 3) | pastVal == (normalHRMin - 3)): # if pastVal equals the min, then generate value slightly higher than min but <= avg
        stressHR = random.randint(normalHRMin + 3, stressHRAvg)
    elif (pastVal == stressHRAvg): # if pastVAL equal to the peak, then generate value slightly higher than avg but <= max 
        stressHR = random.randint(stressHRAvg + 3, stressHRMax)
    elif (pastVal == stressHRMax | pastVal == (stressHRMax + 3) | pastVal == (stressHRMax - 3)): # if pastVal approx. equals the max, then generate value slightly lower than max but <= avg
        stressHR = random.randint(stressHRAvg, stressHRMax -3)
    elif (normalHRMin < pastVal < stressHRAvg): # if pastVal bless than peak, then generate value slightly higher than pastVal but <= avg
        if (pastVal + 3 <= stressHRAvg):
            stressHR = random.randint(pastVal + 3, stressHRAvg)
        else:
            stressHR = random.randint(stressHRAvg + 3, stressHRMax)
    elif (stressHRAvg < pastVal < stressHRMax): # if pastVal greater than peak, then generate value slightly higher than pastVal but <= max
        if (pastVal + 3 <= stressHRMax):
            stressHR = random.randint(pastVal + 3, stressHRMax)
        else:
            stressHR = random.randint(stressHRAvg, pastVal)
    else:
        stressHR = random.randint(normalHRMin, stressHRMax)    
    return stressHR

# NORMAL TESTING       
normalHR = random.randint(normalHRMin, normalHRMax) 
print("Past normal stress:", normalHR) 
print("Next normal stress:", normalHRGenerator(normalHR))

# STRESS TESTING
stressHR = random.randint(normalHRMin, stressHRMax)
print ("Past stressed stress:", stressHR)  
print("Next stressed stress:", stressHRGenerator(stressHR))



