# list
nba_teams = ["Lakers", "Nuggets", "Celtics"]
nba_teams.append("Clippers")

# print with format
print(f"Length of nba teams: {len(nba_teams)}")

array_of_ones = [1] * 6

# declaring a list with range
one_through_ten = list(range(10))
print(one_through_ten)

random_numbers = [9,6,7,4,2,4]
random_numbers.sort()

# dictionary
dog = {
    "name": "Rocco",
    "location": "Los Angeles",
    "age": 7
}

print(dog)

# using f keyword for string interpolation
my_message = f"{dog['name']} lives in {dog['location']}."
print(my_message)

def add_numbers(num1, num2):
    result = num1 + num2
    return result


def print_this():
    print("Hello, my name is ...")

# using format function
def rome_prediction(team1, team2):
    return "I predict the {} and {} in the Western Conference Finals".format(team1, team2)

rome_prediction(nba_teams[0], nba_teams[3])


def legal_age(age):
    if (age < 21):
        return "Sorry, you're too young."
    elif (age == 21):
        return "You made it. Welcome to adulthood"
    else:
        return "You're free to pass. Enjoy!"

def the_spot(vip, food_place, location="Bay Area"):
    if (food_place == "full" and not vip):
        print("Sorry, we have no room tonight at this {} location".format(location))
    elif (food_place == "busy" and not vip):
        print("Please wait 30 mins for a table at this {} location".format(location))
    else:
        print("Welcome! Come sit down right away")