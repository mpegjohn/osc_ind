import math
from engineering_notation import EngNumber

print("========================================")
print("Oscilloscope Inductance measurement")
frequency = input("Enter frequency (Hz): ")

time_or_angle = input("Phase difference in time T/t or angle [A/a]")

angle = True
if time_or_angle == "t" or time_or_angle == "T":
    angle = False

if angle:
    phase = input("Enter phase (deg): ")
else:
    time_diff = input("Enter time difference (s): ")
    cyc_time = 1/frequency
    degs_per_ct = 360.0/cyc_time
    phase = time_diff * degs_per_ct

print("Phase angle %s Degrees" % phase)

Rref = input("Enter series resistor (Ohms): ")

va1 = input("Enter amplitude Va1 (V): ")
va2 = input("Enter amplitude Va2 (V): ")

Z=va2*Rref/(math.sqrt((va1**2)- 2 * va1 * va2 * math.cos(math.radians(phase)) + (va2**2)))

print("Impedance Z = %sOhms" % EngNumber(Z))

alpha = phase - math.degrees(math.atan( -1 * va2 * math.sin(math.radians(phase))/(va1 - (va2 * math.cos(math.radians(phase))))))

print("Alpha = %s" % alpha)

Resr = Z * math.cos(math.radians(alpha))

print("Resr = %sOhms " % EngNumber(Resr))

L = Z * math.sin(math.radians(alpha))/(2 * math.pi * frequency)

print("Inductance L = %sH" % EngNumber(L))
