import sys
import random 

LIMIT_TRY = 5

guess_number = random.randint(1, 100)

max_try = 0

print("Угадайте число, загаданное компьютером, в диапазоне от 1 до 100: ")

if len(sys.argv) == 2:
    try:
        max_try = int(sys.argv[1]);
    except ValueError:
        print("Неверное значение")
     
elif len(sys.argv) < 2:
    print("Мало параметров")
    try:
        max_try = int(input("Введите кол-во попыток, за которое вы сможете угадать число\n"));
    except ValueError:
        print("Неверное значение, задано количество попыток по умолчанию")
        max_try = LIMIT_TRY
else:
    print("Слишком много параметров")
    try:
        max_tries = int(input("Введите кол-во попыток, за которое вы сможете угадать число"));
    except ValueError:
        print("Неверное значение, задано количество попыток по умолчанию")
        max_try = LIMIT_TRY

if max_try < 1:
    print("Недопустимое число попыток, задано количество попыток по умолчанию:", LIMIT_TRY)
    max_try = LIMIT_TRY
if max_try > 100:
    print("Слишком большое число попыток, задано количество попыток по умолчанию")
    max_try = LIMIT_TRY

user_number = 0
number_try = 0

while user_number != guess_number:
    
    if number_try == max_try:
        print("Вы проиграли, загаданное число было:" + str(guess_number))
        break
    print("Попытка № ", number_try + 1)
    try:
        user_number = int(input("Угадай число от 1 до 100\n"))
    except ValueError:
        print("Введите число из диапазона от 1 до 100")
        continue
    number_try = number_try + 1
    if (user_number > 100) or (user_number < 1):
        print("Число должно быть в диапазоне от 1 до 100") 
    elif user_number > guess_number:
        print("Число должно быть меньше!")
    elif user_number < guess_number:
        print("Число должно быть больше!")

if number_try-1 < max_try:
    print("Вы угадали число", guess_number, " за", number_try, " попыток")




