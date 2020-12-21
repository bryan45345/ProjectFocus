import json
import sqlite3

conn = sqlite3.connect("podcast.db")
c = conn.cursor()


with open('in.json') as json_file:
	 data = json.load(json_file)
	 for p in data['feed']['results']:
	 	 print('Name: ' + p['artistName'])
	 	 print('id: ' + p['id'])
	 	 print('releaseDate: ' + p['releaseDate'])
	 	 print('name: ' + p['name'])
	 	 print('kind: ' + p['kind'])
	 	 try:
	 	   print('copyright: ' + p['copyright'])
	 	   print('artistId: ' + p['artistId'])
	 	   print('artistUrl: ' + p['artistUrl'])
	 	   print('artworkUrl100: ' + p['artworkUrl100'])
	 	   c.execute('''INSERT INTO cast (artistName,id,eleaseDate,name,kind,copyright,artistId,artistUrl,artworkUrl100) VALUES (?,?,?,?,?,?,?,?,?)''',(p['artistName'],p['id'],p['releaseDate'],p['name'],p['kind'],p['copyright'],p['artistId'],p['artistUrl'],p['artworkUrl100']))
	 	   conn.commit()
	 	 except:
	 	   print('copyright: No copyright')
	 	   print('artistId: No artistId')
	 	   print('artistUrl: No artistUrl')
	 	   print('artworkUrl100: No artworkUrl100')

	 	   

        



	 	 
	 	







	 	