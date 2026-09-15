# 📘 Assignment: Task Tracker with SQLite and FastAPI

## 🎯 Objective

Students will build a small task management API that stores data in SQLite and exposes CRUD endpoints with FastAPI. The activity focuses on persistence, SQL basics, and API design with validation and clear responses.

## 📝 Tasks

### 🛠️ Create the database and API structure

#### Descrição
Set up a FastAPI project that connects to a SQLite database and creates a tasks table for storing to-do items.

#### Requisitos
O programa concluído deve:

- Create a SQLite database file such as `tasks.db`.
- Create a `tasks` table with columns like `id`, `title`, `description`, and `completed`.
- Initialize the database when the app starts.
- Create a FastAPI application instance with a simple health-check endpoint.
- Return JSON responses from the API.

### 🛠️ Implement CRUD routes

#### Descrição
Create endpoints for creating, reading, updating, and deleting tasks in the database.

#### Requisitos
O programa concluído deve:

- Add a route to list all tasks.
- Add a route to get one task by ID.
- Add a route to create a new task.
- Add a route to update an existing task.
- Add a route to delete a task.
- Use proper HTTP status codes such as `200`, `201`, and `404`.
- Return task data in JSON format.

### 🛠️ Validate input and improve the API

#### Descrição
Add validation and error handling so the API accepts clean data and responds clearly when something goes wrong.

#### Requisitos
O programa concluído deve:

- Validate required fields before inserting into the database.
- Ensure the `title` cannot be empty.
- Handle requests for non-existent tasks with a `404` response.
- Use a Pydantic model to structure request and response data.
- Test the API using FastAPI’s built-in documentation at `/docs`.
- Include at least one example request and response in the project notes.
