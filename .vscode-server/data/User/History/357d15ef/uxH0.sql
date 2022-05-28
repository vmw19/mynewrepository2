

-- Create a database table called "user":

CREATE TABLE user (
    id INTERGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    hobbies TEXT,
    active BOOLEAN DEFAULT 1
);


-- Dummy data to play with:

INSERT INTO user (
    first_name,
    last_name,
    hobbies
)

) VALUES (
    "Victoria",
    "Warren",
    "Poetry"
);

