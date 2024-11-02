import random

class NormalHRGenerator:
    def __init__(self):
        self.normalHRMin = 60
        self.normalHRMax = 100
        self.normalHRAvg = int((self.normalHRMin + self.normalHRMax) / 2)
    def generate (self, pastVal):

        if (pastVal in {self.normalHRMin, self.normalHRMin, self.normalHRMin - 3}): # if pastVal equals the min, then generate value slightly higher than min but <= avg
            normalHR = random.randint(self.normalHRMin + 3, self.normalHRAvg)
        elif (pastVal == self.normalHRAvg): # if pastVAL equal to the peak, then generate value slightly higher than avg but <= max 
            normalHR = random.randint(self.normalHRAvg + 3, self.normalHRMax)
        elif (pastVal in {self.normalHRMax, self.normalHRMax + 3, self.normalHRMax - 3}): # if pastVal approx. equals the max, then generate value slightly lower than max but <= avg
            normalHR = random.randint(self.normalHRAvg, self.normalHRMax -3)
        elif (self.normalHRMin < pastVal < self.normalHRAvg): # if pastVal bless than peak, then generate value slightly higher than pastVal but <= avg
            if (pastVal + 3 <= self.normalHRAvg):
                normalHR = random.randint(pastVal + 3, self.normalHRAvg)
            else:
                normalHR = random.randint(self.normalHRAvg + 3, self.normalHRMax)
        elif (self.normalHRAvg < pastVal < self.normalHRMax): # if pastVal greater than peak, then generate value slightly higher than pastVal but <= max
            if (pastVal + 3 <= self.normalHRMax):
                normalHR = random.randint(pastVal + 3, self.normalHRMax)
            else:
                normalHR = random.randint(self.normalHRAvg, pastVal)
        else:
            normalHR = random.randint(self.normalHRMin, self.normalHRMax)    
        return normalHR

# Test normal
normalHR = NormalHRGenerator()
pastNormalHR = random.randint(normalHR.normalHRMin, normalHR.normalHRMax)
print("Past normal HR:", pastNormalHR)
print("Next normal HR:", normalHR.generate(pastNormalHR))
