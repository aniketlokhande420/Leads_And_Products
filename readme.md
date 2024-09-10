# Django Product and Lead Management API

This project is a Django-based RESTful API for managing products and leads, with additional reporting functionalities and authentication mechanisms.

## Features

- **Product Management**: Full CRUD operations for managing products.
- **Lead Management**: Create leads through an open API without authentication.
- **Reporting APIs**:
  - Fetch leads created between two dates.
  - Retrieve top 10 products with the most leads.
  - Retrieve bottom 10 products with the least leads.
  - Determine how many products each lead has inquired about.
- **Authentication**: All APIs (except lead creation) require authentication using Django's built-in authentication system.

## Technology Stack

- **Backend Framework**: Django (Python)
- **Database**: SQLite3
- **API Documentation**: Swagger (using `drf-yasg`)

## Setup and Installation

### Prerequisites

- Python 3.x
- `pip` (Python package manager)
- `virtualenv` (optional but recommended)

### Installation Steps

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3. **Install dependencies:**

    ```bash
    pip install django, django-restframework, setuptools, drf-yasg
    ```

4. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

7. **Access the application:**

    - The application will be available at `http://127.0.0.1:8000/`.

## API Endpoints

### 1. Product Management APIs

- **Create Product**: `POST /api/products/`
- **List Products**: `GET /api/products/`
- **Retrieve Product**: `GET /api/products/{id}/`
- **Update Product**: `PUT /api/products/{id}/`
- **Delete Product**: `DELETE /api/products/{id}/`

### 2. Lead Management APIs

- **Create Lead** (No Authentication Required): `POST /api/leads/`
- **List Leads**: `GET /api/leads/`

### 3. Reporting APIs

- **Fetch Leads Between Two Dates**: `GET /api/reports/leads/?start_date={YYYY-MM-DD}&end_date={YYYY-MM-DD}`
- **Top 10 Products with Most Leads**: `GET /api/reports/top-products/`
- **Bottom 10 Products with Least Leads**: `GET /api/reports/bottom-products/`
- **Number of Products Inquired by Each Lead**: `GET /api/reports/leads/products-count/`

### 4. Authentication API

- **Admin Login (To Obtain CSRF Token and Session Cookie)**: `POST /admin/login/`

## How to Run the APIs(Broswer) Recommended

### 1. Using the local host directly

- **Step 1:**
  Follow the link directly after successfully running the server
  http://127.0.0.1:8000/admin/login/

- **Step 2:**
  Now you can use all the other apis easily.
  Note, if you skip step 1 you may face authentication errors.

## How to Run the APIs(Postman)

### 1. Using Admin API to Get CSRF Token and Session Cookie

- **Step 1: Get CSRF Token**

  Make a `GET` request to the login page:
  GET http://127.0.0.1:8000/admin/login/

Extract the `csrftoken` from the response headers.

- **Step 2: Authenticate**

Make a `POST` request to log in:
POST http://127.0.0.1:8000/admin/login/


**Headers:**
- `X-CSRFToken`: `<your_csrf_token_here>`

**Body (x-www-form-urlencoded):**
- `username`: `<your_username>`
- `password`: `<your_password>`

Extract the `sessionid` cookie from the response.

### 2. Setting Cookies in Postman

- **Step 1: Manage Cookies in Postman**

- Click on the **Cookies** button in Postman.
- Add a new cookie with the following details:
  - **Domain**: `127.0.0.1` (or your server domain)
  - **Cookie Name**: `csrftoken`
  - **Cookie Value**: `<your_copied_csrf_token>`
  - **Cookie Name**: `sessionid`
  - **Cookie Value**: `<your_copied_session_id>`

- **Step 2: Make Authenticated Requests**

Now, use Postman to make requests to other endpoints. The cookies will automatically be sent with the requests.

## API Documentation

The Swagger API documentation can be accessed at:
http://127.0.0.1:8000/swagger/

## Troubleshooting

- **No module named 'pkg_resources'**: Ensure `setuptools` is installed by running `pip install setuptools`.
- **TemplateDoesNotExist drf-yasg/swagger-ui.html**: Ensure `drf_yasg` is added to `INSTALLED_APPS` and `APP_DIRS` is set to `True` in your `TEMPLATES` setting.

## Contribution

Feel free to open issues, submit pull requests, or suggest improvements. All contributions are welcome!
