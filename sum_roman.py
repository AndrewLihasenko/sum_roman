def sum_roman(first_num, second_num):
    roman_nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result_first_num, result_second_num = 0, 0

    for i, n in enumerate(first_num):
        if (i+1) == len(first_num) or roman_nums[n] >= roman_nums[first_num[i+1]]:
            result_first_num += roman_nums[n]
        else:
            result_first_num -= roman_nums[n]

    for i, n in enumerate(second_num):
        if (i+1) == len(second_num) or roman_nums[n] >= roman_nums[second_num[i+1]]:
            result_second_num += roman_nums[n]
        else:
            result_second_num -= roman_nums[n]

    sum_result = int(result_first_num) + int(result_second_num)

    units =     ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    tens =      ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hundreds =  ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    thousands = ["", "M", "MM", "MMM"]

    th = thousands[sum_result // 1000]
    h = hundreds[sum_result // 100 % 10]
    t = tens[sum_result // 10 % 10]
    u = units[sum_result % 10]

    result = th + h + t + u

    return result

if __name__ == '__main__':
    print("Введите 2 римских числа для сложения")
    response_one = input("Введите первое число: ")
    response_two = input("Введите второе число: ")
    sum = sum_roman(response_one, response_two)
    print("Сумма чисел ", response_one, " + ", response_two, "= ", sum)

