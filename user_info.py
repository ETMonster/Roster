import json

class User:
    def __init__(self, id, first_name, last_name, profile_picture_path, login_information, compatability_attributes):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.profile_picture_path = profile_picture_path
        self.login_information = login_information
        self.compatability_attributes = compatability_attributes

    def to_dictionary(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "profile_picture_path": self.profile_picture_path,
            "login_information": self.login_information.to_dictionary() if self.login_information is not None else None,
            "compatability_attributes": self.compatability_attributes.to_dictionary() if self.compatability_attributes is not None else None
        }

class User_Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def to_dictionary(self):
        return {
            "username": self.username,
            "password": self.password
        }

    def to_object(self, dictionary):
        self.username = dictionary["username"]
        self.password = dictionary["password"]

class User_Attributes:
    def __init__(self, gender, preferred_gender, age, mbti_test, favorite_music, favorite_movie, hobby):
        self.gender = gender
        self.preferred_gender = preferred_gender
        self.age = age
        self.mbti_test = mbti_test
        self.favorite_music = favorite_music
        self.favorite_movie = favorite_movie
        self.hobby = hobby

    def to_dictionary(self):
        return {
            "gender": self.gender,
            "preferred_gender": self.preferred_gender,
            "age": self.age,
            "mbti_test": self.mbti_test,
            "favorite_music": self.favorite_music,
            "favorite_movie": self.favorite_movie,
            "hobby": self.hobby
        }

    def to_object(self, dictionary):
        self.gender = dictionary["gender"]
        self.preferred_gender = dictionary["preferred_gender"]
        self.age = dictionary["age"]
        self.mbti_test = dictionary["mbti_test"]
        self.favorite_music = dictionary["favorite_music"]
        self.favorite_movie = dictionary["favorite_movie"]
        self.hobby = dictionary["hobby"]

users = []
current_user = None

def get_user_from_id(user_id):
    for user in users:
        if user.id == user_id:
            return user

def load_users():
    global users

    with open('user_info.json', 'r') as file:
        file = file.read()
        user_data = json.loads(file.strip())

        for user in user_data:
            login_info = User_Login(
                user["login_information"]["username"],
                user["login_information"]["password"]
            )
            attributes = User_Attributes(
                user["compatability_attributes"]["gender"],
                user["compatability_attributes"]["preferred_gender"],
                user["compatability_attributes"]["age"],
                user["compatability_attributes"]["mbti_test"],
                user["compatability_attributes"]["favorite_music"],
                user["compatability_attributes"]["favorite_movie"],
                user["compatability_attributes"]["hobby"]
            )
            user = User(
                int(user["id"]),
                user["first_name"],
                user["last_name"],
                user["profile_picture_path"],
                login_info,
                attributes
            )

            users.append(user)

def write_users():
    user_data_dictionary = [user.to_dictionary() for user in users]

    with open('user_info.json', 'w') as file:
        json.dump(user_data_dictionary, file, indent = 2)

def login(user):
    global current_user

    print(f'Logged in to user {user.id}')
    current_user = user

def signup(user_login):
    global users
    global current_user

    def get_new_user_id(possible_id = 0):
        for user in users:
            if user.id == possible_id:
                possible_id += 1
                get_new_user_id(possible_id)

        return possible_id

    new_user = User(get_new_user_id(), None, None, None, user_login, User_Attributes(None, None, None, None, None, None, None))

    users.append(new_user)
    login(new_user)

    write_users()