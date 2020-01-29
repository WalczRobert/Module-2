def convert_to_months(age_in_years):
    x = int(age_in_years)
    age_in_months = x*12
    print(age_in_months)
    return age_in_months



if __name__ == '__main__':
    print('How old are you?:')
    age_in_years = input('')
    convert_to_months(age_in_years)

