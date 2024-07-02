from random import choice

moods = ['sad', 'angry', 'fear', 'romance', 'calm', 'happy', 'anxious', 'cheerful', 'dissapointed', 'disgusted', 'energetic', 'bored']

animes = [['Naruto', 'happy'],
          ['Haikyuu', 'sad', ], 
          ['Mushishi', 'energetic'],
          ['Bleach', 'angry']]

selection = []

print('what mood are you in?')
mood = input()

for item in animes:
  if item[1] == mood:
    selection.append(item[0])

print('\nYou should watch ' + choice(selection))