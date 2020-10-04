dishes_list = [['Pizza', 'Veg', 2, 10], ['Kebab', 'Meat', 3, 25], ['Coke', 'Beverage', 1, 5],
               ['Beer', 'Beverage', 3, 15]]
order_list_of_dict = [{'order': "Pizza", 'money': 100, 'kind': "Veg"},
                      {'order': "Beer", 'money': 50, 'kind': "Beverage"},
                      {'order': "Kebab", 'money': 40, 'kind': "Meat"},
                      {'order': "Beer", 'money': 50, 'kind': "Beverage"},
                      {'order': "Beer", 'money': 20, 'kind': "Beverage"}
                      ]

menu = {"Veg": {}, "Meat": {}, "Beverage": {}}
total_amount = 0
fulfil_list = list()
for DL_index in range(len(dishes_list)):
    name = dishes_list[DL_index][0]
    kind = dishes_list[DL_index][1]
    amount = dishes_list[DL_index][2]
    price = dishes_list[DL_index][3]
    menu[kind][name] = [amount, price]

print(menu)

for curr_order in order_list_of_dict:
    curr_kind = curr_order['kind']
    curr_money = curr_order["money"]
    curr_name = curr_order["order"]
    if curr_name in menu[curr_kind]:
        dish_details = menu[curr_kind][curr_name]
        if curr_money >= dish_details[1]:
            if dish_details[0] > 0:
                dish_details[0] = dish_details[0] - 1
                total_amount += dish_details[1]
                fulfil_list.append(curr_name)
            else:
                updated_kind = menu[curr_kind].copy()
                updated_kind.pop(curr_name)

                for new_dish_name, new_dish_details in updated_kind.items():
                    if new_dish_details[1] <= curr_order['money'] and new_dish_details[0] > 0:
                        menu[curr_kind][new_dish_name] = new_dish_details[0] - 1
                        total_amount += new_dish_details[1]
                        fulfil_list.append(new_dish_name)
                        break
                else:
                    print("We are sorry, we can't fulfil your order: " + curr_name)
        else:
            print("You better go to the bank my friend")
    else:
        print("We are sorry, we can't fulfil your order: " + curr_name)

print("The restaurant sold: ", fulfil_list)
print("The restaurant earned: ", total_amount)
