### README.txt Mosh Olwuashina 101240184

# Fitness Tracking App Database Project

---

## Project Overview  
This project is a fitness tracking web application built using Flask and SQLite3. The application allows users to:  
1. **View all users and their workout logs**.  
2. **Add workout logs for specific users**.  
3. **Create and view exercises**.  
4. **Create and view workout routines**, demonstrating an **N:N relationship**.  
5. Easily navigate and interact with the database using a Flask-powered web interface.  

---

## Folder Structure
- **Project Directory**: `3005 Project 101240184 Mosh Oluwashina`
- **Database File**: `fitness_tracking_project.db`
- **Application File**: `app.py`
- **Templates Directory** (HTML Files):  
    - `templates/index.html` - Home Page  
    - `templates/users.html` - View all users  
    - `templates/logs.html` - View workout logs for a user  
    - `templates/add_log.html` - Add a workout log  
    - `templates/exercises.html` - View all exercises  
    - `templates/add_exercise.html` - Add a new exercise  
    - `templates/routines.html` - View workout routines  
    - `templates/add_routine.html` - Add a new routine  
    - `templates/routine_exercises.html` - View exercises within a routine (N:N relationship)  

---

## Database File Information
- **Filename**: `fitness_tracking_project.db`  
- **Location**: Root folder (`3005 Project 101240184 Mosh Oluwashina`)  

The database includes the following tables:  
1. **Users**: Stores user information.  
2. **Exercises**: Stores exercise details.  
3. **Workout_Routines**: Stores workout routines for users.  
4. **Routine_Exercises**: Manages the N:N relationship between routines and exercises.  
5. **Workout_Log**: Stores logs of user workouts.  

---

## Instructions to Run the Project

### Prerequisites  
1. Python 3 installed on your system.  
2. Flask installed (run this command if Flask is not installed):  
   ```bash
   pip install flask


##Steps to run
1. Open the terminal and navigate to the database location:
	- cd "3005 Project 101240184 Mosh Oluwashina"
2. Open SQLite with the database file:
	- sqlite3 fitness_tracking_project.db
3. Use these commands to interact with the database:
	- List all tables
		.tables  
	- View table schema
		.schema
	- Query database
		SELECT * FROM Users;
4. Run the flask app:
	python app.py
5. Open a web browser and navigate to:
	 http://127.0.0.1:5000


	



