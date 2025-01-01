import os
from pathlib import Path
import yaml
from fastapi import FastAPI, Query
import psycopg2
from dotenv import load_dotenv

from src.httpclient.HttpxClient import HttpxClient  # type: ignore[import-not-found] # noqa: E501


load_dotenv()

app = FastAPI()
httpx_client = HttpxClient()

PATH = Path(".") / "version.yml"


def connect_to_database():
    """Connect to the PostgreSQL database server and fetch data"""
    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(
            dbname=f"{os.getenv('POSTGRES_DB')}",
            user=f"{os.getenv('POSTGRES_USER')}",
            password=f"{os.getenv('POSTGRES_PASSWORD')}",
            host=f"{os.getenv('POSTGRES_HOST')}",
            port="5432",
        )

        cursor = connection.cursor()

        cursor.execute("SELECT * FROM users")

        rows = cursor.fetchall()

        return rows  # Return the fetched data as a list of tuples

    except psycopg2.Error as error:
        print("Error while connecting to PostgreSQL:", error)
        return []  # Return an empty list in case of an error

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


@app.get("/")
async def get_root():
    return {"message": "You are at the root endpoint."}


@app.get("/message")  # /message?question=Who%20is%20Elon%20Musk?
async def get_answer(question: str = Query("What is your name?")):
    response = await httpx_client.post(question)
    return response


@app.get("/healthcheck")
async def get_healthcheck_data():
    return {"message": "Chatbot is healthy"}


@app.get("/version")
async def get_version():
    with open(PATH, "r") as file:
        yaml_content = yaml.safe_load(file)
    return f"version: {yaml_content['version']}"


@app.get("/data")
async def read_data():
    """Return data from the database"""
    data = connect_to_database()
    return {"data": data}


# python3 -m venv venv
# . venv/bin/activate
# pip install --upgrade pip setuptools wheel
# pip install -r requirements.txt
# uvicorn src.app.main:app --host 0.0.0.0 --port 8000 --reload
