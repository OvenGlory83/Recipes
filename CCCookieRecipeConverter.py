# The quantity of each ingredient, entered in decimals instead of fractions.

ingredients = {
    'flour': 2.25,
    'bak_soda': 1.0,
    'salt': 1.0,
    'butter': 1.0,
    'gran_sug': 0.75,
    'brown_sug': 0.75,
    'vanilla_ext': 1.0,
    'eggs': 2.0,
    'choc_chips': 2.0
    }

# If you want to divide the recipe in half, enter 0.5. To double the recipe, enter 2.0, and so forth.
x = 2.0
def calculate(x):
    for ingredient in ingredients:
        print(ingredient, (x * ingredients[ingredient]))

calculate(x)        
        
              
        
    
