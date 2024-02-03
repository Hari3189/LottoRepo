import pandas
import random

lottomaxnumbers = pandas.read_excel('./LottoMaxHistoricalResults2024.xlsx', 'Results', usecols="B:H").to_dict(orient='split').get('data')

def generateNumber(length=7, max_value=50):
    # It ismn't possible to get a combination like 44 45 46 47 48 49 50, so the first number has to be lesser than 44.
    final_number = []
    min_num = 1
    for i in range(7):
        # print(min_num, 50 - (6 - i))
        num = random.randint(min_num, 50 - (6 - i))
        min_num = num + 1
        final_number.append(num)
    flag = overlapOkay(final_number)
    if flag is False:
        generateNumber()
    return final_number

def overlapOkay(combination):
    flag = True
    for lottomaxnumber in lottomaxnumbers:
        setNumbers = set.intersection(set(combination), set(lottomaxnumber))
        if 7 > len(setNumbers) > 3:
            print(lottomaxnumber, combination, setNumbers)
            flag = False
    # print(lottomaxnumber, combination)
    return flag

# print(generateNumber())
print(overlapOkay([5,13,18,29,37,38,50]))
print(overlapOkay([7,15,21,25,42,45,47]))

print(overlapOkay([1,6,12,18,26,27,40]))
# for lottomaxnumber in lottomaxnumbers:
#     overlapOkay(lottomaxnumber)

# for numbers in lottomaxnumbers:
#     print(numbers)

