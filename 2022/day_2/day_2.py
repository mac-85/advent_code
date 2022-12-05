def greetings():
    print("*********************************************************")
    print("****** Greetings! We've got your result here below ******")
    print("*********************************************************\n")

points_system = {
    'A' : 1,
    'B' : 2,
    'C' : 3
}
points_scored = {
    'lose': 0,
    'tie': 3,
    'win': 6
}

def my_input():
    # Read from input file
    input = open('day_2_input.txt',"r")
    raw = input.read()            
    matrix = []

    # Match the game code for all the input
    code_translate = {
        'X':'A',
        'Y':'B',
        'Z':'C'
    }
    for key,value in code_translate.items():
        raw = raw.replace(key,value)
    data = raw.split("\n")
    for d in data:                
        matrix.append(d.split(" "))
    return matrix


def p_by_shape(data):
    p_by_shape = data
    result = 0    
    for match in p_by_shape:
       if match[1] in points_system:
           result = result + int(points_system[match[1]])
    return result 

def p_by_score(data):
    p_by_score = data
    result = 0
    for match in p_by_score:
        if match[0] == match[1]:
            result = result + 3
        if (match[1] == 'A' and match[0] == 'C'):
            result = result + 6
        elif (match[1] == 'B' and match[0] == 'A'):
            result = result + 6
        elif (match[1] == 'C' and match[0] == 'B'):
            result = result + 6
    return result

def p_by_game_intention(data):
    p_by_score = data
    result = 0
    for match in p_by_score:        
        if (match[1] == 'A'):            
            if match[0] == 'A':
                result = result + points_system['C']
            if match[0] == 'B':
                result = result + points_system['A']
            if match[0] == 'C':
                result = result + points_system['B']
        elif (match[1] == 'B'):
            result = result + 3 + int(points_system[match[0]])
        elif (match[1] == 'C'):
            result = result + 6
            if match[0] == 'A':
                result = result + points_system['B']
            if match[0] == 'B':
                result = result + points_system['C']
            if match[0] == 'C':
                result = result + points_system['A']
    return result

def main():
    data = my_input()
    greetings()  
    print(f"Total of points by shape selected: {p_by_shape(data)}")
    print(f"Total of points by match result: {p_by_score(data)}")
    print(f"Total points: {p_by_shape(data) + p_by_score(data)}")
    print(f"Total points by game intended score: {p_by_game_intention(data)}")
main()