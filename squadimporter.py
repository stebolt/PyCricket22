import csv

class Player:
    def __init__(self, details=[]):
        name = details[0]
        sname = details[1]
        description = details[2]
        canBowl = details[3]

        print(f'Introducing {name.title()} {sname.title()} the {description}')
        if canBowl == 'True':
            print('Hes ready for a bowl')
        
roster = []
with open('team.csv', 'rt') as file:
    csv_rows = csv.reader(file)
    for row in csv_rows:
        roster.append(Player(row))
