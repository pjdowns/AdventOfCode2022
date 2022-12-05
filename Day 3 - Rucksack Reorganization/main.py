# Advent Of Code 2022
# Day 3 - Rucksack Reorganization
#
# PJD


if __name__ == '__main__':
    data_input = []
    with open("day3_input.txt") as f:
        data_input = f.readlines()

    for data in data_input:
        rucksack = data
        compartments = [rucksack[0:(len(rucksack) / 2)], rucksack[(len(rucksack) / 2):len(rucksack)]]
        