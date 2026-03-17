# 🌙 NightNotes

NightNotes is a simple and elegant Django web application designed to capture late-night thoughts, reflections, and ideas.
Users can create, organize, and revisit notes while attaching emotional context through moods and categories.

The project focuses on **clean UI, structured data organization, and user-friendly note management**.

---

##  Features

###  Notes Management

* Create notes
* Edit existing notes
* Delete notes
* View detailed note pages

###  Categories

* Organize notes by category
* Add and delete categories
* Category descriptions for better organization

###  Mood Library

* Attach multiple moods to each note
* Starter moods included
* Add custom moods
* Delete moods from the library

###  Favorites

* Mark notes as favorite
* View all favorite notes in one place

###  Search & Filtering

* Search notes by title
* Filter notes by category
* Filter notes by mood

### UI / UX Improvements

* Dark / Light mode toggle
* Responsive centered layout
* Card-based note display
* Hover animations
* Floating "Create Note" button
* Smooth theme transitions

### Error Handling

* Custom 404 page
(loads only in debug=False for now)

---

##  Built With

* **Python**
* **Django**
* **HTML5**
* **CSS3**
* **Django Templates**

---

## Project Structure

```
nightnotes/
│
├── notes/          # Notes app (CRUD operations)
├── categories/     # Categories management
├── moods/          # Mood library
├── templates/      # HTML templates
├── static/         # CSS and static files
└── manage.py
```

---

## How to Install

1. Clone the repository

```
git clone https://github.com/YOUR_USERNAME/nightnotes.git
```

2. Navigate into the project

```
cd nightnotes
```

3. Create virtual environment

```bash
python -m venv venv
```

4. Activate it

Windows

```
venv\Scripts\activate
```

Mac / Linux

```bash
source venv/bin/activate
```

5. Install dependencies

```
pip install django
```

8. Run migrations

```
python manage.py migrate
```

7. Start the development server

```
python manage.py runserver
```

8. Open in browser

```
http://127.0.0.1:8000
```
##  Future Improvements

Possible future features:

* User authentication system
* Personal accounts
* Note sharing
* Tags system
* Rich text editor
* Search suggestions
* Pagination
* REST API support
* Mobile-friendly UI improvements

---

##  Learning Goals

This project helped me practice:

* Django Models
* Django CRUD operations
* Django Class-Based Views
* Django Forms
* Template inheritance
* Static files management
* UI/UX improvements
* Light/Dark theme implementation

---

##  Author

Developed as a **Django learning project and portfolio application**.

---

## License

This project is open-source and available under the MIT License.
