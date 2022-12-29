#!python3

def calculate_BASE_COCOMO(filePath):
    M = 0
    Td = 0
    LOC = 0
    difficulty = ""

    difficulty_values = {
        "easy": [2.4, 1.05, 2.5, 0.38],
        "intermediate": [3, 1.12, 2.5, 0.35],
        "hard": [3.6, 1.12, 2.5, 0.32]
    }

    with open(filePath, 'r') as f:
        LOC = len(f.readlines())

    a = 0
    b = 0
    c = 0
    d = 0
    difficulty = ""
    if (LOC < 3000):
        difficulty = "easy"
    elif (LOC >= 3000 and LOC < 10000):
        difficulty = "intermediate"
    else:
        difficulty = "hard"

    a = difficulty_values[difficulty][0]
    b = difficulty_values[difficulty][1]
    c = difficulty_values[difficulty][2]
    d = difficulty_values[difficulty][3]

    M = a * ((LOC / 1000)**b)
    Td = c * (M ** d)
    M = round(M, 2)
    Td = round(Td, 2)

    return {
        "LOC": LOC,
        "difficulty": difficulty,
        "Months man(hours)": M,
        "Development time(months)": Td
    }
