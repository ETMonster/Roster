class mbti:
    def __init__(self, matrix, matrix_indices):
        self.matrix = matrix
        self.matrix_indices = matrix_indices

mbti_compatability = mbti([
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
], {
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
})