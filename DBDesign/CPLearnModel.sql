-- Drop child tables first
DROP TABLE IF EXISTS student_test_history;
DROP TABLE IF EXISTS test_details;
DROP TABLE IF EXISTS tests;
DROP TABLE IF EXISTS test_categories;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS question_topics;
DROP TABLE IF EXISTS grades;
DROP TABLE IF EXISTS homework;
DROP TABLE IF EXISTS gallery;
DROP TABLE IF EXISTS permissions;

-- Create parent table 'users'
CREATE TABLE users (
    user_id INT NOT NULL AUTO_INCREMENT,
    last_name VARCHAR(50) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    role ENUM('student', 'teacher', 'admin', 'parent') NOT NULL,
    PRIMARY KEY (user_id)
);

-- Create table 'test_categories' (can be useful for categorizing tests/homework)
CREATE TABLE test_categories (
    test_category_id INT NOT NULL AUTO_INCREMENT,
    test_category_name VARCHAR(255),  -- test category EX: SHSAT, SAT, ACT, etc.
    test_subject VARCHAR(255),        -- main subject like EX: Algebra, Geometry, etc.
    test_subject2 VARCHAR(255),       -- detailed subjects EX: Polynomial graphing, etc.
    PRIMARY KEY (test_category_id)
);

-- Create 'tests' table (for storing test details)
CREATE TABLE tests (
    test_id INT NOT NULL AUTO_INCREMENT,
    test_name VARCHAR(50) NOT NULL,
    test_category_id INT NOT NULL,
    test_file_path VARCHAR(255) NOT NULL,
    PRIMARY KEY (test_id),
    CONSTRAINT fk_test_category FOREIGN KEY (test_category_id) REFERENCES test_categories(test_category_id)
);

-- Create 'grades' table to store grades for students
CREATE TABLE grades (
    grade_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    subject VARCHAR(50) NOT NULL,
    grade DECIMAL(5,2) NOT NULL,
    PRIMARY KEY (grade_id),
    CONSTRAINT fk_grade_user FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Create 'homework' table to store homework assignments
CREATE TABLE homework (
    homework_id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    due_date DATE,
    file_path VARCHAR(255) NOT NULL,
    answer_key_path VARCHAR(255),
    grade_level VARCHAR(20),  -- specify which grade the homework is for
    PRIMARY KEY (homework_id)
);

-- Create 'question_topics' table to store topics for each question (if applicable)
CREATE TABLE question_topics (
    topic_id INT NOT NULL AUTO_INCREMENT,
    topic_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (topic_id)
);

-- Create 'test_details' table (kept for specific test questions if needed)
CREATE TABLE test_details (
    detail_id INT NOT NULL AUTO_INCREMENT,
    test_id INT NOT NULL,
    question_id INT NOT NULL,
    question_type VARCHAR(10),  -- Multiple_choice or other types
    question_answer_choice VARCHAR(255),
    question_answer_details VARCHAR(255),
    topic_id INT NOT NULL,
    PRIMARY KEY (detail_id),
    CONSTRAINT fk_test FOREIGN KEY (test_id) REFERENCES tests(test_id),
    CONSTRAINT fk_question_topic FOREIGN KEY (topic_id) REFERENCES question_topics(topic_id)
);

-- Create 'student_test_history' table to store students' test results
CREATE TABLE student_test_history (
    history_id INT NOT NULL AUTO_INCREMENT,
    test_id INT NOT NULL,
    test_date DATE NOT NULL,
    user_id INT NOT NULL,
    test_score DOUBLE PRECISION NOT NULL,  -- type mapped from: DOUBLE
    PRIMARY KEY (history_id),
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(user_id),
    CONSTRAINT fk_test_history FOREIGN KEY (test_id) REFERENCES tests(test_id)
);

-- Create 'gallery' table to store images related to students
CREATE TABLE gallery (
    image_id INT NOT NULL AUTO_INCREMENT,
    user_id INT,
    image_path VARCHAR(255) NOT NULL,
    description TEXT,
    upload_date DATE,
    PRIMARY KEY (image_id),
    CONSTRAINT fk_gallery_user FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Create 'permissions' table to manage permissions for users
CREATE TABLE permissions (
    permission_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    role ENUM('student', 'teacher', 'admin', 'parent') NOT NULL,
    can_read BOOLEAN NOT NULL DEFAULT 0,
    can_write BOOLEAN NOT NULL DEFAULT 0,
    PRIMARY KEY (permission_id),
    CONSTRAINT fk_permission_user FOREIGN KEY (user_id) REFERENCES users(user_id)
);
