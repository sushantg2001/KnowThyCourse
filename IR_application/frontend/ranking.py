# %% [markdown]
# # Information Retrieval
# # Group Project

# %% [markdown]
# #### Samad Shahid    2019446
# #### Shashwat Goyal  2019447
# #### Sushant Gupta   2019450
# #### Rishi Raj       2019090
# #### Shiven Gupta    2019333

# %%
import nltk
from nltk.tokenize import word_tokenize
import string
from collections import defaultdict
from nltk.corpus import stopwords
import os
import pandas as pd
import numpy as np
import sys

# %%
# folders=os.listdir(r'C:\Users\shash\Desktop\ira1')
# nltk.download('punkt')
# nltk.download('stopwords') # downloading packages

# %%
def ters(inp):
    temp=(c for c in inp if not c.isdigit() and c.isalnum() and c not in string.punctuation) # removes digits and punctuations
    one=1
    zero=0
    for i in range(1,2):
      one=one+zero
    temp1=''
    return temp1.join(temp)

# %%
def pro(inp):
    one=1
    zero=0
    stop=set(stopwords.words('english')) # makes a set of stopwords
    wordt = word_tokenize(inp.lower())  # lowers the words
    wordt = list(dict.fromkeys(wordt))  # removes duplicates
    for i in range(1,2):
      one=one+zero
    valid=[k for k in wordt if k not in stop]  #if the word is valid
    valid=[ters(k) for k in valid]
    for i in range(1,2):
      one=one+zero
    valid=[k for k in valid if len(k) > 1*one] # checking to see if length is greater than 1
    return valid

# %%
data = pd.read_csv("./../IR_application/final_dataset.csv")

# %%
coursewise_to_search = defaultdict(list)

for i in range(data.shape[0]):
  s = str(data["Name"][i]) + " " + str(data["About"][i])
  list_words = pro(s)
  coursewise_to_search[i] = list_words

noOfCourses = len(coursewise_to_search)

# %%
ratingFilter = 0    # 0->None, 1->greater than 4.5, 2->greater than 4, 3->greater than 3.5, 4->greater than 3
difficultyFilter = 0    # 0->None, 1->beginner, 2->intermediate, 3->advanced
websiteFilter = 0    # 0->None, 1->udemy, 2->udacity, 3->coursera, 4->edX

# %%
def didyoumean(query):
    from nltk.metrics.distance import jaccard_distance
    from nltk.util import ngrams
    from nltk.corpus import words

    nltk.download('words')

    stop=set(stopwords.words('english'))

    correct_words = words.words()

    query = word_tokenize(query.lower())
    query=[k for k in query if k not in stop]
    correct=[]

    for word in query:
        temp = [(jaccard_distance(set(ngrams(word, 2)),set(ngrams(w, 2))), w)
                for w in correct_words if w[0] == word[0]]
        correct.append(sorted(temp, key=lambda val: val[0])[0][1])
    # correct = spell.unknown(query)
    str1=" "
    correct=str1.join(correct)
    return pro(correct)


# %%
def perform_query_search(inp):
  inp = didyoumean(inp)

  noOfHits = {}
  for docId in range(noOfCourses):
    hits = 0
    words = coursewise_to_search[docId]
    # print(words)
    for x in inp:
      if (x in words):
        hits += 1
    noOfHits[docId] = hits

  sorted_noOfHits = dict(sorted(noOfHits.items(), key=lambda item: item[1], reverse=True))

  names = set(sorted_noOfHits.values())

  d={}
  for n in names:
      d[n] = [k for k in sorted_noOfHits.keys() if sorted_noOfHits[k] == n]
  # print(d)

  # print(type(data["Ratings"][0]))
  super_ans = {}
  for i in range(len(d)-1,0,-1):
    max_courses=d[list(d.keys())[i]]
    rating={}
    for k in max_courses:
      if ( not pd.isna(data["Ratings"][k]) and data["Ratings"][k] != "Not Calibrated" and data["Ratings"][k] != "None" ):
        rating[k]=float(data["Ratings"][k])
    sorted_rating = dict(sorted(rating.items(), key=lambda item: item[1], reverse=True))
    list_order = list(sorted_rating.keys())
    super_ans[list(d.keys())[i]] = list_order

  return super_ans

# %%
def inFilter(ind):
  flag = True

  curRating = float(data["Ratings"][ind])
  if (ratingFilter == 1 and curRating < 4.5):
    flag = False
  elif (ratingFilter == 2 and curRating < 4):
    flag = False
  elif (ratingFilter == 3 and curRating < 3.5):
    flag = False
  elif (ratingFilter == 4 and curRating < 3):
    flag = False
  if (not flag):
    return False

  curDifficulty = data["Difficulty Level"][ind]
  if (difficultyFilter == 1 and curDifficulty != "Beginner"):
    flag = False
  elif (difficultyFilter == 2 and curDifficulty != "Intermediate"):
    flag = False
  elif (difficultyFilter == 3 and curDifficulty != "Advanced"):
    flag = False
  if (not flag):
    return False

  curWebsite = data["Website"][ind]
  if (websiteFilter == 1 and curWebsite != "Udemy"):
    flag = False
  elif (websiteFilter == 2 and curWebsite != "Udacity"):
    flag = False
  elif (websiteFilter == 3 and curWebsite != "Coursera"):
    flag = False
  elif (websiteFilter == 4 and curWebsite == "Edx"):
    flag = False
  if (not flag):
    return False

  return True

# %%
def print_results(super_ans):
  count = 0
  ans = []
  hits = []

  for i in super_ans.keys():
    for j in super_ans[i]:
      if (inFilter(j)):
        ans.append(j)
        hits.append(i)
        count = count + 1
      if (count > 10):
        break
    if (count > 10):
      break

  for i in range(len(ans)):
    # print(data.iloc[i,:])
    print("Website: " + data["Website"][ans[i]] + "\t\tCourse Name: " + data["Name"][ans[i]] + "\t\tHits: " + str(hits[i]) + "\t\tRating: " + str(data["Ratings"][ans[i]]) + "\t\tDifficulty: " + data["Difficulty Level"][ans[i]])

# %%
def query_menu():

  # Resetting filters
  global ratingFilter
  global difficultyFilter
  global websiteFilter

  ratingFilter = 0
  difficultyFilter = 0
  websiteFilter = 0

  # Apply algo
  output = perform_query_search()

  print_results(output)

  while (1):
    z = int(input("\nEnter\n 1. Apply filter to this query\n 2. Try another Query\n 3. Back to Main Menu\n 4. Exit\n---------------->"))
    if (z == 1):
      filter_menu()
      print_results(output)
    elif (z == 2):
      query_menu()
    elif (z == 3):
      main_menu()
    elif (z == 4):
      sys.exit()
    else:
      print("Invalid Input, try again\n")

# %%
def filter_menu():

  global ratingFilter
  global difficultyFilter
  global websiteFilter

  while (1):
    z = int(input("\nEnter\n 1. Ratings Filter\n 2. Difficulty Levels\n 3. Website Filter\n 4. Done\n---------------->"))

    if (z == 1):
      # rating filter
      print("\nCurrent Filter: ", str(ratingFilter))
      toChange = int(input("Change to\n 0. All\n 1. >=4.5 Only\n 2. >=4 Only\n 3. >=3.5 Only\n 4. >=3 Only\n---------------->"))
      if (toChange <= 4 and toChange >= 0):
        ratingFilter = toChange
        print("Filter Applied")
      else:
        print("Invalid Input, filter unchanged")
    elif (z == 2):
      # difficulty filter
      print("\nCurrent Filter: ", str(difficultyFilter))
      toChange = int(input("Change to\n 0. All\n 1. Beginner Only\n 2. Intermediate Only\n 3. Advanced Only\n---------------->"))
      if (toChange <= 3 and toChange >= 0):
        difficultyFilter = toChange
        print("Filter Applied")
      else:
        print("Invalid Input, filter unchanged")
    elif (z == 3):
      # website filter
      print("\nCurrent Filter: ", str(websiteFilter))
      toChange = int(input("Change to\n 0. All\n 1. Udemy Only\n 2. Udacity Only\n 3. >Coursera Only\n 4. EdX Only\n---------------->"))
      if (toChange <= 4 and toChange >= 0):
        websiteFilter = toChange
        print("Filter Applied")
      else:
        print("Invalid Input, filter unchanged")
    elif (z == 4):
      return
    else:
      print("Invalid Input, try again\n")

# %%
def main_menu():
  z = int(input("\nEnter\n 1. Enter Query\n 2. Exit\n---------------->"))

  if (z == 1):
    query_menu()
  elif (z == 2):
    sys.exit()
  else:
    print("Invalid Input, try again\n")
    main_menu()
