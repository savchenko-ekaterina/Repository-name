numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
left_numbers = numbers[0:4]
right_numbers = numbers[5:]
sum_numbers = sum(left_numbers + right_numbers)
count_numbers = len(numbers)
average_numbers = sum_numbers / count_numbers
numbers[4] = average_numbers
print("Измененный список:", numbers)
