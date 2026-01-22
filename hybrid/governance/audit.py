from database.mysql import connect

class Audit:
    def log(self, action, actor="SYSTEM"):
        db = connect()
        cur = db.cursor()
        cur.execute(
            "INSERT INTO audit_logs (action, actor) VALUES (%s, %s)",
            (action, actor)
        )
        db.commit()
