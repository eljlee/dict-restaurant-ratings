"""Restaurant rating lister."""
import sys

def restaurant_rating(filename):
    """Takes in a file, reads the restaurant and it's ratings, and stores them in a dictionary"""

    rating_file = open(filename)

    restaurant_ratings = {}

    for line in rating_file:
        line = line.rstrip()
        restaurant_name, rating = line.split(":")
        
        restaurant_ratings[restaurant_name] = rating


    for restaurant, number in sorted(restaurant_ratings.items()):
        print "{} is rated at {}".format(restaurant, number)


#restaurant_rating("scores.txt")

for text_file in sys.argv[1:]:
    restaurant_rating(text_file)