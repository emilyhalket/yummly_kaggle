__author__ = 'esievers'

#starting w. scripts posted on kaggle website to get a feel


#start w. script from Manuel looking @ 10 most used ingredients
import pandas as pd
import matplotlib.pyplot as plt
from nltk.stem import WordNetLemmatizer
from collections import Counter


train = pd.read_json('./train.json')
stemmer = WordNetLemmatizer()

def clean_recipe(recipe):
    #make the recipe in lowercase
    recipe = [str.lower(i) for i in recipe]
    # list comprehension form of for loop


    #take out special characters
    # you can "chain" replace statements
    def replacing(i):
        i = i.replace('&', '').replace('(', '').replace(")",'')
        i = i.replace("\'", '').replace('\\', '').replace(',','')
        i = i.replace('.','').replace('%', '').replace('/','')
        i = i.replace('"','')
        return i

    #use function replacing to replace unwanted characters
    recipe = [replacing(i) for i in recipe]
        #again uses list comprehension form
    #get rid of any digits
    recipe = [i for i in recipe if not i.isdigit() ]
        #returns self if not a digit

    #stem ingredients -- get rood word for ingredient words
    recipe = [stemmer.lemmatize(i) for i in recipe]
    return recipe

#now count the number of times each ingredient appears
#loop over each recipe's ingredients in train - and count the ingredients
bag_words = [Counter(clean_recipe(recipe)) for recipe in train.ingredients]
#sum the counts
sum_bags = sum(bag_words, Counter())