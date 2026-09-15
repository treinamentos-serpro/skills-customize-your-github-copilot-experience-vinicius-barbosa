from fastapi import FastAPI

app = FastAPI(title="Student API")


@app.get("/")
def read_root():
    return {"message": "FastAPI server is running"}


# TODO: Create a data model for your resource
# TODO: Add CRUD routes for creating, reading, updating, and deleting items
# TODO: Add validation and error handling
