import json
import sqlite3
import pdb

db = sqlite3.connect('stop_and_frisked.db')
c = db.cursor()
c.execute('''create table stop_and_frisked
         (year text,
          datestop text,
          timestop text,
          frisked text,
          searched text,
          arstmade text,
          pct text,
          sex text,
          race text,
          age text,
          eyecolor text,
          haircolr text,
          build text,
          xcoord text,
          ycoord text)''')
c.close()

db.commit()
db.close()