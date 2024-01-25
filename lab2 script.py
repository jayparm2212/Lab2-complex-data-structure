def main():
    about_me = {
        'full_name': 'Jaydip Parmar',
        'student_id': 10321035,
        'pizza_toppings': ['Mushroom', 'Onion', 'Fresh Garlic'],
        'movies': [
            {
                'title': 'Thor',
                'genre': ' Action'
            },
            {
                'title': 'Jumanji',
                'genre': 'Adventure'
            }
        ]
    }

    about_me['movies'].append({'title': 'Phir Hera Pheri', 'genre': 'comedy'})
    
    print_student_info(about_me)
    print_pizza_toppings(about_me)
    print()
    add_pizza_toppings(about_me, ('Peppers', 'Black Olives'))
    print()
    print_pizza_toppings(about_me)
    print()
    print_movie_genres(about_me)
    print_movie_titles(about_me['movies'])
    
def print_student_info(data):
    full_name = data['full_name']
    first_name = full_name.split()[0]
    student_id = data['student_id']
    
    print(f"My name is {full_name}, but you can call me {first_name}.")
    print(f"My student ID is {student_id}.")
    print()
    
def add_pizza_toppings(data, toppings):
    data['pizza_toppings'].extend(toppings)
    data['pizza_toppings'].sort()
    data['pizza_toppings'] = [topping.lower() for topping in data['pizza_toppings']]
    
def print_pizza_toppings(data):
    print("My favorite pizza toppings are:")
    for topping in data['pizza_toppings']:
      print(f"- {topping}")
     

def print_movie_genres(data):
        genres = [movie['genre'] for movie in data['movies']]
        print("I like to watch", end=" ")
        for i, genre in enumerate(genres):
            if i == len(genres) - 1:
                print(f"and {genre}", end=" ")
            else:
                print(f"{genre},", end=" ")
        print("movies.")
    

def print_movie_titles(movie_list):
        titles = [movie['title'].title() for movie in movie_list]
        print("Some of my favorite movies are", end=" ")
        for i, title in enumerate(titles):
            if i == len(titles) - 1:
                print(f"and {title}!")
            else:
                print(f"{title},", end=" ")
    

if __name__ == "__main__":
    main()

