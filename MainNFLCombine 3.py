import numpy as np
import pandas as pd
from sklearn import neighbors, tree, model_selection
#from sklearn import model_selection
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO
import graphviz
from sklearn import linear_model #import LogisticRegression
 #import KNeighborsClassifier
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import Imputer

#function to delete column from data
def drop_col_n(df, col_n_to_drop):
    col_dict = {x: col for x, col in enumerate(df.columns)}
    return df.drop(col_dict[col_n_to_drop], 1)


#path = '/Users/corpa/Documents/classes/machinelearning/Projects/Combine/NFLData/'
path = '/Users/leeh7/Documents/PythonFiles/NFLML/'
#paths to the main .csv files
wrFile = path + 'draftWRData.csv'
rbFile = path + 'draftRBData.csv'
#qbFile = path + 'draftQBData.csv'
qbFile = path + 'draftQBData.csv'

def createCleanFilePath(path):
    return path[:-4]+"Clean"+path[-4:]

#function to read each file and parse it into a numpy matrix
def readFile(draftFile):
    #pandas read csv file where the headers are at index 0
    df = pd.read_csv(draftFile, header=0)

    # TO GET RID OF THAT NUMBERED COLUMN
    #df = drop_col_n(df, 0)
    df.drop(df.columns[[0]], axis=1, inplace=True)

    # saves the class column, take the Draft Round Out
    classColumn = df.T.iloc[-1]
    #df = drop_col_n(df, 8)
    df.drop(df.columns[[8]], axis=1, inplace=True)

    #headers row into a list
    original_headers = list(df.columns.values)

    #fill NaN values as 0
    #df = df.fillna(0)

    # create cleaned csv data
    #df.to_csv(createCleanFilePath(draftFile), index=False)

    #parse all numeric data (get rid of strings)
    df = df._get_numeric_data()

    #parse the numeric data as numpy matrix
    dfNumPyArray = df.as_matrix()

    #use the imputer to convert all NaN to the mean of the column
    imp = Imputer(missing_values=np.nan, strategy='mean', axis=0)
    imp.fit(dfNumPyArray)

    # MAY CAUSE PROBLEMS/ uses average from column
    # make the dfNumPyArray be this new imputed array
    dfNumPyArray = imp.transform(dfNumPyArray)

    #make the classes (round picks) into a matrix (row)
    classNumPyArray = classColumn.as_matrix()



    #return all 3 for use
    return [dfNumPyArray, classNumPyArray, original_headers]



def compareClassifiers(draftFile1):
    x = 0

    models = []
    models.append(('LR', linear_model.LogisticRegression()))
    models.append(('KNN', neighbors.KNeighborsClassifier()))
    models.append(('CART', tree.DecisionTreeClassifier()))


    numpyData1 = readFile(draftFile1)
    data1Train,data1Test = train_test_split(numpyData1[0], test_size=0.33, random_state=42)

    seed = 6
    #evaluate each model
    results = []
    names = []
    scoring = 'accuracy'
    for name, model in models:
        kfold = model_selection.KFold(n_splits=10, random_state=seed)
        cv_results = model_selection.cross_val_score(model, data1Test,data1Train , cv=kfold, scoring=scoring)
        results.append(cv_results)
        names.append(name)
        msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
        print(msg)



#given a draft file, create a decision  tree
def decisionTree(draftFile):

    #read the data

    numpyData = readFile(draftFile)

    #new Decision Tree
    decisionT = tree.DecisionTreeClassifier()

    #create a tree with the data (x = all of the data without the round pick, y = the round pick)
    #[0] = without class column
    #[1] = class column
    decisionT.fit(numpyData[0], numpyData[1])
    #print(decisionT)

    #sort the importance of features and print the dictionary accordingly.
    dictionary = dict(zip(numpyData[2], decisionT.feature_importances_))
    dictionary = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    for entry in dictionary:
        print(entry)
    print("---")
    #print(dictionary)



    return decisionT




#create a KNeighborsClassifier with given file draftFileData
def kNN(draftFile):
    #read the data
    numpyData = readFile(draftFile)

    #use 5 AT THE MOMENT nearest neighbors (k)
    n_neighbors = 5

    #create the model
    neighModel = neighbors.KNeighborsClassifier(n_neighbors)

    #fit the data to the model
    # [0] = without class column
    # [1] = class column
    neighModel.fit(numpyData[0], numpyData[1])

    #print(neighModel)
    return neighModel


def predictKNN(knnModel, rowData):
    return knnModel.predict([rowData])

#dfWR =
#dfRB =
#dfQB =


#read all three files
wrDataValues = readFile(wrFile)
rbDataValues = readFile(rbFile)
qbDataValues = readFile(qbFile)

#full data_set ... rough
data_set = pd.DataFrame(wrDataValues).append(pd.DataFrame(rbDataValues)).append(pd.DataFrame(qbDataValues))

#print(data_set.head(10))
kNN(wrFile)
decisionTree(wrFile)
decisionTree(rbFile)
decisionTree(qbFile)

#print(pd.DataFrame(wrDataValues))
#print(data_set.head(10))

#    1 model to be trained... split between train and test
