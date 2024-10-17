from flask import Flask, render_template
import pymysql

app = Flask(__name__)

def connect_to_db():
    """ Établit la connexion à la base de données MySQL """
    connection = None
    try:
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='passer',
            database='thruth_scan'
        )
        print("Connexion réussie à la base de données MySQL")
    except pymysql.MySQLError as e:
        print(f"Erreur lors de la connexion à MySQL: {e}")
    return connection

def get_videos(connection):
    """ Récupère les vidéos de la table videos """
    query = "SELECT url, titre FROM videos"
    cursor = connection.cursor()
    cursor.execute(query)
    videos = cursor.fetchall()
    return [{"url": video[0], "titre": video[1]} for video in videos]  # Retourne une liste de dictionnaires

@app.route('/')
def index():
    conn = connect_to_db()
    videos = []
    if conn:
        videos = get_videos(conn)
        conn.close()
    return render_template('index.html', videos=videos)

if __name__ == "__main__":
    app.run(debug=True)
