DROP TABLE IF EXISTS subjects;

CREATE TABLE subjects(
    id serial PRIMARY KEY,
    subject VARCHAR(50)
);

COPY subjects FROM '/Users/annascriven/projects/Week4/day3/flask_postgres_school/data/subjects.csv' DELIMITER ',' CSV HEADER;

DROP TABLE IF EXISTS student;

CREATE TABLE student(
    id serial PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    age INT,
    subject INT,
    FOREIGN KEY(subject) REFERENCES subjects(id)
);


COPY student FROM '/Users/annascriven/projects/Week4/day3/flask_postgres_school/data/student.csv' DELIMITER ',' CSV HEADER;

DROP TABLE IF EXISTS teachers;

CREATE TABLE teachers(
    id serial PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    age INT,
    subject INT,
    FOREIGN KEY(subject) REFERENCES subjects(id)
);

-- COPY student FROM '/Users/annascriven/projects/Week4/day3/flask_postgres_school/data/student.csv' DELIMITER ',' CSV HEADER;
-- COPY subjects FROM '/Users/annascriven/projects/Week4/day3/flask_postgres_school/data/subjects.csv' DELIMITER ',' CSV HEADER;
COPY teachers FROM '/Users/annascriven/projects/Week4/day3/flask_postgres_school/data/teachers.csv' DELIMITER ',' CSV HEADER;

SELECT * FROM student;
SELECT * FROM subjects;
SELECT * FROM teachers;