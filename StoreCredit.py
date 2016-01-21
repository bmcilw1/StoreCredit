#!/usr/bin python

from __future__ import print_function
import sys

def main():
    filename = sys.argv[1]
    f = open(filename, 'rU')
    out = open("out.txt", 'w')
    cases = int(f.readline())

    for case in range(1, cases + 1):
        credit = int(f.readline())
        numItems = int(f.readline())
        itemsList = map(int, f.readline().split())

        itemsDict = {}
        for i in range(1, numItems + 1):
            itemsDict.update({itemsList[i - 1]:i})

        for i in range(numItems):
            key = credit - itemsList[i]
            if key in itemsDict and itemsDict[key] != i + 1:
                print("Case #" + str(case) + ": " + str(i + 1) + " " + str(itemsDict[key]), file=out)
                break

    out.close()
    f.close()

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
