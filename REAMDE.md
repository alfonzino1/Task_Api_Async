#  Task API

FastAPI-сервис для управления транзакциями с SQLAlchemy ORM, Pydantic-валидацией и Docker-оркестрацией.

## ✨ Фичи
- 🔒 Non-root контейнер (`appuser`)
- 📦 Multi-stage Dockerfile (~150MB итоговый образ)
- 💾 Персистентность данных через Docker Volumes
- 🏥 Health checks для контроля готовности
- 🧪 Автотесты через `fastapi.testclient`
- 📄 OpenAPI автодокументация (`/docs`)

##  Стек
| Компонент | Технология |
|-----------|------------|
| Backend   | FastAPI, Uvicorn |
| БД        | SQLite (через SQLAlchemy ORM) |
| Валидация | Pydantic v2 |
| Контейнеры| Docker, Docker Compose |
| Тесты     | pytest |

## 🚀 Запуск

### Локально
```bash
python -m venv .venv
source .venv/bin/activate  # или .venv\Scripts\activate на Windows
pip install -r requirements.txt
uvicorn main:app --reload