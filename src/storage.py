import sqlite3

def save_to_db(df):
    conn = sqlite3.connect("rail_data.db")
    df.to_sql("journeys", conn, if_exists="replace", index=False)
    conn.close()
    print("Saved to database")