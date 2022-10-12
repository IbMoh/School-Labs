print('Welcome to the Money Bag Transport Calculator M.B.T.C!')  # welcome message
print('------------------------------------------------------')

# these are the bags L
small_bag = 20
medium_bag = 50
large_bag = 80

# these are the bags cost
s_b = 10000
m_b = 30000
l_b = 60000

# total volume
volume = 100

# this will let the user input the truck's volume
truck_volume = int(input('\nWhat is the volume of the truck (>= 100L)? '))

# a loop if the person inputs the wrong data
while truck_volume < volume:
    truck_volume = int(input('What is the volume of the truck (>= 100L)? '))

# calculations for the amount of bags that is being transported
truck_volume > volume

c_t = truck_volume // large_bag
sum = truck_volume - (c_t * large_bag)

if sum >= medium_bag:
    b_t = sum // medium_bag
    sum2 = sum - (b_t * medium_bag)
    if sum2 >= small_bag:
        a_t = sum2 // small_bag
    else:
        a_t = 0
else:
    b_t = 0
    if sum >= small_bag:
        a_t = sum // small_bag
    else:
        a_t = 0
# volume left in truck
total_left = truck_volume - (c_t * large_bag + b_t * medium_bag + a_t * small_bag)
# calculations for the amount of money in the bags
sum_cost_big = c_t * l_b
sum_cost_med = b_t * m_b
sum_cost_sma = a_t * s_b

total_sum = sum_cost_big + sum_cost_med + sum_cost_sma

# data output
print('\nPackaging Plan')
print("--------------")
print(f'{c_t} big bags')
print(f'{b_t} medium bags')
print(f'{a_t} small bags')
print(f'\nSpace left : {total_left} ')
print(f'Total Value: {total_sum}Kr')
