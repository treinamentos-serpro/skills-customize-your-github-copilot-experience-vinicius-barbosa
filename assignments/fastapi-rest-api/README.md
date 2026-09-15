# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Students will build a small REST API using FastAPI, learning how to define routes, validate input with Pydantic models, and implement basic CRUD operations in a clean, production-ready structure.

## 📝 Tasks

### 🛠️ Create the FastAPI App

#### Descrição
Set up a new FastAPI application and create the basic structure for a REST API.

#### Requisitos
O programa concluído deve:

- Install and import the `fastapi` and `uvicorn` packages.
- Create an instance of `FastAPI` with a clear application title.
- Add a root endpoint such as `/` or `/health` that returns a JSON response.
- Run the app locally with `uvicorn`.
- Example response:
  ```json
  {
    "message": "FastAPI server is running"
  }
  ```

### 🛠️ Define a Data Model and CRUD Routes

#### Descrição
Model a simple resource, such as tasks, books, or students, and implement CRUD endpoints for it.

#### Requisitos
O programa concluído deve:

- Define a Pydantic model for the resource using `BaseModel`.
- Create endpoints to:
  - list all items
  - get one item by ID
  - create a new item
  - update an existing item
  - delete an item
- Use HTTP status codes such as `200`, `201`, and `404` appropriately.
- Return JSON responses in a consistent format.

### 🛠️ Add Validation and Error Handling

#### Descrição
Improve the API by validating request data and handling common errors in a user-friendly way.

#### Requisitos
O programa concluído deve:

- Validate required fields and value constraints using Pydantic.
- Return a clear `404` response when an item does not exist.
- Use descriptive response messages for invalid requests.
- Include at least one example request and response in the API documentation.
- Ensure the application returns correctly formatted JSON for all endpoints.
