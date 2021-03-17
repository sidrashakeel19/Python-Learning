# ----1 & 2
'''
print("Hello, ", "Sidra", "Welcome", sep="!", end="\n\n\n")
print("Hello, World!", 1, 2, 3.5, False, 4, "test")
print("Hello, World!", 1, 2, 3.5, 4, "test")
name = "Mark"
print(name)
print("double qoute")
print('single quote')

# ----3
weight = 150
print(weight)
original_num = "23"
#new_num = original_num + 7 #this line will give execption as string cant be added into numbers
#print(new_num)
original_num = 8
print(original_num)  # now this variable is refering to int

# ----4
num = 10
another_num = 1.5
sum_of_numbers = num + another_num
print(sum_of_numbers)
print(100/100)  # division returns in float
# but if you use // it will return in int it discards after . it does not round the number
print(100//100)

# ----6
age = 10
age *= 3
whats_left_over = 10 % 3
print(age)
print(whats_left_over)

# ----7
result_of_computation = (2 * 4) * (4 + 2)
print(result_of_computation)

# ----8
whole_greeting = "Hello, " + "World!"
print(whole_greeting)
print(whole_greeting + "new string")
# print("The sum of 2 plus 2 is " + 4) # error you can't use the plus sign to combine strings and numbers
print("The sum of 2 plus 2 is " + "4")

# ----9
species = "mouse"
if species == "cat":
    print("Yep, it's cat.")
    print("still inside if")
elif species == "dog":
    print("it's a dog")
else:
    print("not cat")
print("outside if")
# ----10 Conditional Operators
# ----11 else and elif

# ----12 and 13
weight = 300
time = 6
if weight < 300 and time == 6:  # or for or
    if 1 == 1 or 2 == 0:
        print("demo with or operator and nested if")
    else:
        print("nested else")
    print("with and oeprator")
'''

'''
# ----14
'''
'''
#this is multi line comments
#line 1
#line 2
#line 3

print("comments example finished")

# ----15
cities = ["Atlanta", "Baltimore", "Chicago",
          "Denver", "Los Angeles", "Seattle"]
print(cities)
print("welcome to " + cities[4])
mixed_things = [1, "Bob", "Now is"]
print(mixed_things)

# ----16
cities = ["Atlanta", "Baltimore", "Chicago",
          "Denver", "Los Angeles", "Seattle"]
cities.append("New York")
print(cities)
cities = cities + ["Dubuque", "New Orleans"]
print(cities)
cities.insert(3, "Florida")  # adds 1 item
print(cities)
cities.extend(["Lahore", "Karachi"])  # can append multiple items
print(cities)
cities[2] = "Houston"
print(cities)
cities2 = cities.copy()  # copies by value
cities3 = cities  # by reference
print("Copy of cities", cities2)
print("Reference of cities", cities3)
todays_tasks = []
print(todays_tasks)
todays_tasks = todays_tasks + ["Walk dog", "Buygroceries"]
print(todays_tasks)

# ----17
# slicing main forward hi chalte hain and if error ata hai to slice empty return karta hai
cities = ["Atlanta", "Baltimore", "Chicago",
          "Denver", "Los Angeles", "Seattle"]
smaller_list_of_cities = cities[2:5]
print(smaller_list_of_cities)
print(cities[2:-2])
print(cities)
smaller_list_of_cities = cities[:5]
print(smaller_list_of_cities)
print(cities[:-5])
smaller_list_of_cities = cities[2:]
print(smaller_list_of_cities)
print("numbers")
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(numbers[0:21:2])  # 0 sy start karo 21 tak jao and with step of 2
print(numbers[::5])  # 0 sy start karo end tak jao 5 ka step

# ----18
cities = ["Atlanta", "Baltimore", "Chicago",
          "Denver", "Los Angeles", "Seattle", "New York"]
print("Sort")
print(cities)
cities.sort(reverse=True)
print(cities)
cities.sort()
print(cities)
del cities[1]
print(cities)
del cities[-1]
print(cities)
del cities[0:5:2]  # removes from 0 to 2 with 1 step
print(cities)
cities.remove("Chicago")  # only removes first element it finds
print(cities)

# ----19
cities = ["Atlanta", "Baltimore", "Chicago",
          "Denver", "Los Angeles", "Seattle", "New York"]
print(cities.pop())  # last element will pop
print(cities.pop(0))
print(cities)
print(cities.pop(2))
print(cities)
print(cities.pop(-2))
print(cities)

# ----20 tupple = enum in c#
aTupple = 12, 13, 15, "asdf"
print(aTupple)
states_in_order_of_founding = (
    "Delaware", "Pennsylvania", "New Jersey", "Georgia")
print("The second state founded was " + states_in_order_of_founding[1])

# ----21
cleanest_cities = ["Cheyenne", "Cheyenne", "Santa Fe", "Tucson",
                   "Great Falls", "Honolulu"]
print("Montana" in cleanest_cities)
#cleanest_cities.extend(["1", "2"])
print(len(cleanest_cities))
print(cleanest_cities.count("Cheyenne"))
print(cleanest_cities.index("Cheyenne"))
# cleanest_cities.clear()
city_to_check = "New York"
for a_clean_city in cleanest_cities:
    if a_clean_city == city_to_check:
        print("It's one of the cleanest cities")
    print("It's not a clean city")
    break

# ----22
first_names = ["BlueRay ", "Upchuck ", "Lojack ",
               "Gizmo ", "Do-Rag "]
last_names = ["Zzz", "Burp", "Dogbone", "Droop"]
full_names = []
for a in range(5):
    print(a)
for a in range(10, 0, -2):
    print(a)
for a_first_name in first_names:
    for a_last_name in last_names:
        full_names.append(a_first_name + " " + a_last_name)
print(full_names)

# ----23 casting
city_to_check = input("Enter the name of a city: ")
print(city_to_check)
print(int("2")+2)  # casting
print(float("2.2")+2)
print(str(2.2)+"2")
print(type(3))
print(type(3.222))
print(type("3"))

# ----24
print("TOLOWER".lower())
print("toupper".upper())
print("to upper".title())
'''
# ----25 Dictionaries
'''customer_29876 = {
    "first name": "David", 
    "last name": "Mrejen", 
    "address": "4803 Wellesley St."
    "discounts": ["standard", "volume", "loyalty"], 
}
print(customer_29876)
print(customer_29876["first name"])
print(customer_29876)
customer_29876["newKey"] = "123"
print(customer_29876["newKey"])
print(customer_29876)
#print(customer_29876[222])
del customer_29876[222]
print(customer_29876)

print("")
for a in customer_29876.keys():
    print(a)
for a in customer_29876.values():
    print(a)
for key, val in customer_29876.items():
    print(key)
    print(val)
print("address" in customer_29876)

#dic of dic
customers = {
    "johnog": {
        "first name": "John",
        "last name": "Ogden",
        "address": "301 Arbor Rd.",
    },
    "coder1200": {
        "first name": "Ann",
        "last name": "Sattermyer",
        "address": "PO Box 1145",
    },
    "madmaxine": {
        "first name": "Jill",
        "last name": "Somers",
        "address": "3 Main St.",
    },
}
print(customers["madmaxine"])
print(customers["madmaxine"]["address"])
customersListOfDic = [
    {
        "customer id": 0,
        "first name": "John",
        "last name": "Ogden",
        "address": "301 Arbor Rd.",
    },
    {
        "customer id": 1,
        "first name": "Ann",
        "last name": "Sattermyer",
        "address": "PO Box 1145",
    },
    {
        "customer id": 2,
        "first name": "Jill",
        "last name": "Somers",
        "address": "3 Main St.",
    },
]
#print(customersListOfDic[1]["address"])


#chapter 36: appending a new dic to a list of dic

new_customer_id = len(customers)
new_first_name = "Sidra"
new_last_name = "Shakeel"
new_address = "A605"
print(new_customer_id)
new_dictionary = {
        "customer id": new_customer_id,
        "first name": new_first_name,
        "last name": new_last_name,
        "address": new_address,
        "discounts": ["standard", "volume", "loyalty"], 
}
#print(customers)
#print(new_dictionary)
customersListOfDic.append(new_dictionary)
#print(customersListOfDic)

customer_29876 = {
    "first name": "David", 
    "last name": "Mrejen", 
    "address": "4803 Wellesley St.",
    "discounts": ["standard", "volume", "loyalty"], 
}
if "brother_in_law" in customer_29876["discounts"]:
    discount_amount = .30
elif "loyalty" in customer_29876["discounts"]:
    discount_amount = .15
elif "volume" in customer_29876["discounts"]:
    discount_amount = .10
elif "standard" in customer_29876["discounts"]:
    discount_amount = .5
print(discount_amount)

#chapter 39 creating a dic that contains a dic


#dic of dic
customers = {
    0: {
        "first name": "John",
        "last name": "Ogden",
        "address": "301 Arbor Rd.",
    },
    1: {
        "first name": "Ann",
        "last name": "Sattermyer",
        "address": "PO Box 1145",
    },
    2: {
        "first name": "Jill",
        "last name": "Somers",
        "address": "3 Main St.",
    },
}

print(customers[0])
print(customers[2]["first name"])


#chapter 41: Functions

first_number = 2.8
second_number = 32

def add_numbers(first_number,second_number):    
    total = first_number + second_number
    print(total)

add_numbers(first_number,second_number)

husband_name = "Zain"
wife_name = "Sidra"
def say_names_of_couple(husband_name, wife_name):
    print("The names of the couple are " + husband_name + " and " + wife_name)
say_names_of_couple(wife_name,husband_name)


def calc_tax(sales_total, tax_rate=0.04):
    print(sales_total * tax_rate)
calc_tax(sales_total=101.37)

#def give_greeting(greeting, first_name):
#    print(greeting + ", " + first_name)
def give_greeting(greeting, first_name, flattering_nickname=" the wonder boy"):
    print(greeting + ", " + first_name + flattering_nickname)

give_greeting("Hello there", first_name="Al")

def find_something(dict, inner_dict, target):
    print(dict[inner_dict][target])

find_something(customers,1,"first name")

#chapter 46

def display_result(winner, score, **other_info):
    print("The winner was " + winner)
    print("The score was " + score)
    for key, value in other_info.items():
        print(key + ": " + value)
display_result(winner="Real Madrid", score="1-0", overtime="Yes", injuries="No")

def display_nums(first_num, second_num, *opt_nums):
    print(first_num)
    print(second_num)
    print(opt_nums)
display_nums(100, 200, 300, 400, 500, 600)

def calc_tax(sales_total, tax_rate):
    return(sales_total * tax_rate)
sales_tax = calc_tax(sales_total=101.37, tax_rate=.05)
print(sales_tax)

#chapter 51: while loops

cleanest_cities = ["Cheyenne", "Santa Fe", "Tucson", "Great Falls", "Honolulu"]
user_input = ""
while user_input != "q":
    user_input = input("Enter a city, or q to quit:")
    if user_input != "q":
        for a_clean_city in cleanest_cities:
            if user_input == a_clean_city:
                print("It's one of the cleanest cities")
                break


#Chapter 53: Classes

class Patient():
    def __init__(self, last_name, first_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
def say_if_minor(patient_first_name, patient_last_name, patient_age):
    if patient_age < 21:
        print(patient_first_name + " " + patient_last_name + " is a minor")
pid4343 = Patient("Taleb", "Sue", 61)
pid4344 = Patient("Anand", "Punya", 29)
pid4345 = Patient("Oppenheimer", "Douglas", 15)
pid4346 = Patient("Lin", "Lilly", 48)
pid12902 = Patient("Nilsson", "Rhonda", 33)
'''
'''print(pid4345.first_name)
age_of_patient = pid4345.age
print(age_of_patient)'''
'''
#pid4345.say_if_minor()
say_if_minor(pid4345.first_name, pid4345.last_name, pid4345.age)
#pid4343.say_if_minor("April", insured=True)

#creating a method within a class chaptr 60

class Patient():
    def __init__(self, last_name, first_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
    def say_if_minor(self):
        if self.age < 21:
            print(self.first_name + " " + self.last_name + " is a minor")
        else:
            print(self.first_name + " " + self.last_name +" is an adult")
    def change_last_name(self, new_last_name):
        self.last_name = new_last_name

pid4343 = Patient("Taleb", "Sue", 61)
pid4344 = Patient("Anand", "Punya", 29)
pid4345 = Patient("Oppenheimer", "Douglas", 15)
pid4346 = Patient("Lin", "Lilly", 48)
pid12902 = Patient("Nilsson", "Rhonda", 33)

pid4345.say_if_minor()
pid4346.say_if_minor()

pid4343.change_last_name("Ortega")
pid4343.say_if_minor()
'''

#chapter 62
#Writing data with keyword "w". we use 'with' to close the file when we have written to the file
#with open("whatever.txt", "w") as file_to_work_with:
#file_to_work_with = open("whatever.txt", "w"):
'''
greeting = "My name is Sidra"
with open("greet.txt", "w") as f:
    f.write("Hello World! ")
    f.write(greeting)


#Chapter 64
#Retrieving data with keyword "r", we can skip r to read data as it is the default setting with open keyword

with open("greet.txt", "r") as f:
    text_of_file = f.read()
print(text_of_file)

#Chapter 65
#Appending data with keyword "a"

with open("greet.txt", "a") as f:
    f.write("\nHave a nice day!")

with open("greet.txt") as f:
    message = f.read()
print(message)


#Chapter 66 Modules
import calculations

tax_for_this_order = calculations.calc_tax(sales_total=101.37, tax_rate=.05)
print(tax_for_this_order)

#Chapter 67 CSV Files
import csv

with open("competitions.csv") as f:
    contents_of_file = csv.reader(f)
    potter_competitions = []
    for each_line in contents_of_file:
        potter_competitions += each_line
print(potter_competitions)
#print(potter_competitions[10])
target = input("Enter the name of a competition: ")
index_number_of_target = potter_competitions.index(target)
print(index_number_of_target)
index_number_of_winner = index_number_of_target + 1
the_winner = potter_competitions[index_number_of_winner]
print("Winner is: ", the_winner)

#Chapter 70 loading info into csv files
import csv
with open("new_competitions.csv", "w", newline="") as f:
    data_handler = csv.writer(f, delimiter=",")
    data_handler.writerow(["Year", "Event", "Winner"])
    data_handler.writerow(["1995", "Best Kept Lawn", "None"])
    data_handler.writerow(["1999", "Gobstones", "Welch National"])

# Chapter 73 appending data onto them
with open("new_competitions.csv", "a", newline="") as f:
    data_handler = csv.writer(f, delimiter=",")
    data_handler.writerow(["2006", "Football World Cup", "Brazil"])
    data_handler.writerow(["2008", "Cricket World Cup", "Australia"])
    data_handler.writerow(["2012", "Cricket World Cup", "India"])
'''
#Chapter 74 JSON

import json

alphabet_letters = ["a", "b", "c"]

customer_29876 = {
    "first name": "David",
    "last name": "Elliott",
    "address": "4803 Wellesley St.",
    }

'''
with open("alphabet_list.json", "w") as f:
    json.dump(alphabet_letters, f)
    
with open("customer.json", "w") as f2:
    json.dump(customer_29876, f2)


with open("customer.json") as f:
    customer_29876 = json.load(f)
    print(customer_29876)

try:
    filename = input("What text file to open? ")
    with open(filename) as f:
        print(f.read())
except FileNotFoundError:
    print("Sorry, " + filename + " not found.")

while True:
    try:
        filename = input("What text file to open? ")
        with open(filename) as f:
            print(f.read())
            break
    except FileNotFoundError:
        print("Sorry, " + filename + " not found.")
'''

