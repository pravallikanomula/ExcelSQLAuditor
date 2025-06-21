# 📊 Excel-to-SQL Visual Auditor

A Python-based tool to compare Excel files with SQL Server table data. It highlights differences such as new, missing, or modified rows and generates a color-coded audit report in Excel format.

---

## ✨ Features

- ✅ Load Excel files and SQL Server tables
- 🔍 Detect added, removed, or changed rows
- 🎨 Highlight differences in a generated Excel audit report
- 💬 CLI support with options like `--input`, `--table`, `--output`, `--dry-run`
- 🔐 Secure credentials using `.env` file
- 🛠 Optional GUI (coming soon)

---

## 🛠 Tech Stack

- **Python 3.8+**
- `pandas`, `pyodbc`, `openpyxl`, `xlsxwriter`
- `click` for CLI
- `python-dotenv` for environment management
- **SQL Server** (Docker or remote)

---

## 📂 Project Structure
excel_sql_auditor/
├── auditor.py # Main CLI entrypoint
├── db_utils.py # SQL Server connection logic
├── excel_utils.py # Excel loading and comparison logic
├── templates/ # Default Excel template (optional)
│ └── default_audit_template.xlsx
├── logs/ # Audit logs
├── .env # Your DB credentials (not checked in)
├── requirements.txt
└── README.md

---

## ⚙️ Setup Instructions

### 1. Clone the Repo & Set Up Environment


git clone https://github.com/pravallikanomula/ExcelSQLAuditor.git
cd ExcelSQLAuditor
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


### 2. Configure Environment Variables
Create a .env file in the root directory:

DB_DRIVER={ODBC Driver 17 for SQL Server}
DB_SERVER=localhost,1433
DB_DATABASE=your_database
DB_USER=sa
DB_PASSWORD=YourStrongP@ssw0rd


### 3. Start SQL Server (if using Docker)

docker run -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=YourStrongP@ssw0rd' \
   -p 1433:1433 --name sqlserver \
   -d mcr.microsoft.com/mssql/server:2022-latest

---

## 🚀 Usage
python auditor.py --input data.xlsx --table customer_data --output audit_report.xlsx --dry-run
CLI Options
Option	Description
--input	Path to the Excel file
--table	SQL Server table name
--output	Output Excel report path
--dry-run	Only preview changes, no database updates

---

## Output Example

The generated audit_report.xlsx will include:

Sheet 1: New Rows

Sheet 2: Missing Rows

Sheet 3: Changed Rows

Color-coded formatting helps highlight exact differences in cell values.

---

# 🛡️ License
This project is licensed under the MIT License.

