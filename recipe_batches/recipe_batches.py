#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    recipe_requires = []
    available_ingredients = []
    leftover_ingredients = []

    for key in recipe:
        # checks to make sure all of the ingredients needed for the recipe are available.  If not, return 0
        if key not in ingredients:
            return 0
        # adds the recipe and ingredients to the empty arrays above
        else:
            recipe_requires.append(recipe[key])
            available_ingredients.append(ingredients[key])

    for i, ingredient in enumerate(available_ingredients):
        amount_left = ingredient - recipe_requires[i]

        if amount_left < 0:
            return 0
        else:
            leftover_ingredients.append(ingredient / recipe_requires[i])
            return(math.floor(min(leftover_ingredients)))


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
