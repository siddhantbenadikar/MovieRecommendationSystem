import requests
import csv
import time

API_KEY = 'cc9594c46dbb5d5c6b363a60f2cdff1c'
URL = 'https://api.themoviedb.org/3/movie/{}'
PARAMS = {'api_key': API_KEY, 'language': 'en-US'}

with open('ml-latest-small/linkscopy.csv') as linksfile:
    csvreader = csv.reader(linksfile)
    count = 0
    metaDataFile = open('ml-latest-small/movies_metadatanew.csv', 'w+')
    csvwriter = csv.writer(metaDataFile)
    next(csvreader, None)
    for row in csvreader:
        tmdbId = row[2]
        newURL = URL.format(tmdbId)
        r = requests.get(url = newURL, params=PARAMS)
        data = r.json()
        print(data)
        if count == 0:
            csvwriter.writerow(data.keys())
        csvwriter.writerow(data.values())
        count += 1

        if count % 40 == 0:
            time.sleep(8)
            
metaDataFile.close()
linksfile.close()
