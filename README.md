# Django Notes App 📝

A simple and clean web application for creating, viewing, editing, and deleting personal notes.  
Built with **Django** and styled with **Bootstrap**, this app demonstrates full CRUD functionality using Django’s MVC architecture.

---

## 🚀 Features

- 🆕 Create new notes
- 📋 View a list of all saved notes
- 🔍 See full details of a single note
- ✏️ Edit existing notes
- ❌ Delete notes

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Database:** SQLite (default Django DB)

---

## 📸 Screenshots

*You can add screenshots here later after deploying or running locally.*

---

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/django-notes-app.git
cd django-notes-app




Create and activate a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate


Install dependencies
	•	Pipfile
	•	Pipfile.lock


Run migrations and start the server
python manage.py migrate
python manage.py runserver


Folder Structure
notes_project/
├── notes_app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   └── notes_app/
│   │       ├── base.html
│   │       ├── notes_list.html
│   │       ├── note_detail.html
│   │       └── note_form.html
├── notes_project/
│   ├── settings.py
│   └── urls.py

