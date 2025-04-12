<p align="center">
  <a href="https://fastapi.tiangolo.com"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI"></a>
</p>
<p align="center">
    <em>FastAPI framework, high performance, easy to learn, fast to code, ready for production</em>
</p>
<p align="center">
<a href="https://github.com/fastapi/fastapi/actions?query=workflow%3ATest+event%3Apush+branch%3Amaster" target="_blank">
    <img src="https://github.com/fastapi/fastapi/actions/workflows/test.yml/badge.svg?event=push&branch=master" alt="Test">
</a>
<a href="https://coverage-badge.samuelcolvin.workers.dev/redirect/fastapi/fastapi" target="_blank">
    <img src="https://coverage-badge.samuelcolvin.workers.dev/fastapi/fastapi.svg" alt="Coverage">
</a>
<a href="https://pypi.org/project/fastapi" target="_blank">
    <img src="https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
<a href="https://pypi.org/project/fastapi" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058" alt="Supported Python versions">
</a>
</p>

---

**Documentation**: <a href="https://fastapi.tiangolo.com" target="_blank">https://fastapi.tiangolo.com</a>

# FastAPI MySQL Docker Project

## 📝 Description
A backend project using the FastAPI framework, MySQL database, and Docker. This project provides a REST API with JWT authentication and user management.
## 🛠 Technologies Used
- FastAPI
- MySQL
- SQLAlchemy
- Alembic
- Docker & Docker Compose
- JWT Authentication
- Pydantic
- Python 3.9

## 🚀 Setup and Run

### Prerequisites
- Docker
- Docker Compose

### Installation Steps

1. Clone repository:
```bash
git clone <repository-url>
cd <project-folder>
```

2. Create a .env file from the example:
```bash
cp .env.example .env
```

3. Configure environment variables in the .env file:
DATABASE_URL=mysql+pymysql://user:password@db:3306/dbname
DATABASE_USER=user
DATABASE_PASSWORD=password
DATABASE_NAME=dbname
DATABASE_HOST=db
MYSQL_ROOT_PASSWORD=rootpassword
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

4. Start the application with Docker:
```bash
docker-compose up -d --build
```

5. Run migrations:
```bash
docker-compose exec fastapi alembic upgrade head
```

### Project Structure
```
.
├── app/
│   ├── api/
│   │   └── v1/
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   ├── models/
│   │   ├── base.py
│   │   └── user.py
│   ├── schemas/
│   └── main.py
├── migrations/
├── tests/
├── .env
├── .gitignore
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```

### Database Migrations
#### Create a new migration:
```
docker-compose exec fastapi alembic revision --autogenerate -m "description"
```

#### Run migrations:
```
docker-compose exec fastapi alembic upgrade head
```

#### Rollback migration::
```
docker-compose exec fastapi alembic downgrade -1
```

### API Documentation
After running the application, you can access:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Contact
Email: [lephung8399@gmail.com](lephung8399@gmail.com)

