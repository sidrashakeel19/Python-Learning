import calculations
import csv
import json
# functions 41 to 50


def add_numbers():
    first_number = 2
    second_number = 3
    total = first_number + second_number
    print(total)


def add_numbers1(first_number, second_number=5):
    total = first_number + second_number
    print(total)


def greet_user(greeting1, greeting2):
    print(greeting1)
    print(greeting2)


def find_something(dict, inner_dict, target):
    print(dict[inner_dict][target])


def display_result(winner, score, **other_info):
    print("The winner was " + winner)
    print("The score was " + score)
    for key, value in other_info.items():
        print(key + ": " + value)


def display_nums_optional(winner, score, *other_info):
    print(winner)
    print(score)
    print(other_info)


def calc_tax(sales_total, tax_rate):
    tax = sales_total * tax_rate
    return tax


greet_user(greeting2="greeting2", greeting1="greeting1")
greet_user("new value", greeting2="greeting1")
add_numbers()
add_numbers1(1.255, 1)
add_numbers1(1.255)
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

# ** is used for key val, * is used for single values and will be saved as tupple
find_something(customers, 2, "last name")
display_result(winner="Real Madrid", score="1-0",
               overtime="yes", injuries="none")
display_nums_optional(100, 200, 300, 400, 500)
sales_tax = calc_tax(sales_total=101.37,
                     tax_rate=.05)
print(sales_tax)

# while loop 51
print("*****************WHILE******************")
counter = 0
while(counter < 10):
    print(counter)
    counter = counter + 1
# classes 53
print("*****************CLASSES******************")


class Patient():
    def __init__(self, last_name, first_name, age):  # ctor
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

    def toString(self):
        print(self.first_name)
        print(self.last_name)
        print(self.age)

    def setAge(self, newAge):
        self.age = newAge


pid4343 = Patient("Taleb", "Sue", 61)
print(pid4343.first_name)
pid4343.toString()
pid4343.first_name = "updated name"
pid4343.toString()
pid4343.setAge(100)
pid4343.toString()
# Data Files 62
print("*****************Data Files******************")
# with is replacement of using() in C#
with open("whatever.txt", "w") as objFile:
    objFile.write("Hello world 123")

with open("whatever.txt", "a") as objFile:
    objFile.write("\nHello world 123 appended")

# read mode is default so if you dont pass 2nd param its fine
with open("whatever.txt", "r") as objFile:
    print(objFile.read())

# Data Files 66
print("*****************Modules******************")
print(calculations.calc_tax(sales_total=101.37,
                            tax_rate=.05))
# Data Files 67
print("*****************CSV Files******************")
with open("competitions.csv") as f:
    contents_of_file = csv.reader(f)
    potter_competitions = []
    for each_line in contents_of_file:
        potter_competitions += each_line
    print(potter_competitions)
    print(potter_competitions[1])
with open("competitions.csv", "a", newline="") as f:
    data_handler = csv.writer(f, delimiter=",")
    data_handler.writerow(["2015", "Best-Kept Lawn",
                           "None"])

alphabet_letters = ["a", "b", "c"]
with open("jsonfile.txt", "w", newline="") as f:
    json.dump(alphabet_letters, f)
alphabet_letters = []
with open("jsonfile.txt", "r", newline="") as f:
    alphabet_letters = json.load(f)
print(alphabet_letters)
# Data Files 76
print("*****************Execptions******************")
try:
    x = 1/0
except:
    print("error")
