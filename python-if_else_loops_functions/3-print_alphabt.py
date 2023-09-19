#!/usr/bin/python3
for char in range(ord('a'), ord('z') + 1):
    if char == 'e' or char == 'q' :
        continue
    print(chr(char), end='')