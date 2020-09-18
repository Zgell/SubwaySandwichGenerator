import random       

sandwich = ['BBQ Pulled Pork', 'BBQ Rotisserie Style Chicken', 'Chicken and Bacon Ranch Melt', 'Cold Cut Combo', 'Black Forest Ham', 'Italian B.M.T.',
'Meatball Marinara', 'Oven Roasted Chicken', 'Pizza Sub Melt', 'Roast Beef', 'Steak and Cheese', 'Subway Club', 'Sweet Onion Chicken Teriyaki', 'Tuna',
'Turkey Breast and Black Forest Ham', 'Turkey Breast', 'Veggie Delite']
bread = ['Italian','Italian Herbs and Cheese','9-Grain Honey Oat','9-Grain Wheat','Ciabatta','Flatbread','Wrap']
cheese = ['Orange Cheese','White Cheese','Swiss Cheese']
toasted = ['Not Toasted','Toasted']
veggies = ['Spinach','Banana Peppers','Black Olives','Cucumbers','Green Peppers','Lettuce','Pickles','Red Onions','Tomatoes'] # 9 different vegetables
seasonings = ['Grated Parmesan','Oregano','Salt','Pepper'] # 4 seasonings
sauces = ['Chipotle Southwest', 'House Sandwich Sauce', 'Honey Mustard', 'Light Mayo', 'Regular Mayo', 'Mustard', 'Ranch', 'Caesar', 'Sweet Onion'] # 9 sauces

def bread_curve():
        x = 0
        curved_bread = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 6]
        rand = random.randint(0, len(curved_bread)-1)
        x = curved_bread[rand]
        return x
def veggie_curve():
        x = 0
        rand = random.randint(1, 100)
        while (rand < (90 - (9 * x))):
                rand = random.randint(1, 100)
                x += 1
        if x > 9:
                x = 9
        return x

def seasoning_curve():
        x = 0
        rand = random.randint(1, 100)
        while (rand < (85 - (20 * x))):
                rand = random.randint(1, 100)
                x += 1
        if x > 4:
                x = 4
        return x
def sauce_curve():
        x = 0
        sauce_weights = [0,0,0,0,0,1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,4,4,4,5,5,6,7,8,9]
        rand = random.randint(0, len(sauce_weights)-1)
        x = sauce_weights[rand]
        return x

print("Subway Sandwich Generator")
print("")

random_int = random.randint(0,len(sandwich)-1)
print("  Sandwich: " + sandwich[random_int])
random_int = random.randint(0,len(bread)-1)
print("     Bread: " + bread[bread_curve()])
random_int = random.randint(0,len(cheese)-1)
print("    Cheese: " + cheese[random_int])
random_int = random.randint(0,len(toasted)-1)
print("   Toasted: " + toasted[random_int])

vegetable_number = veggie_curve() #The number of vegetables that go on the sandwich
veggie_list = [] #A variable for storing all of the vegetables
i = 0 #Number of vegetables actually put on the sandwich / in the list
while (i != vegetable_number):
        random_int = random.randint(0,len(veggies)-1)
        while (veggie_list.count(veggies[random_int]) > 0): #Reroll to prevent duplicate veggies
                random_int = random.randint(0,len(veggies)-1)
        veggie_list.append(veggies[random_int])
        i += 1
if len(veggie_list) == 0:
        veggie_list.append("None")
print("   Veggies:", ", ".join(veggie_list))



seasoning_number = random.randint(0, len(seasonings)) #The number of seasonings that go on the sandwich
seasoning_list = [] #A variable for storing all of the seasonings
i = 0 #Number of seasonings actually put on the sandwich / in the list
while (i != seasoning_number):
        random_int = random.randint(0,len(seasonings)-1)
        while (seasoning_list.count(seasonings[random_int]) > 0): #Reroll to prevent duplicate veggies
                random_int = random.randint(0,len(seasonings)-1)
        seasoning_list.append(seasonings[random_int])
        i += 1
if len(seasoning_list) == 0:
        seasoning_list.append("None")
print("Seasonings:", ", ".join(seasoning_list))



sauce_number = sauce_curve() #The number of seasonings that go on the sandwich
sauce_list = [] #A variable for storing all of the seasonings
i = 0 #Number of seasonings actually put on the sandwich / in the list
while (i != sauce_number):
        random_int = random.randint(0,len(sauces)-1)
        while (sauce_list.count(sauces[random_int]) > 0): #Reroll to prevent duplicate veggies
                random_int = random.randint(0,len(sauces)-1)
        sauce_list.append(sauces[random_int])
        i += 1
if len(sauce_list) == 0:
        sauce_list.append("None")
print("    Sauces:", ", ".join(sauce_list))