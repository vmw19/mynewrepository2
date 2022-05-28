

-- Create a database table called "user":

CREATE TABLE user (
    id INTERGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    hobbies TEXT,
)