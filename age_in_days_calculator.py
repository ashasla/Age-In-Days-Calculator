print('*** Age In Days Calculator ***')

age_years = int(input('Enter your age in years: '))

age_months = age_years * 12
age_days = age_years * 365
age_hours = age_days * 24

print(f'You have lived {age_months} months.')
print(f'You have lived {age_days} days.')
print(f'You have lived {age_hours} hours.')

