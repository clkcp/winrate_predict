import numpy as np

class Config():
    def __init__(self):
        #update hero win rate
        self.hero_wr = {}
        with open("../data/heros.txt") as f:
            for line in f:
                (hero_id,_,_,wr) = line.split()
                hero_id = int(hero_id)
                wr = float(wr.strip().rstrip("%"))/100.0
                self.hero_wr.update({hero_id:wr})
        
        # get match up comb
        comb = np.zeros([120,120])
        anti = np.zeros([120,120])
        with open("../data/match_up_comb.txt") as f:
            for line in f:
                a, b, c = line.split()
                a = int(a)
                b = int(b)
                c = float(c)
                comb[a,b] = c
        # get match up anti
        with open("../data/match_up_anti.txt") as f:
            for line in f:
                a, b, c = line.split()
                a = int(a)
                b = int(b)
                c = float(c)
                anti[a,b] = c
        self.comb = comb
        self.anti = anti

        self.model_path = "../data/svm_0.0.2"
    

config = Config()