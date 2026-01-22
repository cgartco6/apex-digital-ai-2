from database.mysql import connect

def migrate():
    db = connect()
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS schema_versions (version INT PRIMARY KEY)")
    db.commit()

if __name__ == "__main__":
    migrate()
