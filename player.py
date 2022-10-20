import random

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
        DISMISSAL_OPTIONS = ['bowled','caught','lbw','stumped','run out']
        dismissal_choice = random.choices(DISMISSAL_OPTIONS, k=1, weights=[4, 8, 4, 1, 2])
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
