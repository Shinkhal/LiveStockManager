# 🐄 Livestock Manager

A complete livestock management system built with **Django**.  
It helps farmers manage animals, vaccinations, reminders, and health records — all in one place.

---

## 🚀 Features

✅ User Authentication (Register/Login/Logout)  
✅ Owner Profile Linked to Django User  
✅ Add, Edit & Delete Animals  
✅ Add, Edit & Delete Vaccinations  
✅ Dashboard Overview  
✅ Upcoming Vaccination Reminders  
✅ Overdue Alerts  
✅ Modern clean UI  
✅ Fully responsive  
✅ Date picker support  
✅ Secure per-user data access  
✅ Beautiful card-based dashboard  

---

## 📸 Screenshots
<img width="1920" height="1080" alt="Screenshot (66)" src="https://github.com/user-attachments/assets/4ee4a100-4801-4a4b-8211-0d7471eff47e" />


---

## 🏗️ Tech Stack

**Frontend**
- HTML5
- CSS3
- Icons & Emojis
- Responsive styling

**Backend**
- Python 3.x
- Django 5.x

**Database**
- SQLite (default)

---

## 📦 Installation

Follow the steps to run this project locally:

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Shinkhal/LiveStockManager.git
cd LiveStockManager
````

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
source venv/Scripts/activate      # Windows
# or
source venv/bin/activate          # macOS/Linux
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` not created, run:

```bash
pip freeze > requirements.txt
```

### 4️⃣ Run migrations

```bash
python manage.py migrate
```

### 5️⃣ Start development server

```bash
python manage.py runserver
```

Now open:

👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---


## 📁 Project Structure

```
/core
    /templates/core
    /static/core
    models.py
    views.py
    forms.py
    urls.py

livestock_manager
    settings.py
    urls.py

README.md
manage.py
```

---

## 💡 Why This Project is Useful

This system helps streamline livestock management:

* Saves time
* Prevents lost vaccination records
* Easy monitoring
* Owner-based security
* Minimal UI + powerful backend

---

## 🤝 Contributing

Pull requests are welcome!
For major changes, please open an issue first to discuss what you'd like to change.

---

## ⚖️ License

MIT License 

---

# 🎉 Thank You!

If you liked this project, consider giving it a ⭐ on GitHub.
