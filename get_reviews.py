import json
import pandas as pd
import os,sys

#open json file
reviews = []
for line in open('C:/Downloads/yelp_dataset/yelp_academic_dataset_review.json', 'r',encoding="utf8"):
    reviews.append(json.loads(line))
#print(reviews[0])


#get features and put them in a dataframe
from flatten_json import flatten_json
r = reviews[0:30]
df = pd.DataFrame([flatten_json(x) for x in reviews])
df.head()
print(df.columns)   # 'review_id', 'user_id', 'business_id', 'stars', 'useful', 'funny','cool', 'text', 'date'

#find null cols
#print(df.isnull().values.any())

# avg and stds of numeric columns
#print(df.describe())

#find unique features
# for c in ['stars', 'useful', 'funny','cool']:
#     print(df[c].unique())

#drop not important features
important_features = df.drop(['review_id','user_id'],axis=1)
print(important_features.columns)

important_features.to_csv('data/reviews.csv', encoding='utf-8', index=False)