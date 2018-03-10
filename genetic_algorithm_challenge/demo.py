"""
MAGIC Gamma Telescope Data Set
(https://archive.ics.uci.edu/ml/datasets/magic+gamma+telescope)
"""
from numpy                   import random           as np_random
from pandas                  import read_csv         as pd_read_csv
from sklearn.model_selection import train_test_split
from tpot                    import TPOTClassifier


def main():
    # load data
    telescope = pd_read_csv('MAGIC Gamma Telescope Data.csv')
    # clean data
    telescope_shuffle = telescope.iloc[np_random.permutation(len(telescope))]                      # pylint: disable=E1101
    tele = telescope_shuffle.reset_index(drop=True)
    # store two classes
    tele['class'] = tele['class'].map({'g': 0, 'h': 1})
    tele_class = tele['class'].values
    # split training, testing, and validation data
    training_indices, validation_indices = training_indices, _ = train_test_split(tele.index,
                                                                                 stratify=tele_class,
                                                                                 train_size=0.75,
                                                                                 test_size=0.25)
    # use genetic programming to find best ML model and hyperparameters
    tpot = TPOTClassifier(generations=5, verbosity=2)
    tpot.fit(tele.drop('class', axis=1).loc[training_indices].values, tele.loc[training_indices, 'class'].values)
    # score the accuracy
    tpot.score(tele.drop('class', axis=1).loc[validation_indices].values, tele.loc[validation_indices, 'class'].values)
    # export generated code
    tpot.export('pipeline.py')


if __name__ == "__main__":
    main()
