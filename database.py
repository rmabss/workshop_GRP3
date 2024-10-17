import pymysql

def connect_to_db():
    """ Établit la connexion à la base de données MySQL """
    try:
        # Établir la connexion à MySQL
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='passer',
            database='thruth_scan'
        )

        if connection.open:
            print("Connexion réussie à la base de données MySQL")

            # Exécuter une requête de test
            cursor = connection.cursor()
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            print("Tables dans la base de données:")
            for table in tables:
                print(table[0])  # Afficher seulement le nom de la table

            # Appeler la fonction pour insérer des vidéos
            insert_video(connection, 'https://www.youtube.com/watch?v=cQ54GDm1eL0', 'Titre vidéo 1', 'Description vidéo 1')
            insert_video(connection, 'https://www.youtube.com/watch?v=AmUC4m6w1wo&t=13s', 'Titre vidéo 2', 'Description vidéo 2')

    except pymysql.MySQLError as e:
        print(f"Erreur lors de la connexion à MySQL: {e}")

    finally:
        if 'connection' in locals() and connection.open:
            cursor.close()
            connection.close()
            print("Connexion fermée.")

def insert_video(connection, url, titre, description):
    """ Insère une vidéo dans la table videos """
    query = "INSERT INTO videos (url, titre, description) VALUES (%s, %s, %s)"
    try:
        cursor = connection.cursor()
        cursor.execute(query, (url, titre, description))
        connection.commit()  # Valide la transaction
        print("Vidéo insérée avec succès")
    except pymysql.MySQLError as e:
        print(f"Erreur lors de l'insertion de la vidéo: {e}")
    finally:
        cursor.close()  # Ferme le curseur après l'opération

if __name__ == "__main__":
    connect_to_db()

