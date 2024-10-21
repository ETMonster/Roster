class User:
    def __init__(self, id, first_name, last_name, gender, age, mbti_test, favorite_movies, favorite_music, hobbies):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.mbti_test = mbti_test
        self.favorite_movies = favorite_movies
        self.favorite_music = favorite_music
        self.hobbies = hobbies


users = [
    User(0, 'John', 'Smith', 'Male', 34, 'ESTJ', ['Dune', 'Jumanji', 'Interstellar'], 'Rock', ['Chess', 'Gaming', 'Biking']),
    User(1, 'John', 'Smith', 'Male', 34, 'INTP', ['Dune', 'Jumanji', 'Interstellar'], 'Rock', ['Chess', 'Gaming', 'Biking']),
]

print([vars(user) for user in users])
