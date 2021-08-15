from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import pickle

data_penguins = pd.read_csv(r'..\data\penguins_cleaned.csv')

df = data_penguins.copy()
##
target = 'species'
encode = ['sex' , 'island']

for col in encode:
    dummy = pd.get_dummies(df[col] , prefix= col)
    df = pd.concat([df,dummy] , axis = 1)
    del df[col]

target_mapper = {'Adelie':0, 'Chinstrap':1, 'Gentoo':2}
def target_encode(val):
    return target_mapper[val]

df['species'] = df['species'].apply(target_encode)

## Separationg X and Y
X = df.drop('species' , axis = 1)
Y = df['species']

clf = RandomForestClassifier()
clf.fit(X,Y)

## Saving the Model
pickle.dump(clf , open('penguins_clf_pkl' ,'wb'))