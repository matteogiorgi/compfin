#! /usr/bin/env python3

iter_par = 0
mach_prec = 1
max_it = 1000

while (1 + mach_prec > 1) and (iter_par <= max_it):
    mach_prec = mach_prec / 2
    iter_par = iter_par + 1

mach_prec = mach_prec * 2
print("Machine precision:", mach_prec)
