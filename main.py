import random

random_number = random.randint(1, 100) # Generating random number
print('Вітаю, я загадав число від 1 до 100. Спробуй відгадати його за 7 спроб')
attempt = 7 # Attempt quantity

# Verification of input

while attempt > 0 :

    valid = 0 # verification flag

    while valid == 0:

        user_input = input('Введіть ваше припущення: ')
        num_of_user = 0

        try:

            num_of_user = int(user_input) #verification of int input
            valid = 1

            if num_of_user > 100 or num_of_user < 1: #verefication of range
                print("Число повинно бути в межах від 1 до 100")
                valid = 0

        except ValueError:
            print("Invalid input")

# Checking game rules

    if num_of_user < random_number:

        print('Занадто маленьке')
        attempt -= 1
        print('У вас залишилось ', attempt, ' спроб')

    elif num_of_user > random_number:

        print('Занадто велике')
        attempt -= 1
        print('У вас залишилось ', attempt, ' спроб')

    else:

        print('Вітаємо! Число відгадане')
        exit()

else:
    print('Ви вичерпали усі спроби :(')

print('Правильна відповідь: ', random_number)


