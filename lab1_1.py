budget_ticket = 500
economy_ticket = 750
vip_ticket = 2000
bag = 200
meal = 150
num_bag = 0
num_meal = 0

print('Ticket types:')
print('1. Budget  ( 500kr)')
print('2. Economy ( 700kr)')
print('3. VIP     (2000kr)')

choice = int(input('\nPlease choose a Ticket Type: '))

while not (choice == 1 or choice == 2 or choice == 3):
    choice = int(input('\nWrong Input Please choose a Ticket Type: '))
if choice == 1 or choice == 2 or choice == 3:
    print('\ncurrently you have:')
    print(f'   {num_bag} bag(s) registered')
    print(f'   {num_meal} meal(s) registered')
    print('\nHere are your options:')
    print('1. Add Bag (max 1)')
    print('2. Add Meal (max 1)')
    print('3. Remove Bag')
    print('4. Remove Meal')
    print('5. Finalize Ticket')
else:
    print('')

choice2 = int(input('\nEnter your Option Preference: '))
while choice2 != 5:
    if choice2 == 1:
        num_bag = 1
        print('\ncurrently you have:')
        print(f'   {num_bag} bag(s) registered')
        print(f'   {num_meal} meal(s) registered')
        print('\nHere are your options:')
        print('1. Add Bag (max 1)')
        print('2. Add Meal (max 1)')
        print('3. Remove Bag')
        print('4. Remove Meal')
        print('5. Finalize Ticket')
        choice2 = int(input('\nEnter your Option Preference: '))

    elif choice2 == 2:
        num_meal = 1
        print('\ncurrently you have:')
        print(f'   {num_bag} bag(s) registered')
        print(f'   {num_meal} meal(s) registered')
        print('\nHere are your options:')
        print('1. Add Bag (max 1)')
        print('2. Add Meal (max 1)')
        print('3. Remove Bag')
        print('4. Remove Meal')
        print('5. Finalize Ticket')
        choice2 = int(input('\nEnter your Option Preference: '))

    elif choice2 == 3:
        num_bag = 0
        print('\ncurrently you have:')
        print(f'   {num_bag} bag(s) registered')
        print(f'   {num_meal} meal(s) registered')
        print('\nHere are your options:')
        print('1. Add Bag (max 1)')
        print('2. Add Meal (max 1)')
        print('3. Remove Bag')
        print('4. Remove Meal')
        print('5. Finalize Ticket')
        choice2 = int(input('\nEnter your Option Preference: '))

    elif choice2 == 4:
        num_meal = 0
        print('\ncurrently you have:')
        print(f'   {num_bag} bag(s) registered')
        print(f'   {num_meal} meal(s) registered')
        print('\nHere are your options:')
        print('1. Add Bag (max 1)')
        print('2. Add Meal (max 1)')
        print('3. Remove Bag')
        print('4. Remove Meal')
        print('5. Finalize Ticket')
        choice2 = int(input('\nEnter your Option Preference: '))

    else:
        print('\nInvalid Input')
        choice2 = int(input('\nEnter your Option Preference: '))

if choice == 1:
    total = budget_ticket + (num_bag * bag + num_meal * meal)
    if (num_bag == 0 and num_meal == 0):
        total = budget_ticket
        print('Receipt:')
        print(f'Ticket :  {budget_ticket}kr')
        print("        -------")
        print(f'Total  :  {total}kr')
    if (num_bag == 1 and num_meal == 0):
        print('Receipt:')
        print(f'Ticket :  {budget_ticket}kr')
        print(f'Bag    :  {num_bag * bag}kr')
        print("        -------")
        print(f'Total  :  {total}kr')
    elif (num_bag == 0 and num_meal == 1):
        print('Receipt:')
        print(f'Ticket :  {budget_ticket}kr')
        print(f'Meal   :  {num_meal * meal}kr')
        print("        -------")
        print(f'Total  :  {total}kr')
    elif (num_bag == 1 and num_meal == 1):
        total = budget_ticket + (num_bag * bag + num_meal * meal)
        print('Receipt:')
        print(f'Ticket :  {budget_ticket}kr')
        print(f'Bag    :  {num_bag * bag}kr')
        print(f'Meal   :  {num_meal * meal}kr')
        print("        -------")
        print(f'Total  :  {total}kr')

elif choice == 2:
    total = budget_ticket + (num_bag * bag + num_meal * meal)
    if (num_bag == 0 and num_meal == 0):
        total = economy_ticket
        print('Receipt:')
        print(f'Ticket :  {economy_ticket}kr')
        print("        -------")
        print(f'Total  :  {total}kr')
    if (num_bag == 1 and num_meal == 0):
        print('Receipt:')
        print(f'Ticket :  {economy_ticket}kr')
        print(f'Bag    :  {num_bag * bag}kr')
        print("        -------")
        print(f'Total  :  {total}kr')
    elif (num_bag == 0 and num_meal == 1):
        print('Receipt:')
        print(f'Ticket :  {economy_ticket}kr')
        print(f'Meal  :  {num_meal * meal}kr')
        print("        -------")
        print(f'Total  :  {total}kr')
    elif (num_bag == 1 and num_meal == 1):
        total = economy_ticket + (num_bag * bag + num_meal * meal)
        print('Receipt:')
        print(f'Ticket :  {economy_ticket}kr')
        print(f'Bag    :  {num_bag * bag}kr')
        print(f'Meal   :  {num_meal * meal}kr')
        print("        -------")
        print(f'Total  :  {total}kr')
elif choice == 3:
    total = vip_ticket + (num_bag * bag + num_meal * meal)
    if (num_bag == 0 and num_meal == 0):
        total = vip_ticket
        print('Receipt:')
        print(f'Ticket : {vip_ticket}kr')
        print("        -------")
        print(f'Total  : {total}kr')
    if (num_bag == 1 and num_meal == 0):
        print('Receipt:')
        print(f'Ticket : {vip_ticket}kr')
        print(f'Bag  :  {num_bag * bag}kr')
        print("        -------")
        print(f'Total  : {total}kr')
    elif (num_bag == 0 and num_meal == 1):
        print('Receipt:')
        print(f'Ticket : {vip_ticket}kr')
        print(f'Meal  :  {num_meal * meal}kr')
        print("        -------")
        print(f'Total  : {total}kr')
    elif (num_bag == 1 and num_meal == 1):
        total = vip_ticket + (num_bag * bag + num_meal * meal)
        print('Receipt:')
        print(f'Ticket : {vip_ticket}kr')
        print(f'Bag    :  {num_bag * bag}kr')
        print(f'Meal   :  {num_meal * meal}kr')
        print("        -------")
        print(f'Total  : {total}kr')
