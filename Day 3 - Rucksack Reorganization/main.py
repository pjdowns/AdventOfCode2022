# Advent Of Code 2022
# Day 3 - Rucksack Reorganization
#
# PJD

priority = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
            "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
            "u", "v", "w", "x", "y", "z"]

if __name__ == '__main__':
    data_input = []
    with open("day3_input.txt") as f:
        data_input = f.readlines()

    priority_total = 0
    common_item = ""

    for data in data_input:
        rucksack = data
        rucksack_end = len(rucksack) - 1
        rucksack_mid = int(rucksack_end / 2)

        compartments = [rucksack[0:rucksack_mid], rucksack[rucksack_mid:rucksack_end]]

        for item in compartments[0]:
            if compartments[1].find(item) > 0:
                common_item = item
                break;

        if common_item.isupper():
            priority_total = priority_total + (priority.index(common_item.lower()) + 1)+26
        else:
            priority_total = priority_total + (priority.index(common_item)+1)

    print("Priority Total: {0}".format(priority_total))


