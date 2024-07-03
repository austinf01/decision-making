from jikanpy import Jikan
from random import choice

import pandas as pd

moods = ['sad', 'angry', 'fear', 'romance', 'calm', 'happy', 'anxious', 'cheerful', 'dissapointed', 'disgusted', 'energetic', 'bored']

animes = [['Naruto', 'happy'],
          ['Haikyuu', 'sad', ], 
          ['Mushishi', 'energetic'],
          ['Bleach', 'angry']]

selection = []

jikan = Jikan()
df = pd.DataFrame(jikan.anime(457))
print(df['data'][['title_japanese', 'title_english']])
print(df['data']['episodes'])

#gets the number of minutes in the duration of the episode/movie 
print([int(s) for s in df['data']['duration'].split() if s.isdigit()][0])

#gets genre
# print([genre['name'] for genres_list in df['data'].apply(lambda x: x['genres']) for genre in genres_list])

# List comprehension to extract 'name' from 'genres'

genres = df['data']['genres']

size = len(genres)
names = [genres[i]['name'] for i in range(size)]
print(names)

# print('what mood are you in?')
# mood = input()

# for item in animes:
#   if item[1] == mood:
#     selection.append(item[0])

# print('\nYou should watch ' + choice(selection))