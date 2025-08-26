# 🚀 FastAPI Blog API

A modern, high-performance RESTful blog API built with FastAPI, featuring JWT authentication, user management, and comprehensive blog operations. This project demonstrates best practices in API development with Python, including proper project structure, security implementation, and database management.

![FastAPI Blog API Screenshot 1](assets/fastapipic1.png)

## ✨ Features

### 🔐 Authentication & Security

- **JWT Token Authentication** - Secure user authentication with JSON Web Tokens
- **Password Hashing** - Bcrypt encryption for secure password storage
- **OAuth2 Bearer Token** - Industry-standard authentication flow
- **Protected Routes** - Secure endpoints requiring authentication

### 👥 User Management

- **User Registration** - Create new user accounts
- **User Profile** - Retrieve user information and associated blogs
- **Secure Login** - Authenticate users with email/password

### 📝 Blog Operations

- **Create Blogs** - Authenticated users can create new blog posts
- **Read Blogs** - Retrieve all blogs or specific blog by ID
- **Update Blogs** - Edit existing blog posts
- **Delete Blogs** - Remove blog posts
- **User-Blog Relationships** - Each blog is associated with its creator

### 🛠️ Technical Features

- **SQLAlchemy ORM** - Robust database operations with relationships
- **Pydantic Models** - Data validation and serialization
- **Alembic Migrations** - Database schema version control
- **Modular Architecture** - Clean separation of concerns
- **Environment Configuration** - Production-ready settings management
- **CORS Support** - Cross-origin resource sharing enabled
- **API Documentation** - Auto-generated interactive docs

![FastAPI Blog API Screenshot 2](assets/fastapipic2.png)

## 🏗️ Project Structure

```
fastapi-project/
├── blog/                          # Main application package
│   ├── routers/                   # API route handlers
│   │   ├── authentication.py     # Auth endpoints (/login)
│   │   ├── blog.py               # Blog CRUD endpoints
│   │   └── user.py               # User management endpoints
│   ├── repository/               # Data access layer
│   │   ├── blog.py              # Blog database operations
│   │   └── user.py              # User database operations
│   ├── alembic/                 # Database migrations
│   ├── config.py                # Environment configuration
│   ├── database.py              # Database connection setup
│   ├── hashing.py               # Password hashing utilities
│   ├── main.py                  # FastAPI application instance
│   ├── models.py                # SQLAlchemy database models
│   ├── oauth2.py                # OAuth2 authentication logic
│   ├── schemas.py               # Pydantic data models
│   └── token.py                 # JWT token operations
├── assets/                      # Project screenshots
├── build.sh                     # Render deployment build script
├── start.sh                     # Render deployment start script
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone the repository**
   
   ```bash
   git clone <repository-url>
   cd fastapi-project
   ```

2. **Create virtual environment**
   
   ```bash
   python -m venv fastapi-env
   
   # Windows
   fastapi-env\Scripts\activate
   
   # macOS/Linux
   source fastapi-env/bin/activate
   ```

3. **Install dependencies**
   
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   
   ```bash
   uvicorn blog.main:app --reload
   ```

5. **Access the API**
   
   - API: http://localhost:8000
   - Interactive Docs: http://localhost:8000/docs
   - Alternative Docs: http://localhost:8000/redoc

## 📚 API Endpoints

### Authentication

| Method | Endpoint | Description | Auth Required |
| ------ | -------- | ----------- | ------------- |
| POST   | `/login` | User login  | ❌             |

### Users

| Method | Endpoint     | Description     | Auth Required |
| ------ | ------------ | --------------- | ------------- |
| POST   | `/user/`     | Create new user | ❌             |
| GET    | `/user/{id}` | Get user by ID  | ✅             |

### Blogs

| Method | Endpoint     | Description     | Auth Required |
| ------ | ------------ | --------------- | ------------- |
| GET    | `/blog/`     | Get all blogs   | ✅             |
| POST   | `/blog/`     | Create new blog | ✅             |
| GET    | `/blog/{id}` | Get blog by ID  | ✅             |
| PUT    | `/blog/{id}` | Update blog     | ✅             |
| DELETE | `/blog/{id}` | Delete blog     | ✅             |

### System

| Method | Endpoint  | Description   | Auth Required |
| ------ | --------- | ------------- | ------------- |
| GET    | `/`       | Root endpoint | ❌             |
| GET    | `/health` | Health check  | ❌             |

## 🔧 Configuration

### Environment Variables

Create a `.env` file or set environment variables:

```env
SECRET_KEY=your-super-secret-key-here
DATABASE_URL=postgresql://user:password@localhost/dbname  # For production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Database Configuration

- **Development**: SQLite (default)
- **Production**: PostgreSQL (recommended)

## 🧪 Usage Examples

### 1. Create a User

```bash
curl -X POST "http://localhost:8000/user/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "password": "securepassword"
  }'
```

### 2. Login

```bash
curl -X POST "http://localhost:8000/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=john@example.com&password=securepassword"
```

### 3. Create a Blog (with token)

```bash
curl -X POST "http://localhost:8000/blog/" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My First Blog",
    "body": "This is the content of my first blog post."
  }'
```

## 🚀 Deployment

### Render Deployment

This project is configured for easy deployment on Render:

1. **Push to GitHub**
2. **Create Render Account**
3. **Create PostgreSQL Database**
4. **Create Web Service**
5. **Set Environment Variables**
6. **Deploy**

Detailed deployment instructions are included in the project.

### Local Development

```bash
# Run with auto-reload
uvicorn blog.main:app --reload --host 0.0.0.0 --port 8000
```

## 🛠️ Technologies Used

- **[FastAPI](https://fastapi.tiangolo.com/)** - Modern, fast web framework for building APIs
- **[SQLAlchemy](https://www.sqlalchemy.org/)** - SQL toolkit and ORM
- **[Pydantic](https://pydantic-docs.helpmanual.io/)** - Data validation using Python type hints
- **[Alembic](https://alembic.sqlalchemy.org/)** - Database migration tool
- **[Passlib](https://passlib.readthedocs.io/)** - Password hashing library
- **[Python-JOSE](https://python-jose.readthedocs.io/)** - JWT implementation
- **[Uvicorn](https://www.uvicorn.org/)** - ASGI server implementation

## 📁 Database Schema

### Users Table

- `id` (Primary Key)
- `name` (String)
- `email` (String, Unique)
- `password` (Hashed String)

### Blogs Table

- `id` (Primary Key)
- `title` (String)
- `body` (Text)
- `user_id` (Foreign Key → Users.id)

### Relationships

- One User can have many Blogs
- Each Blog belongs to one User

## 🔒 Security Features

- **Password Hashing**: Bcrypt with salt
- **JWT Tokens**: Secure authentication tokens
- **Token Expiration**: Configurable token lifetime
- **Protected Routes**: Authentication required for sensitive operations
- **CORS Configuration**: Cross-origin request handling
- **Input Validation**: Pydantic model validation

## 🧪 Testing

Run the test suite:

```bash
pytest
```

## 📝 API Documentation

Once the server is running, visit:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- FastAPI team for the excellent framework
- SQLAlchemy team for the robust ORM
- The Python community for amazing libraries

---

**Built with ❤️ using FastAPI**

Please give this repository a star and follow my account also, cheers!
For questions or support, please open an issue in the repository.