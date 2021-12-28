import pyinputplus as cstom_input

bread_types = ['Wheat', 'white', 'sourdough']
meat_types = ['chicken', 'turkey', 'ham', 'tofu']
cheese_types = ["cheddar", "Swiss", "mozzarella"]
protein_price = [100,200,300,400]
bread_price = [100,200,300]
cheese_price = [100,200,300]

def take_input():

    bread = cstom_input.inputMenu(bread_types)

    protein = cstom_input.inputMenu(meat_types)
    cheese = cstom_input.inputYesNo("Do you want to have cheese ? ")
    if(cheese == 'yes' ):
        cheese_type = cstom_input.inputMenu(cheese_types)
    extra = cstom_input.inputYesNo("want mayo, mustard, lettuce, or tomato?? ")
    sand_count = cstom_input.inputNum("Enter the number of sandwhich you want", min=1)
    return [bread_types.index(bread),meat_types.index(protein),cheese,cheese_types.index(cheese_type),extra,sand_count]


def cal_price(lst):
    total = protein_price[lst[0]] + bread_price[lst[1]]
    if(lst[2] == "yes"):
        total += cheese_price[lst[3]]
    if(lst[4] == "yes"):
        total += 200
    total = total * lst[5]
    print("The total amount is: ", total)

option_list = take_input()
cal_price(option_list)
