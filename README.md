# 📝 Flask Task Manager

A simple Task Manager web application built with **Flask**, **SQLite**, and **SQLAlchemy**.  
It allows users to add, edit, and delete tasks with a clean interface.

## 🚀 Features
- Add new tasks  
- Edit existing tasks  
- Delete tasks  
- Store tasks in a SQLite database  
- Simple and clean UI with CSS styling


⚙️ Installation & Running Locally
1️⃣ Clone the repository
git clone https://github.com/your-username/flask-task-manager.git
cd flask-task-manager

2️⃣ Create and activate a virtual environment (recommended)
python -m venv venv


Activate it:

Windows (PowerShell)

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Initialize the database

Run the following in Python shell (only first time):

python
>>> from app import db
>>> db.create_all()
>>> exit()

5️⃣ Run the application
python app.py

6️⃣ Open in browser

Go to:

http://127.0.0.1:5000/








