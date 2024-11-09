import user_info

class MBTI:
    matrix = [
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
        [0, 0, 0, 0, 1, 2, 4, 1, 4, 2, 4, 2, 3, 3, 3, 3],  # ESTJ
    ]
    matrix_indices = {
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
        'ESTJ': 15,
    }

    @staticmethod
    def get_matrix(personality, compare_personality):
        return MBTI.matrix[MBTI.matrix_indices[personality]][MBTI.matrix_indices[compare_personality]]

def get_compatability(user, compare_user):
    compatability_score = 0

    # Gender
    if (compare_user.compatability_attributes.preferred_gender == 'All' or
    compare_user.compatability_attributes.preferred_gender == user.compatability_attributes.gender):
        compatability_score += 5

    if user.compatability_attributes.preferred_gender == compare_user.compatability_attributes.gender:
        compatability_score += 5

    if user.compatability_attributes.gender == 'Other' or compare_user.compatability_attributes.gender == 'Other':
        compatability_score += 3

    # Age
    compatability_score += 8 - abs(int(user.compatability_attributes.age) - int(compare_user.compatability_attributes.age))

    # MBTI personality test
    compatability_score += MBTI.get_matrix(user.compatability_attributes.mbti_test, compare_user.compatability_attributes.mbti_test) * 2

    # Favorites
    if user.compatability_attributes.favorite_music == compare_user.compatability_attributes.favorite_music:
        compatability_score += 4
    if user.compatability_attributes.favorite_movie == compare_user.compatability_attributes.favorite_movie:
        compatability_score += 4
    if user.compatability_attributes.hobby == compare_user.compatability_attributes.hobby:
        compatability_score += 4

    return compatability_score

def find_matches(user):
    class User_Score:
        def __init__(self, user_id, score):
            self.user_id = user_id
            self.compatability_score = score

    compatability_scores = []

    for compare_user in user_info.users:
        if user.id == compare_user.id:
            continue

        compatability_score = get_compatability(user, compare_user)
        compatability_scores.append(User_Score(compare_user.id, compatability_score))

    compatability_scores = sorted(compatability_scores, key = lambda obj: obj.compatability_score, reverse = True)

    for x in compatability_scores:
        print(x.user_id, x.compatability_score)

    return compatability_scores