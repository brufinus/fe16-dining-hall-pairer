import yaml

def get_shared_liked_meals(characters):
    """Returns a list of shared liked meals for a pair of characters."""
    shared_liked_meals = []
    with open('liked_meals.yml') as stream:
        try:
            liked_meals_dict = yaml.safe_load(stream)
            for meal in liked_meals_dict:
                if characters[0] in liked_meals_dict[meal] and characters[1] in liked_meals_dict[meal]:
                    shared_liked_meals.append(meal)
        except yaml.YAMLError as exc:
            print(exc)
    return shared_liked_meals

def get_pair(inp_character=''):
    """Returns a list of two characters to pair.

    Gets characters as input from user. Accepts first character as input.
    """
    characters = []
    descriptor = ['First', 'Second']
    if inp_character != '' and validate_character(inp_character):
        characters.append(inp_character)
    while len(characters) < 2:
        character = (input(f'{descriptor[len(characters)]} character: ')).capitalize()
        if validate_character(character):
            characters.append(character)
    return characters

def validate_character(character):
    """Returns True if character is in the list of characters. Prints an error message and returns False otherwise."""
    with open('characters.yml') as stream:
        try:
            character_dict = yaml.safe_load(stream)
            dict_vals = character_dict['characters']
            if character in dict_vals:
                return True
            print('Invalid character - enter a valid name.')
            return False
        except yaml.YAMLError as exc:
            print(exc)

def execute_pairer(inp_character=''):
    """Executes the pairer and prints output depending on what it finds."""
    character_list = get_pair(inp_character)
    print(f'Finding shared liked meals for {character_list[0]} and {character_list[1]}...\n')
    meals = get_shared_liked_meals(character_list)
    plurality = ['this meal', 'these meals']
    if len(meals) > 1:
        print(f'{character_list[0]} and {character_list[1]} enjoy {plurality[1]} together:')
    elif len(meals) == 1:
        print(f'{character_list[0]} and {character_list[1]} enjoy {plurality[0]} together:')
    else:
        print(f'{character_list[0]} and {character_list[1]} don\'t enjoy any meals together.')
        return
    print('\n'.join(meals))

print('Dining Hall Liked Meal Pairer\nProvide two characters to view their shared liked meals.\n')
user_in = ''
while True:
    execute_pairer(user_in)
    user_in = (input('\nInput another character to run again (n to exit): ')).capitalize()
    if user_in == 'N':
        break
