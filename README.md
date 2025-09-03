# SMS Project (School Management System)

A simple **School Management System** built with **Django** and **MySQL**.

This project is designed to be **easy to set up on any machine** with minimal configuration. Currently, it includes:

- `config/` — Django project settings
- `core/` — Django app containing the `School` model
- MySQL integration

---

## Features

- Manage Schools with the following fields:
  - `id` (Primary Key, Auto-increment)
  - `name` (String)
  - `address` (Text)
  - `established_year` (Integer)
- Fully configured MySQL database connection
- Environment-based settings for security and flexibility
- Ready for development and collaboration with Git

---

## Prerequisites

- Python 3.13+
- MySQL 8+ installed (macOS via Homebrew )
- `pip` (Python package manager)
- Git

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/cole15sky/TechYatri-SMS.git
cd TechYatri-SMS

### 2. Create a virtual environment
python -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows

### 3. Install dependencies
pip install -r requirements.txt

### 4. Configure MySQL
brew services start mysql   # macOS
sudo systemctl start mysql  # Linux

