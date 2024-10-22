<<<<<<< HEAD
from tkinter import *
from user_info import User, users

mbti_matrix_value = {
    'INFP': 0,
    'ENFP': 1,
    'INFJ': 2,
    'ENFJ': 3,
    'INTJ': 4,
    'ENTJ': 5,
    'INTP': 6,
    'ENTP': 7,
    'ISFP': 8,
    'ESFP': 9,
    'ISTP': 10,
    'ESTP': 11,
    'ISFJ': 12,
    'ESFJ': 13,
    'ISTJ': 14,
    'ESTJ': 15
}

mbti_compatibility_matrix = [
    [3, 3, 3, 4, 3, 4, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0],  # INFP
    [3, 3, 4, 3, 4, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0],  # ENFP
    [3, 4, 3, 3, 3, 3, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0],  # INFJ
    [4, 3, 3, 3, 3, 3, 3, 3, 4, 0, 0, 0, 0, 0, 0, 0],  # ENFJ
    [3, 4, 3, 3, 3, 3, 3, 4, 2, 2, 2, 2, 1, 1, 1, 1],  # INTJ
    [4, 3, 3, 3, 3, 3, 4, 3, 2, 2, 2, 2, 2, 2, 2, 2],  # ENTJ
    [3, 3, 3, 3, 3, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 4],  # INTP
    [3, 3, 4, 3, 4, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1],  # ENTP
    [0, 0, 0, 4, 2, 2, 2, 2, 1, 1, 1, 1, 2, 4, 2, 4],  # ISFP
    [0, 0, 0, 0, 2, 2, 2, 2, 1, 1, 1, 1, 4, 2, 4, 2],  # ESFP
    [0, 0, 0, 0, 2, 2, 2, 2, 1, 1, 1, 1, 2, 4, 2, 4],  # ISTP
    [0, 0, 0, 0, 2, 2, 2, 2, 1, 1, 1, 1, 4, 2, 4, 2],  # ESTP
    [0, 0, 0, 0, 1, 2, 1, 1, 2, 4, 2, 4, 3, 3, 3, 3],  # ISFJ
    [0, 0, 0, 0, 1, 2, 1, 1, 4, 2, 4, 2, 3, 3, 3, 3],  # ESFJ
    [0, 0, 0, 0, 1, 2, 1, 1, 2, 4, 2, 4, 3, 3, 3, 3],  # ISTJ
    [0, 0, 0, 0, 1, 2, 4, 1, 4, 2, 4, 2, 3, 3, 3, 3]  # ESTJ
]

for x in mbti_compatibility_matrix:
    for y in x:
        print(('\033[31m' if y == 0 else '\033[33m' if y == 1 else '\033[92m' if y == 2 else
                     '\033[32m' if y == 3 else '\033[34m' if y == 4 else '\033[0m') + '# ', end = '')
    print('')

def get_compatibility(userA, userB):
    print(mbti_compatibility_matrix[mbti_matrix_value[userA.mbti_test]][mbti_matrix_value[userB.mbti_test]])

get_compatibility(users[0], users[1])
=======
from pages.start_window import *

start_window.mainloop()
>>>>>>> d8181a7 (Initial commit)
