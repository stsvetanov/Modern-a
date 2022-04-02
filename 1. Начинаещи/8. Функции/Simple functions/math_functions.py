import math

print(math)

signal_power = 20
noise_power = 5
ratio = signal_power / noise_power
decibels = 10 * math.log10(ratio)
print(decibels)
