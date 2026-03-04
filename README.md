# IR Search Engine - Project 31

A Django-based Information Retrieval application that implements advanced search algorithms including BM25 and TF-IDF for document ranking and retrieval.

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies](#technologies)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Key Algorithms](#key-algorithms)
- [API Documentation](#api-documentation)

## 🎯 Overview

This IR project implements a search engine that retrieves and ranks documents based on user queries. It combines multiple ranking algorithms (BM25, TF-IDF) and includes intelligent query correction features using language models.

**Course**: Information Retrieval (IIITD, Sem 6, 2022)
**Project ID**: 31

## ✨ Features

- **BM25 Ranking**: State-of-the-art probabilistic ranking function
- **TF-IDF Ranking**: Classical term frequency-inverse document frequency scoring
- **Query Correction**: "Did you mean?" suggestions for misspelled queries
- **Advanced Filtering**: Filter results by difficulty level and other criteria
- **Django Web Interface**: User-friendly search interface
- **REST API**: RESTful API endpoints for programmatic access
- **Database Support**: SQLite for document storage and indexing

## 🛠️ Technologies

- **Backend Framework**: Django 4.0.4
- **API**: Django REST Framework 3.13.1
- **Authentication**: djangorestframework-simplejwt 4.8.0
- **Database**: SQLite3
- **Python Version**: 3.9+
- **Additional Libraries**:
  - django-environ (environment configuration)
  - coreapi, coreschema (API documentation)
  - defusedxml (security)

## 📁 Project Structure

```
IR_application/
├── config/                 # Django configuration
│   ├── host/              # Host-specific settings
│   └── local/             # Local development settings
├── frontend/              # Main IR application
│   ├── bm25.py           # BM25 ranking algorithm
│   ├── ranking.py        # Ranking implementations
│   ├── ranking2.py       # Alternative ranking approaches
│   ├── filter.py         # Result filtering logic
│   ├── forms.py          # Django forms
│   ├── views.py          # View controllers
│   ├── models.py         # Database models
│   ├── urls.py           # URL routing
│   └── migrations/       # Database migrations
├── static/               # Static assets
│   └── css/             # Stylesheets
├── templates/           # HTML templates
│   ├── frontpage.html
│   ├── resultpage.html
│   └── search_results.html
├── manage.py           # Django management script
└── db.sqlite3          # SQLite database

terminal/               # Jupyter notebooks for analysis
├── IR_Project.ipynb
├── IR_Project_Hits.ipynb
├── tf_idf.ipynb
└── ir_project.py
```

## 🚀 Installation

### Prerequisites
- Python 3.9 or higher
- pip or conda package manager

### Setup Steps

1. **Clone/Extract the repository**
   ```bash
   cd IR2022_project_31
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**
   ```bash
   cd IR_application
   python manage.py migrate
   ```

## 🏃 Running the Application

### Development Server

```bash
cd IR_application
python manage.py runserver
```

The application will be available at `http://localhost:8000`

### Using Gunicorn (Production)
```bash
gunicorn config.wsgi:application
```
(Note: Ensure gunicorn is in requirements.txt)

## 🔍 Key Algorithms

### BM25 Ranking
- Probabilistic ranking function based on the probability ranking principle
- Considers term frequency, inverse document frequency, and document length
- Located in: `frontend/bm25.py`

### TF-IDF Ranking
- Classical information retrieval scoring method
- Implementation in: `frontend/ranking.py` and `frontend/ranking2.py`

### Query Correction
- "Did you mean?" feature for misspelled queries
- Helps users find relevant documents even with typos

## 📊 Dataset

- **File**: `final_dataset.csv`
- **Database**: `db.sqlite3`
- Index file: `bm25.txt`

## 📝 Testing

Jupyter notebooks are provided for analysis and testing:
- `terminal/IR_Project.ipynb` - Main project analysis
- `terminal/IR_Project_Hits.ipynb` - Hit analysis and evaluation
- `terminal/tf_idf.ipynb` - TF-IDF algorithm testing
- `terminal/ir_project.py` - Standalone Python script

## 🔗 API Endpoints

The application provides Django REST Framework API endpoints. Key views are defined in `frontend/urls.py` and `frontend/views.py`.

## 📄 Configuration

- **Host Configuration**: `config/host/settings.py`
- **Local Configuration**: `config/local/settings.py`
- **Environment Variables**: Configured via `django-environ`

## 📦 Deployment

A `ProcFile` is included for Heroku deployment. Update as needed for your platform.

---

**Author**: Sushant Gupta (2022)
**Status**: Academic Project