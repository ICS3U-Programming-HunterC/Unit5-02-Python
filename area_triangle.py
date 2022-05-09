#!/usr/bin/env python3
# Created by: Hunter Connolly
# Created on: May 6, 2022
# This program calculates the area of a triangle using functions


def calc_area(base, height):
    # calculate area
    area = base * height / 2

    # display the area
    print("The area of your triangle is: {}cm^2".format(area))


def main():
    # get the base and height
    base_as_string = input("Enter the base(cm): ")
    height_as_string = input("Enter the height(cm): ")

    # error check
    try:
        base_as_number = float(base_as_string)
        height_as_number = float(height_as_string)
        # call function
        calc_area(base_as_number, height_as_number)
    except Exception:
        print("Must be a number!")

if __name__ == "__main__":
    main()
