🚌 Student Transport Management System
This is a Flask web application designed to manage student transport logistics, including student registration, bus assignment, location tracking, and analytical visualization.

🔧 Features
Add, view, and delete student records with transport details.

Assign buses to students based on address.

Real-time GPS-based bus location tracking.

Analytical insights including:

Student type distribution (day scholars, hostelers, etc.)

Number of students per bus

Distribution of students by pickup address





Open Cmd inside this folder and run-

pip install Flask Flask-SQLAlchemy matplotlib

after run

python app.py

open server link on browser.


🚀 Project Workflow Overview
1. Startup and Database Initialization
When the application starts, it checks if the SQLite database student_transport.db exists.

If it doesn’t contain any students, it inserts sample data with predefined students, locations, and bus assignments.

This is done via db.create_all() and a conditional check on Student.query.count().

🧑‍🎓 Student Management
🔹 /busmodule — Manage Students
Displays all students.

You can add new students using a form (name, ID, type, address, bus assigned).

You can delete any student by their ID.

🔹 /add_student (POST)
Form submission route.

Saves a new student record to the database.

🔹 /delete_student/<id>
Deletes a student record using their ID.

🔹 /transportsystem
Displays all students in a read-only view (a transport manager view).

🧭 Real-Time Bus Tracking
🔹 /trackingsystem, /driver, /user
Separate views for:

Driver: Updates real-time GPS data of the bus via /update_location.

User: Views live location of the selected bus.

Tracking System: General map interface.

🔹 /update_location (POST)
Accepts JSON data from the driver (lat, lon, speed, heading, etc.).

Updates an in-memory dictionary bus_locations with live data.

🔹 /get_location/<bus_number>
Returns the latest location and metadata of a given bus.

🔹 /get_buses
Returns a list of all bus numbers being tracked.

🔹 /stop_sharing (POST)
Stops tracking a specific bus (removes it from bus_locations).

📊 Data Analysis and Charts
🔹 /analysis
Analyzes student data from the database:

Pie chart: Student type distribution (day scholars, hostelers, etc.)

Bar chart: Number of students per bus

Bar chart: Students per pickup address

Uses matplotlib to generate charts.

Charts are rendered as base64 images and embedded in the HTML.

🌐 Templates
Uses Jinja2 templating via Flask to render HTML pages like:

index.html — Home page

busmodule.html — Student management

trackingsystem.html — GPS tracking interface

analysis.html — Chart dashboard

driver.html / user.html — Role-specific views

💾 Data Storage
Uses SQLite with SQLAlchemy ORM.

Stores student details: name, student_id, type, address, bus_assigned.

📌 Summary
Feature	Description
Student Management	Add, delete, and list students
Bus Assignment	Assign buses based on student address/type
GPS Tracking	Real-time location updates and tracking
Data Visualization	Pie & bar charts showing system usage & insights
Roles	Different interfaces for drivers and users





Access Control-

Username- Avanthi.StudentTransportSystem
mail id- limir61296@firain.com
password- 6vngagkh)hz%9LL