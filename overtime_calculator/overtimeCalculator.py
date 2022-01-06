hours_worked = input("Enter Hours:")
rate = input("Enter Rate:")


if float(hours_worked) <= 40:
    pay = float(hours_worked) * float(rate)
else:
    pay = ((float(hours_worked) - 40) * float(rate) * 1.5) + float(rate) * 40

print(pay)

get_me_out = input('Do you want to continue? [y/n]')
while get_me_out == 'n':
    print('too bad')
    hours_worked = input("Enter Hours:")
    rate = input("Enter Rate:")

    if float(hours_worked) <= 40:
        pay = float(hours_worked) * float(rate)
    else:
        pay = ((float(hours_worked) - 40) * float(rate) * 1.5) + float(rate) * 40

    print(pay)
    get_me_out = input('Do you want to continue? [y/n]')
else:
    print('too bad')
    exit()



