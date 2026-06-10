from fastapi import FastAPI
from datetime import datetime
import os
import socket
import psycopg2

app = FastAPI()

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "devopsdb")
DB_USER = os.getenv("DB_USER", "devopsuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "devopspassword")


def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
    )


#@app.get("/")
#def read_root():
#    return {
#        "message": "FastAPI + PostgreSQL deployed by GitHub Actions",
#        "hostname": socket.gethostname(),
#        "environment": os.getenv("APP_ENV", "development"),
#        "time": datetime.utcnow().isoformat(),
#    }

@app.get("/")
def read_root():
    raise Exception("Simulated production error")

@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }


@app.get("/db-check")
def db_check():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()
        cur.close()
        conn.close()

        return {
            "database": "connected",
            "postgres_version": version[0]
        }
    except Exception as e:
        return {
            "database": "error",
            "detail": str(e)
        }
