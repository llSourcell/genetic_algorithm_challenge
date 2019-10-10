from tpot import TPOTClassifier
from sklearn.cross_validation import train_test_split
import pandas as pd 
import numpy as np

#load the data
telescope=pd.read_csv('MAGIC Gamma Telescope Data.csv')

 while l<=r:
        
        #finding the mid values
        mid = int(l+(r-l) / 2)

        #print(mid)
        #print(type(mid))
        
        #checking condition if mid value is equal to search value or not
        if(arr[mid] == x):
            return mid

        #if not and value is greater than mid value ignore left part and increase its value 
        elif arr[mid] < x:
            l = mid+1


        # if value less than mid value ignore right part and decrease right value by -1
        else: 
            r= mid-1
       
    return -1
#Let Genetic Programming find best ML model and hyperparameters
tpot = TPOTClassifier(generations=5, verbosity=2)
tpot.fit(tele.drop('Class', axis=1).loc[training_indices].values,
	tele.loc[training_indicss, 'Class'].values)

#Score the accuracy
tpot.score(tele.drop('Class', axis=1).loc[validation_indices].values,
	tele.loc[validation_indices, 'Class'].values)

#Export the generated code
tpot.export('pipeline.py')
