from fastapi import FastAPI
import psycopg2

app = FastAPI(title="Example")

conn = psycopg2.connect(
    dbname="bizaList",
    user="postgres",
    password="12345",
    host="localhost"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM music")
results = cursor.fetchall()
cursor.close()

@app.get("/")
async def get_music():
    return results