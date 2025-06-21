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

