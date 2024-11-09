def alphabetical_value(name):
    #Calculate the alphabetical value of a name
    return sum(ord(char) - ord('A') + 1 for char in name)

def calculate_name_score(filename):
    with open(filename, 'r') as f:
        # Read the names from the file and remove quotes and newlines
        names = f.read().replace('"', '').split(',')

    # Sort the names alphabetically
    names.sort()

    # Calculate the name score for each name and sum them
    total_score = 0
    for i, name in enumerate(names, start=1):
        name_value = alphabetical_value(name)
        total_score += i * name_value
    
    return total_score

file = 'names.txt'
total_score = calculate_name_score(file)

print(f'Score is {total_score}') # 871198282