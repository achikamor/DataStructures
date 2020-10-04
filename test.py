##      Class example   ##
##input:
# dishes_list = [['Pizza', 'Veg', 2, 10], ['Kebab', 'Meat', 3, 25], ['Coke', 'Beverage', 1, 5],
#                ['Beer', 'Beverage', 1, 15]]
# order_list_of_dict = [{'order': "Pizza", 'money': 100, 'kind': "Veg"},
#                       {'order': "Beer", 'money': 60, 'kind': "Beverage"},
#                       {'order': "Kebab", 'money': 40, 'kind': "Meat"},
#                       {'order': "Beer", 'money': 20, 'kind': "Beverage"}]


##output:
# The restaurant sold:  ['Pizza', 'Beer', 'Kebab', 'Coke']
# The restaurant earned:  55




##      Empty dishes    ##
##input:
# dishes_list = []
# order_list_of_dict = [{'order': "Pizza", 'money': 100, 'kind': "Veg"},
#                       {'order': "Beer", 'money': 60, 'kind': "Beverage"},
#                       {'order': "Kebab", 'money': 40, 'kind': "Meat"},
#                       {'order': "Beer", 'money': 20, 'kind': "Beverage"}]

##output:
# We are sorry, we can't fulfil your order: Pizza
# We are sorry, we can't fulfil your order: Beer
# We are sorry, we can't fulfil your order: Kebab
# We are sorry, we can't fulfil your order: Beer
# The restaurant sold:  []
# The restaurant earned:  0

##      Too-Many   ##
#input:
# dishes_list = [['Greek-Salad', 'Veg', 4, 13], ['Steak', 'Meat', 5, 51], ['Coke', 'Beverage', 1, 5],
#                ['Beer', 'Beverage', 5, 15], ['Gondi', 'Veg', 3, 12], ['Beef', 'Meat', 2, 10]]
# order_list_of_dict = [{'order': "Pizza", 'money': 100, 'kind': "Veg"},
#                       {'order': "Beer", 'money': 60, 'kind': "Beverage"},
#                       {'order': "Steak", 'money': 30, 'kind': "Meat"},
#                       {'order': "Gondi", 'money': 20, 'kind': "Veg"},
#                       {'order': "Greek-Salad", 'money': 20, 'kind': "Veg"},
#                       {'order': "Beer", 'money': 20, 'kind': "Beverage"},
#                       {'order': "Beer", 'money': 20, 'kind': "Beverage"},
#                       {'order': "Beef", 'money': 20, 'kind': "Meat"},
#                       {'order': "Beef", 'money': 20, 'kind': "Meat"},
#                       {'order': "Steak", 'money': 20, 'kind': "Meat"},
#                       {'order': "Beer", 'money': 20, 'kind': "Beverage"},
#                       {'order': "Beer", 'money': 20, 'kind': "Beverage"},
#                       {'order': "Gondi", 'money': 20, 'kind': "Veg"},
#                       {'order': "Beer", 'money': 20, 'kind': "Beverage"}]

##output
# We are sorry, we can't fulfil your order: Pizza
# You better go to the bank my friend
# You better go to the bank my friend
# The restaurant sold:  ['Beer', 'Gondi', 'Greek-Salad', 'Beer', 'Beer', 'Beef', 'Beef', 'Beer', 'Beer', 'Gondi', 'Coke']
# The restaurant earned:  137


##      All-accepted    ##
##input:
# dishes_list = [['Pizza', 'Veg', 2, 10], ['Kebab', 'Meat', 3, 25], ['Coke', 'Beverage', 1, 5],
#                ['Beer', 'Beverage', 3, 15], ['Greek-Salad', 'Veg', 4, 13], ['Steak', 'Meat', 5, 51]]
# order_list_of_dict = [{'order': "Pizza", 'money': 100, 'kind': "Veg"},
#                       {'order': "Beer", 'money': 60, 'kind': "Beverage"},
#                       {'order': "Coke", 'money': 40, 'kind': "Beverage"},
#                       {'order': "Beer", 'money': 20, 'kind': "Beverage"},
#                       {'order': "Steak", 'money': 60, 'kind': "Meat"},
#                       {'order': "Greek-Salad", 'money': 20, 'kind': "Veg"},
#                       {'order': "Pizza", 'money': 100, 'kind': "Veg"},
#                       {'order': "Kebab", 'money': 30, 'kind': "Meat"}]

##output:
# The restaurant sold:  ['Pizza', 'Beer', 'Coke', 'Beer', 'Steak', 'Greek-Salad', 'Pizza', 'Kebab']
# The restaurant earned:  144
normal = 20
symbol = 30
expensive = 50

primes = [2, 3, 5, 7, 11, 13, 17, 19]
total_budget = 0
crowed_list = []
total_gifts = 0
not_specified = True
while not_specified:
    countries_number = int(input("Enter the amount of countries:"))
    if countries_number > 0:
        not_specified = False

for curr_country in range(countries_number):
    curr_budget = int(input("Enter the budget for country number #" + str(curr_country + 1) + ":"))
    total_budget += curr_budget
    not_done = True
    runner = 1
    while not_done:
        curr_crowed = int(input("Enter the amount of people at show number #" + str(runner) + ":"))
        if curr_crowed == 0 or curr_crowed == -999:
            not_done = False
        else:
            crowed_list.append(curr_crowed)
            runner += 1

crowed_list_copy = crowed_list.copy()
for crowed_runner in range(len(crowed_list)):
    number = crowed_list_copy[crowed_runner]
    for smaller in range(2, number+1):
        if smaller <= primes[-1]:
            if smaller in primes:
                crowed_list[crowed_runner] -= 1
        else:
            to_append = True
            for prime in primes:
                if smaller % prime == 0:
                    to_append = False
                    break
            if to_append:
                primes.append(smaller)
                crowed_list[crowed_runner] -= 1

for filter_crowed in crowed_list:
    total_gifts += filter_crowed
print("We need " + str(total_gifts) + " pouches.")

if expensive * total_gifts <= total_budget:
    print("We can afford the expensive type")
elif symbol * total_gifts <= total_budget:
    print("We can afford the symbol type")
elif normal * total_gifts <= total_budget:
    print("We can afford the normal type")
else:
    print("We can't afford any of the pouches")
diff = expensive * total_gifts - total_budget
if diff <= 0:
    diff = 0
print("In order to afford the expensive pouches, we need to add " + str(diff) + " shekels.")
