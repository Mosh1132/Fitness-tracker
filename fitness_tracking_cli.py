import sqlite3
from datetime import date

# Connect to the database
DB_PATH = "/home/mosh/3005 Project 101240184 Mosh Oluwashina/fitness_tracking_project.db"
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

def display_menu():
    print("\n===== Fitness Tracking App CLI =====")
    print("1. Add a new user")
    print("2. Add a new routine")
    print("3. Add a workout log")
    print("4. View all exercises in a routine")
    print("5. View user progress for an exercise")
    print("6. Search exercises by muscle group")
    print("7. Exit")
    choice = input("Select an option: ")
    return choice

def add_user():
    username = input("Enter username: ")
    email = input("Enter email: ")
    subscription_type = input("Enter subscription type (Basic/Premium): ")
    join_date = date.today().strftime("%Y-%m-%d")
    cursor.execute("""
        INSERT INTO Users (username, email, subscription_type, join_date)
        VALUES (?, ?, ?, ?)
    """, (username, email, subscription_type, join_date))
    conn.commit()
    print("User added successfully!")

def add_routine():
    user_id = input("Enter user ID: ")
    routine_name = input("Enter routine name: ")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    cursor.execute("""
        INSERT INTO Workout_Routines (user_id, routine_name, start_date)
        VALUES (?, ?, ?)
    """, (user_id, routine_name, start_date))
    conn.commit()
    print("Routine added successfully!")

def add_workout_log():
    user_id = input("Enter user ID: ")
    exercise_id = input("Enter exercise ID: ")
    log_date = input("Enter log date (YYYY-MM-DD): ")
    sets = input("Enter number of sets: ")
    reps = input("Enter number of reps: ")
    weight = input("Enter weight lifted: ")
    cursor.execute("""
        INSERT INTO Workout_Log (user_id, exercise_id, log_date, sets, reps, weight)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (user_id, exercise_id, log_date, sets, reps, weight))
    conn.commit()
    print("Workout log added successfully!")

def view_exercises_in_routine():
    routine_id = input("Enter routine ID: ")
    cursor.execute("""
        SELECT Exercises.exercise_name, Routine_Exercises.sets, Routine_Exercises.reps, Routine_Exercises.weight
        FROM Routine_Exercises
        JOIN Exercises ON Routine_Exercises.exercise_id = Exercises.exercise_id
        WHERE Routine_Exercises.routine_id = ?
    """, (routine_id,))
    results = cursor.fetchall()
    if results:
        print("\nExercises in Routine:")
        for row in results:
            print(f"Exercise: {row[0]}, Sets: {row[1]}, Reps: {row[2]}, Weight: {row[3]} lbs")
    else:
        print("No exercises found for this routine.")

def view_user_progress():
    user_id = input("Enter user ID: ")
    exercise_id = input("Enter exercise ID: ")
    cursor.execute("""
        SELECT log_date, sets, reps, weight
        FROM Workout_Log
        WHERE user_id = ? AND exercise_id = ?
        ORDER BY log_date
    """, (user_id, exercise_id))
    results = cursor.fetchall()
    if results:
        print("\nProgress for Exercise:")
        for row in results:
            print(f"Date: {row[0]}, Sets: {row[1]}, Reps: {row[2]}, Weight: {row[3]} lbs")
    else:
        print("No logs found for this user and exercise.")

def search_exercises():
    muscle_group = input("Enter muscle group to search for (e.g., Chest, Legs): ")
    cursor.execute("""
        SELECT exercise_name
        FROM Exercises
        WHERE muscle_group = ?
    """, (muscle_group,))
    results = cursor.fetchall()
    if results:
        print("\nExercises in Muscle Group:")
        for row in results:
            print(row[0])
    else:
        print("No exercises found for this muscle group.")

def main():
    while True:
        choice = display_menu()
        if choice == "1":
            add_user()
        elif choice == "2":
            add_routine()
        elif choice == "3":
            add_workout_log()
        elif choice == "4":
            view_exercises_in_routine()
        elif choice == "5":
            view_user_progress()
        elif choice == "6":
            search_exercises()
        elif choice == "7":
            print("Exiting... Goodbye!")
            conn.close()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
