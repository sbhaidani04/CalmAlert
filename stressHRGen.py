import random

class StressHRGenerator:
    def __init__(self):
        self.normalHRMin = 60
        self.stressHRMax = 220
        self.stressHRAvg = int((self.normalHRMin + self.stressHRMax) / 2)
    def generate (self, pastVal):

        if (pastVal in {self.normalHRMin, self.normalHRMin, self.normalHRMin - 3}): # if pastVal equals the min, then generate value slightly higher than min but <= avg
            stressHR = random.randint(self.normalHRMin + 3, self.stressHRAvg)
        elif (pastVal == self.stressHRAvg): # if pastVAL equal to the peak, then generate value slightly higher than avg but <= max 
            stressHR = random.randint(self.stressHRAvg + 3, self.stressHRMax)
        elif (pastVal in {self.stressHRMax, self.stressHRMax + 3, self.stressHRMax - 3}): # if pastVal approx. equals the max, then generate value slightly lower than max but <= avg
            stressHR = random.randint(self.stressHRAvg, self.stressHRMax -3)
        elif (self.normalHRMin < pastVal < self.stressHRAvg): # if pastVal bless than peak, then generate value slightly higher than pastVal but <= avg
            if (pastVal + 3 <= self.stressHRAvg):
                stressHR = random.randint(pastVal + 3, self.stressHRAvg)
            else:
                stressHR = random.randint(self.stressHRAvg + 3, self.stressHRMax)
        elif (self.stressHRAvg < pastVal < self.stressHRMax): # if pastVal greater than peak, then generate value slightly higher than pastVal but <= max
            if (pastVal + 3 <= self.stressHRMax):
                stressHR = random.randint(pastVal + 3, self.stressHRMax)
            else:
                stressHR = random.randint(self.stressHRAvg, pastVal)
        else:
            stressHR = random.randint(self.normalHRMin, self.stressHRMax)    
        return stressHR

# Test stress
stressHR = StressHRGenerator()
pastStressHR = random.randint(stressHR.normalHRMin, stressHR.stressHRMax)
print("Past normal HR:", pastStressHR)
print("Next normal HR:", stressHR.generate(pastStressHR))
