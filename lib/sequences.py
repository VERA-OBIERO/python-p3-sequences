#!/usr/bin/env python3

def print_fibonacci(length):
    x = []

    if length == 0:
        pass
    elif length == 1:
        x.append(0)
    elif length >= 2:
        x = [0, 1]
        for i in range(2, length):
            x.append(x[i - 1] + x[i - 2])
    
    print(x) 