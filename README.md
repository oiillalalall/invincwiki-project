# 🦸‍♂️ Invinwiki

Welcome to the **Invincible Universe Database**! This is a dynamic, full-stack web application designed to track, manage, and explore everything related to the *Invincible* comic series and animated television show. From characters and factions to multi-dimensional story arcs and superpowers, this app serves as the ultimate digital encyclopedia.

---

## 🚀 Features

* **Dynamic Data Management:** Seamlessly add, update, and manage entries for Seasons, Episodes, Comics, Characters, Organizations, Species, Weapons, and Story Arcs.
* **Smart Forms:** Utilizes dynamic Jinja2 templating with automated form generation driven by `WTForms`.
* **File Upload Integration:** Support for uploading character avatars, comic issue cover arts, and story arc promotional images via `multipart/form-data`.
* **Security First:** Implements built-in **CSRF protection tokens** (`hidden_tag()`) across all data submission forms to protect the database backend from malicious scripts.
* **Modern UI:** Built using an *Invincible*-themed custom yellow and blue color scheme, fully responsive via modern utility classes.

---

## 🛠️ Tech Stack

* **Backend:** Python (Flask / FastAPI)
* **Frontend:** HTML5, Jinja2 Templating Engine, Bootstrap 5 (or custom CSS framework)
* **Form Management:** WTForms
* **Database:** SQL-based Relational Database (PostgreSQL / SQLite / MySQL)

---

## 📂 Project Structure

```text
├── app/
│   ├── models/          # Database structural models (Seasons, Powers, etc.)
│   ├── routes/          # Form submit routers and view endpoints
│   ├── templates/       # Jinja2 HTML templates (Add forms, View lists)
│   └── static/          # Images, custom styles, and configurations
├── README.md
└── requirements.txt     # Python environment dependencies
