import matplotlib.pyplot as plt
import numpy as np
from typing import List, Optional
from dataclasses import dataclass, field
from math import sqrt, pi, exp, pow, e

@dataclass
class Numbers(object):
   ls: List[int]
   _mean: Optional[float] = field(default=None)
   _variance: Optional[float] = field(default=None)
   _stddev: Optional[float] = field(default=None)

   @property
   def mean(self):
      if self._mean is None:
         self._mean = sum(self.ls) / len(self.ls)
      return self._mean

   @property
   def variance(self):
      if self._variance is None:
         mean, ls = self.mean, self.ls
         vs = [(v - mean) ** 2 for v in ls]
         self._variance = sum(vs) / len(vs)
      return self._variance

   @property
   def stddev(self):
      if self._stddev is None:
         self._stddev = sqrt(self.variance)
      return self._stddev

   def pdf_bell_curve_at_x(self, x: int):
      # Fetch this dataset's vals.
      mean = self.mean
      sigma = self.stddev

      # Build the equation.
      numdum = 1 / sqrt( 2 * pi * sigma ** 2 )
      exponent = -1 * (((x - mean) ** 2) / (2 * sigma ** 2))
      e_exponent = e ** exponent

      # Bring together result.
      result = numdum * e_exponent

      return result
      

if __name__ == "__main__":
   numbers = Numbers(ls=[1, 2, 3, 3, 5, 5, 5, 6, 7, 8, 4, 4, 2, 3, 4])   
   
   mean = numbers.mean
   dev = numbers.stddev

   pds = []
   xs = []
   step_size = 0.01
   for x in np.arange(mean - 5 * dev, mean + 5 * dev, step_size):
      pd = numbers.pdf_bell_curve_at_x(x)
      pds.append(pd * step_size)
      xs.append(x)
   
   plt.plot(xs, pds)
   plt.show()
   print(sum(pds))