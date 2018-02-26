from tpot import TPOTClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

""" MAGIC Gamma Telescope Data Set """
""" https://archive.ics.uci.edu/ml/datasets/magic+gamma+telescope """

# load data
telescope = pd.read_csv('MAGIC Gamma Telescope Data.csv')
# clean data
telescope_shuffle = telescope.iloc[np.random.permutation(len(telescope))] # pylint: disable=E1101
tele = telescope_shuffle.reset_index(drop=True)
# store two classes
tele['class'] = tele['class'].map({'g': 0, 'h': 1})
tele_class = tele['class'].values
# split training, testing, and validation data
training_indices, validation_indices = training_indices, testing_indices = train_test_split(tele.index, stratify=tele_class, train_size=0.75, test_size=0.25)
# use genetic programming to find best ML model and hyperparameters
tpot = TPOTClassifier(generations=5, verbosity=2)
tpot.fit(tele.drop('class', axis=1).loc[training_indices].values, tele.loc[training_indices, 'class'].values)
# score the accuracy
tpot.score(tele.drop('class', axis=1).loc[validation_indices].values, tele.loc[validation_indices, 'class'].values)
# export generated code
tpot.export('pipeline.py')
