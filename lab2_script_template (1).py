def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        'name' : 'Jay Chaudhary',
        'student id' : '1240',
        'pizza_toppings' : [
            'PEPPERONI',
            'MUSHROOM',
            'GREEN_PEPPER'
        ],
        'movies' : [
            {
                'title' : 'Avengers Endgame',
                'genre' : 'Suspense'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       '
            },
            {
                'tile' : 'Intersellar',
                'genre' : 'Mystery' 
            }
        ]
    }

    # TODO: Step 3 - Add another movie to the data structure
    new_movie = {
                'tile' : 'Spider-Man',
                'genre' : 'Action' 
            }
    about_me['movies'].append(new_movie)
    print(movies) # Temporary debug print

# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me)
    name = about_me['name']
    first_name = name.split()[0]
    student_id = about_me['student_id']
    print(f"My name is {name}, but you can call me {first_name}.")
    print(f"My student ID is {student_id}.")
    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    about_me['pizza_toppings'].extend(toppings)
    lowercase_toppings = []
    for topping in about_me['pizza_toppings']:
        lowercase_toppings.append(topping.lower())
    about_me['pizza_toppings'] = sorted(lowercase_toppings)
    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print("my favourite pizza toppings are:")
    toppings = about_me['pizza_toppings']
    for topping in toppings:
        formatted_topping = topping.capitalize()
        print(f"- {formatted_topping}")
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    genres = [movie['genre'] for movie in about_me['movies']]
    print(f"I like to watch {','.join(genres)} movies.")
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    titles = [movie[title].tile() for movie in movie_list]
    print(f'Some of my favourite mobies are {','.join(titles)}!")
    return
    
if __name__ == '__main__':
    main()