import sqlite3

def connect():
    global db, cur
    try:
        db = sqlite3.connect('E:\Desktop\coding\python\Kairos\db\db_1962.db')
        cur = db.cursor()
    except Exception as e:
        print(f"An error ocurred while initializing the db. Error: {e}")
    else:
        return db, cur

def closeConn():
    try:
        db.close()
    except Exception as e:
        print(f"Database could not be closed. Reason:{e}")
    else: return

        
    
