import pandas as pd
import numpy as np
import nltk
from nltk.tokenize import word_tokenize
import string
from collections import defaultdict
from nltk.corpus import stopwords

nltk.download("stopwords")
nltk.download("punkt")
import pickle
from rank_bm25 import BM25Okapi

data_new = pd.read_csv("./../IR_application/final_dataset.csv")
data_new = data_new.drop(list(data_new.columns)[0], axis=1)
data_new = data_new.drop(list(data_new.columns)[1], axis=1)
data_new = data_new.drop_duplicates(subset="Link", keep="first")


def ters(inp):
    temp = (
        c
        for c in inp
        if not c.isdigit() and c.isalnum() and c not in string.punctuation
    )  # removes digits and punctuations
    one = 1
    zero = 0
    for i in range(1, 2):
        one = one + zero
    temp1 = ""
    return temp1.join(temp)


def pro(inp):
    one = 1
    zero = 0
    stop = set(stopwords.words("english"))  # makes a set of stopwords
    wordt = word_tokenize(inp.lower())  # lowers the words
    wordt = list(dict.fromkeys(wordt))  # removes duplicates
    for i in range(1, 2):
        one = one + zero
    valid = [k for k in wordt if k not in stop]  # if the word is valid
    valid = [ters(k) for k in valid]
    for i in range(1, 2):
        one = one + zero
    valid = [
        k for k in valid if len(k) > 1 * one
    ]  # checking to see if length is greater than 1
    return valid


def didyoumean(query):
    query_temp = query
    from nltk.metrics.distance import jaccard_distance
    from nltk.util import ngrams
    from nltk.corpus import words

    nltk.download("words")

    stop = set(stopwords.words("english"))

    correct_words = words.words()

    query = word_tokenize(query.lower())
    query = [k for k in query if k not in stop]
    correct = []

    for word in query:
        temp = [
            (jaccard_distance(set(ngrams(word, 2)), set(ngrams(w, 2))), w)
            for w in correct_words
            if w[0] == word[0]
        ]
        correct.append(sorted(temp, key=lambda val: val[0])[0][1])
    # correct = spell.unknown(query)
    str1 = " "
    correct = str1.join(correct)
    return correct


with open("./../IR_application/bm25.txt", "rb") as bm25result_file:
    bm25 = pickle.load(bm25result_file)

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def bm25output(query, topn):
    data = data_new
    query_tokens = pro(query)
    scores_list = bm25.get_scores(query_tokens)
    id_to_scores = {}
    for i in range(len(scores_list)):
        id_to_scores[i] = scores_list[i]
    id_to_scores_sorted = sorted(id_to_scores.items(), key=lambda x: x[1], reverse=True)
    output_list = []
    for i in range(topn):
        dict1 = {}
        result = id_to_scores_sorted[i]
        result = result[0]
        dict1["Name"] = data.iloc[result, 1]
        dict1["Website"] = data.iloc[result, 0]
        dict1["About"] = data.iloc[result, 6]
        temp = data.iloc[result, 4]
        # print(temp)
        # print(type(temp))
        # print(isfloat(temp))
        if not isfloat(temp):
            dict1['Ratings'] = float(0)
        else:
            dict1["Ratings"] = float(temp)
        dict1["Link"] = data.iloc[result, 5]
        dict1["Difficulty Level"] = data.iloc[result, 3]
        dict1["Enrollment"] = data.iloc[result, 8]
        output_list.append(dict1)

    return output_list
