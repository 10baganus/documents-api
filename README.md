# 📄 Documents API

**Documents API** — это RESTful-сервис на Django для загрузки, хранения и управления документами.  
Поддерживается авторизация по email, Swagger UI, кастомная модель пользователя и работа в Docker-контейнере.

---

## 🚀 Возможности

- 🔐 Авторизация по email (кастомная модель пользователя)
- 📁 Загрузка и просмотр документов
- 📄 Swagger-документация (`drf-yasg`)
- 🐳 Docker-окружение
- ⚙️ Настройка через `.env`

---

## 🛠️ Стек технологий

- Python 3.10+
- Django 5.2
- Django REST Framework
- SimpleJWT (JWT-авторизация)
- drf-yasg (Swagger UI)
- SQLite (можно заменить на PostgreSQL)
- Docker (опционально)

---

## ⚙️ Установка (локально)

```bash
git clone https://github.com/10baganus/documents-api.git
cd documents-api
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
