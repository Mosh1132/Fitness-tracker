-- Users Table
CREATE TABLE Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    subscription_type TEXT,
    join_date DATE
);

-- Exercises Table
CREATE TABLE Exercises (
    exercise_id INTEGER PRIMARY KEY AUTOINCREMENT,
    exercise_name TEXT NOT NULL,
    muscle_group TEXT NOT NULL
);

-- Workout_Routines Table
CREATE TABLE Workout_Routines (
    routine_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    routine_name TEXT NOT NULL,
    start_date DATE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Routine_Exercises Table (N:N Relationship)
CREATE TABLE Routine_Exercises (
    routine_id INTEGER NOT NULL,
    exercise_id INTEGER NOT NULL,
    sets INTEGER NOT NULL,
    reps INTEGER NOT NULL,
    weight REAL NOT NULL,
    PRIMARY KEY (routine_id, exercise_id),
    FOREIGN KEY (routine_id) REFERENCES Workout_Routines(routine_id),
    FOREIGN KEY (exercise_id) REFERENCES Exercises(exercise_id)
);

-- Workout_Log Table
CREATE TABLE Workout_Log (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    exercise_id INTEGER NOT NULL,
    log_date DATE NOT NULL,
    sets INTEGER NOT NULL,
    reps INTEGER NOT NULL,
    weight REAL NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (exercise_id) REFERENCES Exercises(exercise_id)
);

-- User_Exercises Table (Optional Explicit N:N Relationship)
CREATE TABLE User_Exercises (
    user_id INTEGER NOT NULL,
    exercise_id INTEGER NOT NULL,
    PRIMARY KEY (user_id, exercise_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (exercise_id) REFERENCES Exercises(exercise_id)
);
