
import pandas as pd
from scipy import stats
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt
import numpy as np


#os.chdir("D:/")

#base  = pd.read_csv("b.csv")

def ks(test,pred):
    data =  pd.DataFrame({'bad':test, 'score':pred})
    data['good'] = 1 - data.bad
    rv1=data[data['bad']==1]['score']
    rv2=data[data['bad']==0]['score']
    return stats.ks_2samp(rv1, rv2)
     
#base.loc[base.PD_12M == 1, 'PD_12M'] = 3
#base.loc[base.PD_12M == 0, 'PD_12M'] = 1
#base.loc[base.PD_12M == 3, 'PD_12M'] = 0



def gini(test,pred,plot=False):
    
    
    logit_roc_auc_train = roc_auc_score(test, pred)
#fpr, tpr, thresholds = roc_curve(y_validation, logisticRegr.predict_proba(x_validation)[:,1])
    if plot:
        fpr, tpr, thresholds = roc_curve(test, pred)
        plt.figure()
        plt.plot(fpr, tpr, label='Logistic Regression (area = %0.2f)' % logit_roc_auc_train)
        plt.plot(fpr, tpr)
        plt.plot([0, 1], [0, 1],'r--')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('Receiver operating characteristic TRAIN')
        plt.legend(loc="lower right")
        plt.savefig('Log_ROC_train')
        plt.show()
        
    return logit_roc_auc_train,logit_roc_auc_train*2-1


def Find_Optimal_Cutoff(test, pred):
    """ Find the optimal probability cutoff point for a classification model related to event rate
    Parameters
    ----------
    target : Matrix with dependent or target data, where rows are observations

    predicted : Matrix with predicted data, where rows are observations

    Returns
    -------     
    list type, with optimal cutoff value

    """
    fpr, tpr, threshold = roc_curve(test, pred)
    i = np.arange(len(tpr)) 
    roc = pd.DataFrame({'tf' : pd.Series(tpr-(1-fpr), index=i), 'threshold' : pd.Series(threshold, index=i)})
    roc_t = roc.ix[(roc.tf-0).abs().argsort()[:1]]

    return list(roc_t['threshold']) 


