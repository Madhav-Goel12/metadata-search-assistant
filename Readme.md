# 🔍 AI-Powered Metadata Search Assistant

An AI-powered Metadata Search Assistant that allows users to explore metadata extracted from multiple Kaggle datasets using natural language queries.

The application scans datasets, extracts metadata, stores it in SQLite, and provides a searchable interface built with FastAPI and Streamlit.

---

# 🚀 Features

- 📂 Browse multiple datasets
- 📊 Explore tables and column metadata
- 🔍 Search by database, table, or column name
- 🤖 AI-inspired Natural Language Search
- 🧠 Automatic keyword normalization
- 🔄 Refresh metadata catalog
- 📈 Dashboard statistics
- ⚡ FastAPI REST APIs
- 🎨 Interactive Streamlit UI

---

# 🛠️ Tech Stack

### Backend
- Python
- FastAPI
- SQLite
- Pandas

### Frontend
- Streamlit

### AI/NLP
- Rule-based Natural Language Processing
- Multi-keyword extraction
- Query normalization

### Tools
- Git
- GitHub
- VS Code

---

# 📁 Project Structure

```
SearchAssistant/
│
├── backend/
│   ├── routes/
│   ├── services/
│   ├── app.py
│   └── database.py
│
├── frontend/
│   └── app.py
│
├── datasets/
│   ├── Housing/
│   ├── Netflix/
│   ├── Spotify/
│   ├── Titanic/
│   └── Wine/
│
├── metadata/
│   └── metadata.db
│
├── scripts/
│
├── requirements.txt
│
└── README.md
```

---

# ⚙️ How It Works

## Step 1

The application scans Kaggle datasets.

↓

## Step 2

Metadata is extracted from every column including:

- Column Name
- Data Type
- Row Count
- Null Count
- Unique Count
- Sample Values
- Min/Max Values
- Memory Usage

↓

## Step 3

The extracted metadata is stored inside a SQLite database.

↓

## Step 4

FastAPI exposes REST APIs to access the metadata.

↓

## Step 5

Streamlit provides an interactive interface where users can:

- Browse databases
- View metadata
- Search using natural language

---

# 🔍 Example Searches

```
Find price
```

```
Where is price?
```

```
Show latitude and longitude
```

```
Find total bedrooms and rooms
```

```
Show ocean proximity
```

The system intelligently extracts relevant search terms and returns matching metadata.

---

# 📡 REST APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /stats | Dashboard statistics |
| GET | /search?keyword= | Search metadata |
| GET | /databases | List databases |
| GET | /databases/{database} | List tables |
| GET | /databases/columns/{table} | Column metadata |
| POST | /refresh | Refresh metadata catalog |

---

# 📸 Screenshots

## Dashboard

<img width="100%" src="screenshots/dashboard.png">

## Metadata Search

<img width="100%" src="screenshots/search.png">

## Search Results

<img width="100%" src="screenshots/results.png">

---

# 💡 Future Enhancements

- OpenAI Integration
- Ollama Integration
- Semantic Search using Embeddings
- Fuzzy Matching
- Voice Search
- Dataset Upload Support
- Metadata Visualization
- Authentication & User Management

---

# ▶️ Running the Project

## Install dependencies

```bash
pip install -r requirements.txt
```

## Start FastAPI

```bash
uvicorn backend.app:app --reload
```

## Start Streamlit

```bash
streamlit run frontend/app.py
```

---

# 📚 Datasets Used

- California Housing Dataset
- Netflix Movies & TV Shows
- Spotify Tracks Dataset
- Titanic Dataset
- Wine Reviews Dataset

(Source: Kaggle)

---

# 👨‍💻 Author

**Madhav Goel**

B.Tech Computer Science Engineering

Internship Project

---

# 📄 License

This project was developed as part of an internship for educational and learning purposes.
