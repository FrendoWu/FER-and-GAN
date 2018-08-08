# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 23:44:13 2018

@author: t0916126
"""
from hmmlearn2.hmm import GaussianHMM
import numpy as np
from sklearn.externals import joblib
import math
# import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def scoreModels(models, newTestPictures, testLabels, verbose=True):

    results = [i.score(newTestPictures[0], newTestPictures[1]) for i in models]
    outputs = [10*(0.8-((math.exp(-i/100000)/(1+math.exp(-i/100000))))) for i in results]
    answer = {} 
    for i, j in zip(outputs, testLabels):
        answer[i] = j
        if verbose:
            print j, i
    predicted = answer[max(outputs)]
    output = {v: k for k, v in answer.items()}
    return output,answer

def draw_bar(D,real_labels):
    plt.bar(range(len(D)), D.values(), align='center')  
    plt.xticks(range(len(D)), real_labels)



models=[]
testLabels = ['0', '2', '3', '4', '5', '6']
real_labels = ['Angry','Fear','Happy','Sad','Surprise','Neutral']
testPictures=np.random.randint(0,255,[48,48])
newTestPictures=[testPictures, [48]]
for i in range(7):
    if(i!=1):
        name='model-'+str(i)+'.pkl'
        with open(name, 'rb') as f:
            data = joblib.load(f)
            models.append(data)        
        f.close()
SM,SM2=scoreModels(models, newTestPictures, testLabels, verbose=False)
print()
draw_bar(SM,real_labels)