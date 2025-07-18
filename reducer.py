#!/usr/bin/env python

import sys

# The input will be in the form of key-value pairs
# It is sorted according to the key
# Each key value pair will be in a new line
# The key and the value are seperated by a tab (\t)
# The key is the payment type and the value is the sales

# Example input data (Key=Payment, Value=Sales)
# Input is ordered by the key
# Visa  205.96
# Cash  11.32
# Cash  444.19

# We want to sum all values with the same key
# Example output data (Key=Payment, Value=Sum of Sales)
# Visa  205.96
# Cash  455.51

# Sum of all sales (values) is initialized with zero, we just started
sum_sales = 0
count = 0

# Previous key is initialized with None, we just started
previous_key = None

# For each new line in the standard input   
for line in sys.stdin:
    key, value = line.strip().split("\t")

    # Do we have a previous_key (previous_key != None) and 
    # is the new key different than the previous key?
    # This means the line starts with a new key (key changes e.g. from "Visa" to "Cash")
    # Remember that our keys are sorted
    if previous_key != None and previous_key != key:
        # Then write the result of the old key (Key=category, Value= Sum of Sales)
        # to the standart output (stdout)
        # Key and value are seperated by a tab (\t)
        # Line ends with new line (\n)
        # Sum of sales starts again with 0
        average = sum_sales / count if count > 0 else 0
        sys.stdout.write(f"{previous_key}\t{average:.2f}\n")
        sum_sales = 0
        count = 0

        sum_sales += float(value)
        count += 1
        previous_key = key

# write the last result to stdout
if previous_key:
    average = sum_sales / count if count > 0 else 0
    sys.stdout.write(f"{previous_key}\t{average:.2f}\n")