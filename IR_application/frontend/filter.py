import pandas as pd

def filter(result_list,filters):
    '''
    result_list: list of dict
    filter_rating: float [0,5.0]
    filter_website: boolean[Coursera,Edx,Udemy,Udacity]
    filter_difficulty: boolean[Beginner,Intermediate,Advanced]
    '''
    filter_rating = filters[0]
    print(filter_rating)
    print(type(filter_rating))
    filter_website = filters[1]
    filter_difficulty = filters[2]
    df = pd.DataFrame(result_list)
    # print(df.shape)
    print(df.info())
    df = df[df['Ratings'] > filter_rating]
    # print(df.shape)

    difficulty_map = {0:'Beginner', 1:'Intermediate', 2:'Advanced'}
    difs = []
    for i in list(difficulty_map.keys()):
        if filter_difficulty[i]:
            difs.append(difficulty_map[i])
    df = df[df['Difficulty Level'].isin(difs)]
    # print(df.shape)

    website_map = {0:'Coursera', 1:'Edx', 2:'Udemy', 3:'Udacity'}
    webs = []
    for i in list(website_map.keys()):
        if filter_website[i]:
            webs.append(website_map[i])
    df = df[df['Website'].isin(webs)]
    # print(df.shape)

    return df.to_dict('records')