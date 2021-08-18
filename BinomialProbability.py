import math
import sys

arguments = sys.argv
argLength = len(sys.argv)
k = int(sys.argv[1]) if argLength >= 2 else 1  # number of outcome
n = int(sys.argv[2]) if argLength >= 3 else 1  # total number of trial
p = float(sys.argv[3]) if argLength >= 4 else 0  # probability of event

# print('Number of arguments:', len(sys.argv), 'arguments.')
# print('Argument List:', str(sys.argv))

class BinomialProbability:

    def Calculate(self, k: int, n: int, p: float):
        binomial_coefficient = math.comb(n, k)
        #print('binomial_coefficient', binomial_coefficient)

        P = math.pow(p, k)
        NP = math.pow(1 - p, n - k)

        return binomial_coefficient * P * NP

Binomial = BinomialProbability()
print('BinomialProbability:', (Binomial.Calculate(k=k, n=n, p=p)))
