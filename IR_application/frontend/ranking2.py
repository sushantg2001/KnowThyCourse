import nltk
import pandas as pd
from tqdm import tqdm
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.metrics.distance import jaccard_distance
from nltk.util import ngrams
from nltk.corpus import words

nltk.download('punkt')
nltk.download('stopwords')
stop_words = stopwords.words('english')

def preprocessing(text_file):
    tokenizer = nltk.RegexpTokenizer(r"\w+")    # remove punctuations
    tokens = tokenizer.tokenize(text_file)    # token the text

    tokens = [token.lower() for token in tokens]    # lower case
    tokens = [word for word in tokens if not word in stop_words]    # remove stop words

    stemmer = PorterStemmer()    #stemming tokens
    tokens = [stemmer.stem(word) for word in tokens]
    
    lemmatizer = WordNetLemmatizer()   #lemmatizing tokens
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    
    return tokens

def didyoumean(query):
    query = preprocessing(query)
    correct=[]
    correct_words = words.words()
    for word in query:
        temp = [(jaccard_distance(set(ngrams(word, 2)),set(ngrams(w, 2))), w)
                for w in correct_words if w[0] == word[0]]
        correct.append(sorted(temp, key=lambda val: val[0])[0][1])
    # correct = spell.unknown(query)
    str1=" "
    correct=str1.join(correct)
    return preprocessing(correct)

def ranking(query,data,total_n):
    inp = didyoumean(query)
    print(inp)

    numberofcourses = data.shape[0]
    # courses_desc = []
    numberofhits = {}
    for i in tqdm(range(numberofcourses)):
        text = str(data['Name'][i])+" "+str(data['About'][i])
        tokens = preprocessing(text)
        # courses_desc.append(tokens)
        hits = 0
        for x in inp: 
            if x in tokens:
                hits+=1
        numberofhits[i] = hits

    sorted_hits = dict(sorted(numberofhits.items(), key=lambda item: item[1], reverse=True))
    names = set(sorted_hits.values())

    d = {}
    for name in names:
        d[name] = [k for k,m in sorted_hits.items() if m==name]
    names = list(d.keys())
    print(len(names))

    results_list = {}
    for i in range(len(d)-1,-1,-1):
        max_courses = d[names[i]]
        rating = {}
        for k in max_courses:
            courserating = data['Ratings'][k]
            try:
                rating[k] = float(courserating)
            except:
                continue
        
        sorted_rating = dict(sorted(rating.items(), key=lambda item:item[1], reverse=True))
        list_order = list(sorted_rating.keys())
        results_list[names[i]] = list_order
    
    ans = []
    for i,j in results_list.items():
        for docid in j:
            ans.append(docid)
            if len(ans)>=total_n: break
    
    final_results = []
    for i in ans:
        record = {}
        record['Name'] = data.iloc[i,1]
        record['Website'] = data.iloc[i,0]
        record['About'] = data.iloc[i,6]
        record['Ratings'] = data.iloc[i,4]
        record['Link'] = data.iloc[i,5]
        record['Difficulty Level'] = data.iloc[i,3]
        record['Enrollment'] = data.iloc[i,8]

        final_results.append(record)
    
    # print(len(final_results))
    return final_results[:total_n]

# data = pd.read_csv("final_dataset.csv")
# query = "learn deep learming pthon programing"
# t = ranking(query,data,15)
# print(len(t))