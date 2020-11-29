# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

letter1, letter2 = input('Ведите две строчные латинские буквы через пробел: ').split()
position1 = ord(letter1) - ord('a') + 1
position2 = ord(letter2) - ord('a') + 1
diff_position = abs(position1 - position2) - 1
print(f'Буква {letter1} занимает {position1} позицию\n'
      f'Буква {letter2} занимает {position2} позицию\n'
      f'Между {letter1} и {letter2} {diff_position} букв')