movies = []


def add_movie():
    movie_title = input('Enter the movie title')
    movie_dir = input('Enter the movie director')
    movie_release_year = input('Enter the movie release year')

    movies.append({
        'title': movie_title,
        'director': movie_dir,
        'release_year': movie_release_year
    })


def show_movies():
    for each_movie in movies:
        print_movie(each_movie)


def print_movie(movie):
    print(f"Movie Title = {movie['title']}")
    print(f"Movie director = {movie['director']}")
    print(f"Movie Release Year = {movie['release_year']}")


def find_movie():
    find_title = input('Enter the movie title you want to find')
    for each_movie in movies:
        if find_title == each_movie['title']:
            print_movie(each_movie)


selections = {
    'a': add_movie,
    's': show_movies,
    'f': find_movie
}

INPUT_STRING = "Please enter 'a' for add movie or 's' for show movies or 'f' for find movie or 'q' for quit"


def menu():
    user_selection = input(INPUT_STRING)
    while user_selection != 'q':
        if user_selection in selections:
            selection = selections[user_selection]

            selection()

        user_selection = input(INPUT_STRING)


menu()




