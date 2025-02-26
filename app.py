import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Path to your SQLite database
DB_PATH = "fitness_tracking_project.db"

# Home Page
@app.route("/")
def index():
    return render_template("index.html")

# View All Users
@app.route("/users")
def users():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users")
    users = cursor.fetchall()
    conn.close()
    return render_template("users.html", users=users)

# Add a New User
@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        subscription_type = request.form["subscription_type"]
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Users (username, email, subscription_type, join_date)
            VALUES (?, ?, ?, DATE('now'))
        """, (username, email, subscription_type))
        conn.commit()
        conn.close()
        return redirect("/users")
    return render_template("add_user.html")

# View Logs for a Specific User
@app.route("/logs/<int:user_id>")
def logs(user_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT log_date, sets, reps, weight, Exercises.exercise_name
        FROM Workout_Log
        JOIN Exercises ON Workout_Log.exercise_id = Exercises.exercise_id
        WHERE Workout_Log.user_id = ?
    """, (user_id,))
    logs = cursor.fetchall()
    print(f"Logs for user {user_id}: {logs}")  # Debugging statement
    conn.close()
    return render_template("logs.html", logs=logs, user_id=user_id)


# Add a New Workout Log
@app.route("/add_log/<int:user_id>", methods=["GET", "POST"])
def add_log(user_id):
    if request.method == "POST":
        exercise_id = request.form["exercise_id"]
        log_date = request.form["log_date"]
        sets = request.form["sets"]
        reps = request.form["reps"]
        weight = request.form["weight"]
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Workout_Log (user_id, exercise_id, log_date, sets, reps, weight)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (user_id, exercise_id, log_date, sets, reps, weight))
        conn.commit()
        conn.close()
        return redirect(f"/logs/{user_id}")
    return render_template("add_log.html", user_id=user_id)

# View All Exercises
@app.route("/exercises")
def exercises():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Exercises")
    exercises = cursor.fetchall()
    conn.close()
    return render_template("exercises.html", exercises=exercises)

# Add a New Exercise
@app.route("/add_exercise", methods=["GET", "POST"])
def add_exercise():
    if request.method == "POST":
        exercise_name = request.form["exercise_name"]
        muscle_group = request.form["muscle_group"]
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Exercises (exercise_name, muscle_group)
            VALUES (?, ?)
        """, (exercise_name, muscle_group))
        conn.commit()
        conn.close()
        return redirect("/exercises")
    return render_template("add_exercise.html")

# View All Workout Routines
@app.route("/routines")
def routines():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT Workout_Routines.routine_id, Users.username, Workout_Routines.routine_name, Workout_Routines.start_date
        FROM Workout_Routines
        JOIN Users ON Workout_Routines.user_id = Users.user_id
    """)
    routines = cursor.fetchall()
    conn.close()
    return render_template("routines.html", routines=routines)

# Add a New Workout Routine
@app.route("/add_routine/<int:user_id>", methods=["GET", "POST"])
def add_routine(user_id):
    if request.method == "POST":
        routine_name = request.form["routine_name"]
        start_date = request.form["start_date"]
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Workout_Routines (user_id, routine_name, start_date)
            VALUES (?, ?, ?)
        """, (user_id, routine_name, start_date))
        conn.commit()
        conn.close()
        return redirect("/routines")
    return render_template("add_routine.html", user_id=user_id)

# View Exercises in a Routine
@app.route("/routine_exercises/<int:routine_id>")
def routine_exercises(routine_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT Exercises.exercise_name, Routine_Exercises.sets, Routine_Exercises.reps, Routine_Exercises.weight
        FROM Routine_Exercises
        JOIN Exercises ON Routine_Exercises.exercise_id = Exercises.exercise_id
        WHERE Routine_Exercises.routine_id = ?
    """, (routine_id,))
    exercises = cursor.fetchall()
    conn.close()
    return render_template("routine_exercises.html", exercises=exercises, routine_id=routine_id)

if __name__ == "__main__":
    app.run(debug=True)

