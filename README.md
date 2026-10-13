
# Data Redundancy Removal System

A Flask and MySQL-based web application that validates incoming data, detects duplicate entries, and stores only unique, verified records in a cloud database.

## Features

- **Data Validation:** Rejects empty or whitespace-only inputs.
- **Duplicate Detection:** Uses SHA-256 hashing to identify duplicate data.
- **Data Normalization:** Removes extra whitespace before comparison.
- **Cloud Database:** Stores records in Aiven MySQL.
- **Web Interface:** Simple interface for submitting data and viewing results.
- **Cloud Deployment:** Hosted on Render.

## Technology Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, Flask
- **Database:** MySQL (Aiven Cloud)
- **Deployment:** Render
- **Version Control:** Git and GitHub

## How It Works

1. The user submits data through the web interface.
2. The system validates the input.
3. Extra whitespace is normalized.
4. A SHA-256 hash is generated.
5. The database is checked for an existing hash.
6. Duplicate entries are rejected; unique entries are stored in the database.

## Project Links

- **GitHub Repository:** https://github.com/SomaSundari890/data-redundancy-removal
- **Live Application:** https://data-redundancy-removal.onrender.com/.

## Local Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/SomaSundari890/data-redundancy-removal.git
   cd data-redundancy-removal
   ```

2. Create and activate a virtual environment.

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure the required database environment variables in a `.env` file.

5. Run the application:

   ```bash
   python app.py
   ```

6. Open `http://127.0.0.1:5000` in your browser.

## Security

- Database credentials are stored in environment variables.
- The `.env` file is excluded from Git using `.gitignore`.
- Never commit passwords, tokens, or other secrets.

## Future Enhancements

- Similarity-based duplicate detection.
- Improved classification of false positives.
- Detailed validation and audit logs.
- Enhanced error handling and reporting.

## Author

Developed as an internship project.
