number = int(input("Enter your age or year of birth: "))
if 130 < number < 1940:
    print("unrealistic age or birth year")
elif number > 2022:
    print('you are not yet born')

future_year = int(input("Enter your year o f choice: "))
if number < 130:
    age_in_future = (future_year - 2022) + number
elif 2022 > number > 1940:
    age_in_future = future_year - number

print(f'Your age in year {future_year} will be: {age_in_future}')
