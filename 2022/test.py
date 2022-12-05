"""
This actually works and is written by openAI, pretty cool
"""

# import the necessary libraries
import os
import sys

# define the main function
def main():
    file = open("inputs/dag3.txt", "r")
    lines = file.readlines()
    file.close()
    priorities = []

    # loop through the lines
    for line in lines:
        items = []
        for char in line:
            if char != "\n":
                items.append(char)
                
        first_compartment = []
        second_compartment = []

        # loop through the items
        for i in range(len(items)):
            if i < len(items) / 2:
                first_compartment.append(items[i])
            # if the index is greater than or equal to half the length of the items list
            else:
                second_compartment.append(items[i])

        # create a list to store the common items
        common_items = []
        for item in first_compartment:
            if item in second_compartment:
                common_items.append(item)
        common_priorities = []

        for item in common_items:
            if item.islower():
                common_priorities.append(ord(item) - 96)
            # if the item is uppercase
            elif item.isupper():
                common_priorities.append(ord(item) - 38)
        priorities.append(sum(common_priorities))

    print(sum(priorities))

# run the main function
if __name__ == "__main__":
    main()