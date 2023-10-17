numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
before_none = 4
after_none = 5

sum_of_numbers = sum(numbers[:before_none]) + sum(numbers[after_none:])
number_of_elements = len(numbers)
arithmetic_mean = sum_of_numbers / number_of_elements
numbers[4] = arithmetic_mean

print("Измененный список:", numbers)
