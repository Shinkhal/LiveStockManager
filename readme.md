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

> Add your project screenshots here after running locally.

```

/screenshots/homepage.png
/screenshots/login.png
/screenshots/dashboard.png

````

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
git clone https://github.com/your-username/livestock-manager.git
cd livestock-manager
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

## 🧪 Test Credentials

(Optional)
You can include demo credentials if presenting the project:

```
Username: demo
Password: demo123
```

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

## ✅ Improvements to Add (Future Scope)

✅ Upload photos for animals
✅ Vaccination certificates (PDF export)
✅ Email/SMS reminders
✅ Graphs and analytics (Chart.js)
✅ Animal health history
✅ Multi-farm support
✅ Dark mode

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

MIT License (optional)

---

# 🎉 Thank You!

If you liked this project, consider giving it a ⭐ on GitHub.
