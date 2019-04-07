import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import io

#AndhraPradesh
import os
def check_2011(maps,string, year):
        print(maps)
        print(string)
        print(year)
        if(year=='2011'):
            dataset=pd.read_csv("F:/222/2011data/2011AllDiseases/"+string+"malaria2011.csv")
            dataset=dataset.pivot(" Number of Cases","Disease"," Number of Deaths")
            plt.figure(figsize=(7,4),dpi=100)
            if maps=='heatmap':
                    display=sns.heatmap(dataset,annot=True,fmt='f')
                    plt.title(string)
                    plt.show()
            else:
                dataset1=pd.read_csv("F:/222/2011data/2011AllDiseases/"+string+"malaria2011.csv")
                labels=tuple(dataset1.iloc[:,0].values)
                sizes=list(dataset1.iloc[:,1].values)
                explode=[0,0,0,0,0]
                plt.pie(sizes,labels=labels,explode=explode,autopct="%1.1f%%",shadow=True,startangle=90)
                plt.axis('equal')
                plt.legend(labels,loc="best")
                plt.show()
        elif(year=='2012'):
            dataset=pd.read_csv("F:/222/2011data/2012AllDiseases/"+string+"AllDiseases2012.csv")
            dataset=dataset.pivot(" Number of Cases","Disease"," Number of Deaths")
            plt.figure(figsize=(7,4),dpi=100)
            if maps=='heatmap':
                display=sns.heatmap(dataset,annot=True,fmt='f')
                plt.title(string)
                plt.show()
            else:
                dataset1=pd.read_csv("F:/222/2011data/2012AllDiseases/"+string+"AllDiseases2012.csv")
                labels=tuple(dataset1.iloc[:,0].values)
                sizes=list(dataset1.iloc[:,1].values)
                sizes
                explode=[0,0,0,0,0]
                plt.pie(sizes,labels=labels,explode=explode,autopct="%1.1f%%",shadow=True,startangle=90)
                plt.axis('equal')
                plt.legend(labels,loc="best")
                plt.show()
        elif(year=='2013'):
            dataset=pd.read_csv("F:/222/2011data/2013AllDiseases/"+string+"AllDiseases2013.csv")
            dataset=dataset.pivot(" Number of Cases","Disease"," Number of Deaths")
            plt.figure(figsize=(7,4),dpi=100)
            if maps=='heatmap':
                display=sns.heatmap(dataset,annot=True,fmt='f')
                plt.title(string)
                plt.show()
            else:
                dataset1 = pd.read_csv("F:/222/2011data/2013AllDiseases/"+string+"AllDiseases2013.csv")
                labels=tuple(dataset1.iloc[:,0].values)
                sizes=list(dataset1.iloc[:,1].values)
                sizes
                explode=[0,0,0,0,0]
                plt.pie(sizes,labels=labels,explode=explode,autopct="%1.1f%%",shadow=True,startangle=90)
                plt.axis('equal')
                plt.legend(labels,loc="best")
                plt.show()
        elif(year=='2014'):
            dataset=pd.read_csv("F:/222/2011data/2014AllDiseases/"+string+"AllDiseases2014.csv")
            dataset=dataset.pivot(" Number of Cases","Disease"," Number of Deaths")
            plt.figure(figsize=(7,4),dpi=100)
            if maps=='heatmap':
                display=sns.heatmap(dataset,annot=True,fmt='f')
                plt.title(string)
                plt.show()
            else:
                dataset1 = pd.read_csv("F:/222/2011data/2014AllDiseases/"+string+"AllDiseases2014.csv")
                labels=tuple(dataset1.iloc[:,0].values)
                sizes=list(dataset1.iloc[:,1].values)
                sizes
                explode=[0,0,0,0,0]
                plt.pie(sizes,labels=labels,explode=explode,autopct="%1.1f%%",shadow=True,startangle=90)
                plt.axis('equal')
                plt.legend(labels,loc="best")
                plt.show()
        elif(year=='2015'):
            dataset=pd.read_csv("F:/222/2011data/2015AllDiseases/"+string+"AllDiseases2015.csv")
            dataset=dataset.pivot(" Number of Cases","Disease"," Number of Deaths")
            plt.figure(figsize=(7,4),dpi=100)
            if maps=='heatmap':
                display=sns.heatmap(dataset,annot=True,fmt='f')
                plt.title(string)
                plt.show()
            else:
                dataset1 = pd.read_csv("F:/222/2011data/2015AllDiseases/"+string+"AllDiseases2015.csv")
                labels=tuple(dataset1.iloc[:,0].values)
                sizes=list(dataset1.iloc[:,1].values)
                sizes
                explode=[0,0,0,0,0]
                plt.pie(sizes,labels=labels,explode=explode,autopct="%1.1f%%",shadow=True,startangle=90)
                plt.axis('equal')
                plt.legend(labels,loc="best")
                plt.show()

