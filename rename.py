import os
import sys

import user_info

user_info.load_users()

for file, user in zip(os.listdir('images/profiles'), [x for x in user_info.users if x.compatability_attributes.gender == 'Female']):
    if not file.startswith('Face'):
        continue

    print(user.id, user.login_information.username)
    os.rename(os.path.join('images/profiles', file), os.path.join('images/profiles', user.login_information.username + '.jpeg'))