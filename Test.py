import scrython
import requests
import time
import sqlite3
import pandas as pd

con = sqlite3.connect("Inventory.db")

cur = con.cursor()
res = cur.execute('SELECT * FROM cards')

df = pd.DataFrame(res, columns=['set',
                            'col_num',
                            'foil',
                            'count',
                            'name',
                            'mcost',
                            'type',
                            'rarity',
                            'usd_price'])

print(df.head())
path = '.\images\\'

for index, row in df.iterrows(): 
    card = scrython.cards.Named(fuzzy=row[4], set=row[0])
    print(card.name())
    print(card.id())
    name = card.name().replace('//','')
    time.sleep(0.1)
    response = requests.get(card.image_uris(0, 'png'))

    with open('{}{}.png'.format(path, name), 'wb') as f:
       f.write(response.content)