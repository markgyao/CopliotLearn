-- Drop child tables first
DROP TABLE IF EXISTS student_test_history;
DROP TABLE IF EXISTS test_details;
DROP TABLE IF EXISTS tests;
DROP TABLE IF EXISTS test_categories;
DROP TABLE IF EXISTS students;

-- Create parent table 'students'
CREATE TABLE students (
    student_id INT NOT NULL AUTO_INCREMENT,
    last_name CHAR(50) NOT NULL,
    first_name CHAR(50) NOT NULL,
    phone CHAR(20) NOT NULL,
    email CHAR(50) NOT NULL,
    PRIMARY KEY (student_id)
);

-- Create parent table 'test_categories'
CREATE TABLE test_categories (
    test_category_id INT NOT NULL AUTO_INCREMENT,
    test_category_name CHAR(255),  -- test category EX: SHSAT, SAT, ACT, etc.
    test_subject CHAR(255),        -- main subject like EX: Algebra, Geometry, etc.
    test_subject2 CHAR(255),       -- detailed subjects EX: Polynomial graphing, etc.
    PRIMARY KEY (test_category_id)
);

-- Create 'tests' table which references 'test_categories'
CREATE TABLE tests (
    test_id INT NOT NULL AUTO_INCREMENT,
    test_name CHAR(50) NOT NULL,
    test_category_id INT NOT NULL,
    test_file_path CHAR(255) NOT NULL,
    PRIMARY KEY (test_id),
    CONSTRAINT fk_test_category FOREIGN KEY (test_category_id) REFERENCES test_categories(test_category_id)
);

-- Create 'test_details' table which references 'tests'
CREATE TABLE test_details (
    detail_id INT NOT NULL AUTO_INCREMENT,
    test_id INT NOT NULL,
    question_id INT NOT NULL,
    question_type CHAR(10),  -- Multiple_choice or other types
    question_answer_choice CHAR(255),
    question_answer_details CHAR(255),
    PRIMARY KEY (detail_id),
    CONSTRAINT fk_test FOREIGN KEY (test_id) REFERENCES tests(test_id)
);

-- Create 'student_test_history' table which references 'students' and 'tests'
CREATE TABLE student_test_history (
    history_id INT NOT NULL AUTO_INCREMENT,
    test_id INT NOT NULL,
    test_date DATE NOT NULL,
    student_id INT NOT NULL,
    test_score DOUBLE PRECISION NOT NULL,  -- type mapped from: DOUBLE
    PRIMARY KEY (history_id),
    CONSTRAINT fk_student FOREIGN KEY (student_id) REFERENCES students(student_id),
    CONSTRAINT fk_test_history FOREIGN KEY (test_id) REFERENCES tests(test_id)
);
