# Copyright (c) 2022 Evgeny Vovk All rights reserved.
#
# Created by: Evgeny Vovk
# Created on: November 2022
# ICS3U-Unit4-03.py File,
# learning for... statement in python.

import math


def main():

    # input and variables
    input_number = input("Input a positive number: ")

    # process and output
    print("")
    try:
        input_number_asint = int(input_number)
        if input_number_asint < 0:
            print("This is not a positive number.")
        else:
            for counter in range(input_number_asint + 1):
                print("{0}² = {1:,.0f}".format(counter, math.pow(counter, 2)))
    except ValueError:
        print("Invalid input, Please try again following the requirements.")

    print("\n\nDone.")


if __name__ == "__main__":
    main()
