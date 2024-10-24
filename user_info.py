class User:
    def __init__(self, id, login_information, first_name, last_name, profile_picture, attributes):
        self.id = id
        self.login_information = login_information
        self.first_name = first_name
        self.last_name = last_name
        self.profile_picture = profile_picture
        self.attributes = attributes

class User_Attributes:
    def __init__(self, gender, age, mbti_test, favorite_movies, favorite_music, hobbies):
        self.gender = gender
        self.age = age
        self.mbti_test = mbti_test
        self.favorite_movies = favorite_movies
        self.favorite_music = favorite_music
        self.hobbies = hobbies

class User_Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

users = []

def new_user(information):
    user = User(len(users), User_Login(information.username, information.password), None, None, None, None)