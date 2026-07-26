# 🩺 AI-Powered Medical Report Generator

An end-to-end AI-powered medical report generation system built with Python and FastAPI.

The project automatically generates realistic Complete Blood Count (CBC) reports, exports them in multiple formats, predicts possible medical conditions using Machine Learning, and exposes REST APIs for report management and AI analysis.

---

## Features

- AI-powered CBC condition prediction
- Automatic medical report generation
- PDF report generation
- JSON export
- CSV export
- QR Code generation
- Digital verification page
- REST API using FastAPI
- CRUD operations
- Pagination
- Filtering
- Sorting
- Report statistics
- Machine Learning integration
- Automated testing using Pytest
- GitHub Actions CI
- Docker support

---

## Tech Stack

- Python
- FastAPI
- Scikit-learn
- Pandas
- NumPy
- ReportLab
- QRCode
- Pytest
- Docker
- GitHub Actions

---

## Project Structure

```text
medical-report-generator/
│
├── src/
│   ├── api/
│   ├── ai/
│   ├── generators/
│   ├── analytics/
│   ├── pdf/
│   ├── security/
│   ├── verification/
│   └── models/
│
├── tests/
├── assets/
├── data/
├── output/
│
├── Dockerfile
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/SyedMubeenAli/medical-report-generator.git
```

Move into the project

```bash
cd medical-report-generator
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the API

```bash
uvicorn src.api.main:app --reload
```

---

## API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## Running Tests

```bash
pytest
```

---

## Docker

Build

```bash
docker build -t medical-report-generator .
```

Run

```bash
docker run -p 8000:8000 medical-report-generator
```

---

## Machine Learning

The project includes a Random Forest classifier trained on synthetic CBC data to predict possible medical conditions.

The trained model is integrated with the FastAPI backend and exposed through REST APIs.

---

## Continuous Integration

GitHub Actions automatically:

- Install dependencies
- Run tests
- Validate every push

---

## Future Improvements

- User authentication
- Database integration
- Cloud deployment
- Multi-language reports
- Medical image analysis
- Dashboard

---

## Author

**Syed Mubeen Ali**

GitHub

https://github.com/SyedMubeenAli

LinkedIn

https://www.linkedin.com/in/syedmubeenali2k17/