"""Restaurant rating lister."""
import sys


def user_input():
    """Takes in user input for restaurant and it's rating, append to dictionary, and returning update dictionary"""
    restaurant_name_input = raw_input("Enter Restaurant name: ")
    restaurant_score_input = int(raw_input("Enter Restaurant's rating: "))

    return restaurant_name_input, restaurant_score_input


def restaurant_rating(filename):
    """Takes in a file, reads the restaurant and it's ratings, and stores them in a dictionary"""

    rating_file = open(filename)

    restaurant_ratings = {}

    for line in rating_file:
        line = line.rstrip()
        restaurant_name, rating = line.split(":")

        restaurant_ratings[restaurant_name] = rating

    # for restaurant, number in sorted(restaurant_ratings.items()):
    #     print "{} is rated at {}".format(restaurant, number)

    restaurant_name_input, restaurant_score_input = user_input()

    restaurant_ratings[restaurant_name_input] = restaurant_score_input

    for restaurant, number in sorted(restaurant_ratings.items()):
        print "{} is rated at {}".format(restaurant, number)

for text_file in sys.argv[1:]:
    restaurant_rating(text_file)
