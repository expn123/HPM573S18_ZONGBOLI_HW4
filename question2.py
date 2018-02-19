import numpy as np

class Game:
    def __init__(self,id):
        self.id=id
        self.rnd=np.random
        self.rnd.seed(self.id)
        self.rarray = np.random.random(size=20)
        self.game_list = list(self.rarray)
    def simulation(self):
        for k in range(0, 20):
            if self.rarray[k] > 0.6:
                self.game_list[k] = 'H'
            else:
                self.game_list[k] = 'T'
        m = 0
        for j in range(0, len(self.game_list) - 2):
            if self.game_list[j] == 'T' and self.game_list[j + 1] == 'T' and self.game_list[j + 2] == 'H':
                m += 1
                j = j + 3
            else:
                m += 0
                j = j + 1
        total_result = 100 * m - 250
        return total_result

class Cohort:
    def __init__(self,id,pop_size):

        self.gamelist=[]
        self.catotal_score=[]
        n=1
        while n<=pop_size:
            gameunit=Game(id*pop_size+n)
            self.gamelist.append(gameunit)
            n+=1

    def simulatecohort(self):
        for game in self.gamelist:
            value=game.simulation()
            self.catotal_score.append(value)

    def get_expected_score(self):
        return sum(self.catotal_score)/len(self.catotal_score)


cohorttest=Cohort(1,1000)
cohorttest.simulatecohort()
print("The expected score is",cohorttest.get_expected_score())
