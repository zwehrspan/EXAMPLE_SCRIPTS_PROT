import pandas as pd
import numpy as np
from scipy.optimize import curve_fit

# Define exponential decay equation
def decay_eq(inX, tau, a):
    y = a*np.exp(-tau*inX)
    return y

# Calculate the Tau parameter for diffusion
def calc_tau(val, mytime):
  popt, pcov = curve_fit(decay_eq, mytime, val, p0=[0.001, 1])
  out_tau = 1/2/(1/popt[0])
  return(out_tau)

# Read in translational values
iData = pd.read_csv("../DATA/translational_diff_coeff_molnum.txt", delim_whitespace=True, header=None)
dTransCalc = float(iData.iloc[4,2])

# Read in rotational values, calculate Tau, and average over x y z
iDatax = pd.read_csv("../DATA/x_rotational_diff_coeff_moltyp.txt", delim_whitespace=True, header=None)
val = iDatax.iloc[:7,2]
mytime = iDatax.iloc[:7,1]
out_tau_x = calc_tau(val, mytime)

iDatay = pd.read_csv("../DATA/y_rotational_diff_coeff_moltyp.txt", delim_whitespace=True, header=None)
val = iDatay.iloc[:7,2]
mytime = iDatay.iloc[:7,1]
out_tau_y = calc_tau(val, mytime)

iDataz = pd.read_csv("../DATA/z_rotational_diff_coeff_moltyp.txt", delim_whitespace=True, header=None)
val = iDataz.iloc[:7,2]
mytime = iDataz.iloc[:7,1]
out_tau_z = calc_tau(val, mytime)

dRotCalc = (out_tau_x + out_tau_y + out_tau_z) / 3
