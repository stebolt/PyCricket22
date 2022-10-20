import random
from tabulate import tabulate

class Team:
    """ A simple representation of a team """

    def __init__(self, team_name, team_squad):
        self.name = team_name
        self.squad = []
#        self.score = 0
        self.oversFaced = 0
        self.stillIn = True

        for player in team_squad:
            self.squad.append(Player(player))         

        self.onStrike = self.squad[0]
        self.battingPartner = self.squad[1]

    def faceAnOver(self):
        global scorecard
#        overScore = 0
        # First rotate the batsmen at the start of the over.
        # In an over - as long as the team isn't all out...
        # ... Play a shot, and set rotation to true if 1 or 3 is scored.
        # Check whether the on strike batsman was dismissed and the over wickets count isn't 10.
        # ... and bring in the next bastman.
        # Otherwise if they need to rotate, do it.
        self.rotateTheStrike()
        for delivery in range(6):
            if self.calculateLostWickets() < 10:
                rotate_the_strike = self.onStrike.playAShot()
            if self.onStrike.dismissed and self.calculateLostWickets() < 10:
                self.bringInTheNextBatsman()
            if rotate_the_strike:
                self.rotateTheStrike()
        scorecard += '|'
        self.oversFaced += 1
#        print('Score in that over was ' + str(overScore))

    def rotateTheStrike(self):
        (self.onStrike, self.battingPartner) = (self.battingPartner, self.onStrike)


    def bringInTheNextBatsman(self):
        self.onStrike = self.squad[self.calculateLostWickets() + 1]


    def calculateScore(self):
        runs = 0
        for j in self.squad:
            runs += j.score
        return runs

    def calculateLostWickets(self):
        wicketsLost = 0
        for j in self.squad:
            if j.dismissed:
                wicketsLost += 1
        return wicketsLost



class Player:
    """A representation of one of the players"""

    def __init__(self, player_name):
        self.name = player_name
        self.score = 0
        self.dismissed = False
        self.dismissal = ''

    def scoringWithWeights(self):
        scoring_options = [0, 1, 2, 3, 4, 6, 9]
        score = random.choices(scoring_options, k=1, weights=[8, 6, 4, 2, 4, 1, 1])
        return score[0]

    def owzat(self):
        dismissal_options = ['bowled','caught','lbw','stumped','run out']
        dismissal_choice = random.choices(dismissal_options, k=1, weights=[4, 8, 4, 1, 2])
        print('Owzat! Wicket! ' + self.name + ' is out ' + dismissal_choice[0].lower())
        return dismissal_choice[0]

    def playAShot(self):
        global scorecard
        number = self.scoringWithWeights()
        rotate = False
        if number == 9:
            self.dismissal = self.owzat()
            self.dismissed = True
            scorecard += 'W'
        else:
            self.score += number
            if number == 1 or number == 3:
                rotate = True
            if number == 0:
                scorecard += '-'
            else:
                scorecard += str(number)
#        print('Score: ' + str(number) + '\tRotate: ' + str(rotate))
        return rotate

# GLOBAL DEFS
def printScorecard(teamToBat):
#    print(scorecard)
    print(f'{teamToBat.calculateScore()}/{teamToBat.calculateLostWickets()}')
    print('After ' + str(teamToBat.oversFaced) + ' overs')
    print()

def printIntro():
    print('Welcome to Python cricket, here comes the first over')


def coinToss(a, b):
    teams = [a, b]
    random.shuffle(teams)
    return teams[0], teams[1]

def printNewScorecard(team):
    print(team.name + '\n------------------')
    for j in team.squad:
        print("{:15} {:15} {:<10}".format(j.name, j.dismissal, str(j.score)))
    print(f"\n\tOvers: {team.oversFaced}\t\t{teamToBat.calculateScore()}/{teamToBat.calculateLostWickets()}\n")

def import_squad_list(file):
    with open(file) as f:
        return [line.rstrip() for line in f]

def playAnInnings(teamToBat):
    while teamToBat.calculateLostWickets() < 10 and teamToBat.oversFaced < 20:
        teamToBat.faceAnOver()
        printScorecard(teamToBat)
    printNewScorecard(teamToBat)

while True:
    # Build the squad lists
    england = Team('England', import_squad_list('squads/england.txt'))
    australia = Team('Australia', import_squad_list('squads/australia.txt'))
    
    # Create a scorecard for the ball by ball view
    scorecard = ''

    #Introduce the game
    printIntro()
    
    print('England line up:\n--------------')
    for i in england.squad:
        print(i.name)
    
    print('Australia line up:\n--------------')
    for i in australia.squad:
        print(i.name)

    teamToBat, teamToBowl = coinToss(england, australia)
    print(teamToBat.name + ' to bat first. ' + teamToBowl.name + ' will bowl.')

    playAnInnings(teamToBat)
    teamToBat = teamToBowl
    playAnInnings(teamToBowl)

    print('Game over')
    break