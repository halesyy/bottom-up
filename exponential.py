import numpy as np
import math
import matplotlib.pyplot as plt
from typing import List, Tuple


def pdf_exponential(l: float, x: float) -> float:
   # The negative (`-` to `-l` component) is responsible
   # for it being a decaying curve.
   # E^(-l * x) is the decaying component.
   # l is the rate of decay.
   return l * (math.e ** (-l * x))

# This represents something I have measured elsewhere,
# which is the independent rate of sale events in pharmacy.
# It is approx 1 every 370 seconds.
LAMBDA = 1 / 370 

def make_exponential_dist(l: float) -> Tuple[List[float], List[float]]:
   x = np.arange(0, 1000, 0.1)
   y = [pdf_exponential(l, x) for x in x]
   return x, y

def integrate_pdf(l: float, from_x: float, upto_x: float, step: float):
   """Manually integrates for the area"""
   probs = []
   for x in np.arange(from_x, upto_x, step):
      prob = step * pdf_exponential(l, x)
      probs.append(prob)
   return sum(probs)

print(integrate_pdf(l=LAMBDA, from_x=0, upto_x=370, step=0.0001))
plt.plot(*make_exponential_dist(LAMBDA))
plt.show()