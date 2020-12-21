from flask import Flask , render_template , request
import sqlite3

app = Flask(__name__,template_folder='template')


connection = sqlite3.connect('podcast.db')
cursor = connection.cursor()
cursor.execute("select * from cast;")
result = cursor.fetchall()
for row in result:
	       print("Id: ", row[0])
	       print("Name: ", row[1])
	       print("id: ", row[2])
	       print("JoiningDate: ", row[3])
	       print("Name: ", row[4])
	       print("\n")


@app.route('/')
def table():
	return render_template("index.html",row=row,result=result)

@app.route('/searcha',methods=['GET', 'POST'])
def search():

	if request.method == 'POST':
		artsit = request.form.get('artsit')
		name = request.form.get('name')
		connection = sqlite3.connect('podcast.db')
		cursor = connection.cursor()
		cursor.execute("select artistName,id,eleaseDate,name,kind,copyright,artistId,artistUrl,artworkUrl100 from cast WHERE artistName=? and name=?;",(artsit,name))
		result = cursor.fetchall()
		for row in result:
			       print("Id:", row[0])
			       return render_template("search_Podcast.html",row=row,result=result)
	else:
		return render_template("search_Podcast.html")


if __name__ == "__main__":
	app.run(debug=True)