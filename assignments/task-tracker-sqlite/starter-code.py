import sqlite3
from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task Tracker API")


DATABASE_NAME = "tasks.db"


def get_db_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def initialize_database():
    conn = get_db_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            completed BOOLEAN DEFAULT 0
        )
        """
    )
    conn.commit()
    conn.close()


initialize_database()


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


@app.get("/")
def read_root():
    return {"message": "Task Tracker API is running"}


# TODO: Create a route to list all tasks
# TODO: Create a route to get one task by ID
# TODO: Create a route to create a new task
# TODO: Create a route to update an existing task
# TODO: Create a route to delete a task
# TODO: Add validation and error handling for missing tasks
