from matplotlib import pyplot as plt
import pandas as pd
import numpy  as np
import math
import pandas.tools.rplot as rplot


def print_outframe(lm, col_list):

    temp = []
    cols = ['intercept']

    temp.append(lm.intercept_)

    for num in lm.coef_:
        temp.append(num)
    
    
    for col in col_list:
        cols.append(col)
    
    out_frame = pd.DataFrame([cols, temp]).transpose()

    print (out_frame)
                 
               

def scat_rplot(Bdat1, col_list):

  
  for col in col_list:
       
    if(Bdat1[col].dtype in [np.int64, np.int32, np.float64]): 
         
        fig = plt.figure(figsize = (12,6)) 

        fig.clf() 
        ax = fig.gca() 
        plot = rplot.RPlot(Bdat1, x = col, y = 'cnt') 
        plot.add(rplot.GeomScatter()) 
        plot.add(rplot.GeomPolyFit(degree=2)) 
        plt.xlabel(col) 
        plt.ylabel('cnt') 
        plot.render(plt.gcf())  
        plt.show()
        fig.savefig('./figures/sscatter' + col)
        plt.close() 

  
def plot_outframe(lm, X, name):
    
    imp = lm.coef_
    names = X.columns

    imp, names = zip(*sorted(zip(imp,names)))

    fig = plt.figure(1, figsize=(10, 10))
    
    plt.barh(np.arange(len(names)), imp, align='center')
    plt.yticks(np.arange(len(names)),names)
    plt.xlabel('Importances of features')
    plt.ylabel('Features')
    plt.title('Importance of each feature ('+name+')')
    plt.show()

    fig.savefig('./figures/'+name[0:5]+'_feat_imp')
    plt.close()     
    
def plot_outframe2(rfr, X, pnum):
    
    imp = rfr.feature_importances_
    names = X.columns

    imp, names = zip(*sorted(zip(imp,names)))

    fig = plt.figure(1, figsize=(10, 10))
    
    plt.barh(np.arange(len(names)), imp, align='center')
    plt.yticks(np.arange(len(names)),names)
    plt.xlabel('Importances of features')
    plt.ylabel('Features')
    plt.title('Importance of each feature (Random Forest Regressor)')
    plt.show()

    fig.savefig('./figures/rfr_feat_imp'+pnum) 
    plt.close() 