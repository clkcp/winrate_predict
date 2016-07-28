import json
import re
import numpy as np
import scipy as sp
import pickle
from sklearn import cross_validation
from sklearn import svm
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from config import config
import copy

class PredictModel():
    def ca(self, a, b):
        res = []
        for i in a:
            for j in a:
                if not i == j:
                    res.append(config.comb[i,j])
            for j in b:
                res.append(config.anti[i,j])
        res = np.array(res)
        return res

    def get_feature(self, heros):
        team0 = heros["A"]
        team1 = heros["B"]
        count = 0
        teams = np.zeros([2,120], dtype=np.float)
        wr = np.zeros([2, 5], dtype=np.float)
        for i in team0:
            teams[0][i] = 1.0
            wr[0][count] = config.hero_wr[i]
            count+=1
        count = 0
        for i in team1:
            teams[1][i] = 1.0
            wr[1][count] = config.hero_wr[i]
            count+=1

        p = np.zeros([2,45])
        p[0] = self.ca(team0, team1)
        p[1] = self.ca(team1, team0)
        ret = np.hstack([teams, wr, p]).reshape([1, -1])
        return ret

    def predict(self, heros):
        ## hard code here
        ## need a predict model
        feat = self.get_feature(heros)
        clf = copy.deepcopy(config.clf)
        pre = clf.predict_proba(feat.reshape(1, -1))
        return pre[0][1]


if __name__ == "__main__":
    predictor = PredictModel()
    heros = {"A":[1,2,3,4,5], "B":[7,8,9,10,11]}
    print "ans" , predictor.predict(heros)