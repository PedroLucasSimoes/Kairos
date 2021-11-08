import sqlite3

def connect():
    try:
        db = sqlite3.connect('E:\Desktop\coding\python\Kairos\db\db_1962.db')
        cur = db.cursor()
    except Exception as e:
        print(f"An error ocurred while initializing the db. Error: {e}")
    else:
        print("DB Initialized")
        return db, cur
        
    
