class User:
    def __init__(self, id, login_information, first_name, last_name, profile_picture_path, compatability_attributes):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.profile_picture_path = profile_picture_path
        self.login_information = login_information
        self.compatability_attributes = compatability_attributes

class User_Attributes:
    def __init__(self, gender, age, mbti_test, favorite_movies, favorite_music, hobbies):
        self.gender = gender
        self.age = age
        self.mbti_test = mbti_test
        self.favorite_music = favorite_music
        self.favorite_movies = favorite_movies
        self.hobbies = hobbies

class User_Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

users = []
current_user = None

brackets = {
    '(': [')', type(User_Login)],
    '{': ['}', type(User_Attributes)],
    '[': [']', type(list)]
}

def load_users():
    global users

    with open('user_info.txt', 'r') as users_file:
        users_file = users_file.readlines()

        for user in users_file:
            new_user = User(None, None, None, None, None, None)

            class_to_variable_transposition = {
                type(User_Login): new_user.login_information,
                type(User_Attributes): new_user.compatability_attributes
            }

            for i, x in enumerate(user):
                if x not in brackets:
                    continue

                for j, y in enumerate(user[i:]):
                    if y == brackets[x][0]:
                        attribute_list = user[i + 1:i + j].split(',')
                        print(attribute_list)
                        print(class_to_variable_transposition[brackets[x][1]])
                        print(brackets[x][1])
                        class_to_variable_transposition[brackets[x][1]] = brackets[x][1](attribute_list)

            print(vars(new_user))

        #for user in users:
            #print(user.vars())


def login(user_id):
    global current_user

    user_id = int(user_id)

    print(f'Logged in to user {user_id}')
    current_user = users[user_id]

def create_new_user(information):
    user = User(len(users), User_Login(information.username, information.password), None, None, None, None)