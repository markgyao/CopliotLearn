-- Drop existing tables
DROP TABLE IF EXISTS student_homeworks;
DROP TABLE IF EXISTS student_tests;
DROP TABLE IF EXISTS tests;
DROP TABLE IF EXISTS homeworks;
DROP TABLE IF EXISTS classes;
DROP TABLE IF EXISTS teachers;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS permissions;

-- Create 'students' table
CREATE TABLE students (
    student_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    PRIMARY KEY (student_id)
);

-- Create 'teachers' table
CREATE TABLE teachers (
    teacher_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    PRIMARY KEY (teacher_id)
);

-- Create 'classes' table
CREATE TABLE classes (
    class_id INT NOT NULL AUTO_INCREMENT,
    class_name VARCHAR(50) NOT NULL,
    teacher_id INT NOT NULL,
    PRIMARY KEY (class_id),
    CONSTRAINT fk_teacher_class FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
);

-- Create 'homeworks' table
CREATE TABLE homeworks (
    homework_id INT NOT NULL AUTO_INCREMENT,
    class_id INT NOT NULL,
    due_date DATE NOT NULL,
    description TEXT,
    PRIMARY KEY (homework_id),
    CONSTRAINT fk_class_homework FOREIGN KEY (class_id) REFERENCES classes(class_id)
);

-- Create 'tests' table
CREATE TABLE tests (
    test_id INT NOT NULL AUTO_INCREMENT,
    class_id INT NOT NULL,
    category_id INT NOT NULL,  -- You may want to define categories as a separate table or ENUM
    PRIMARY KEY (test_id),
    CONSTRAINT fk_class_test FOREIGN KEY (class_id) REFERENCES classes(class_id)
);

-- Create 'student_tests' table
CREATE TABLE student_tests (
    student_id INT NOT NULL,
    test_id INT NOT NULL,
    score DECIMAL(5,2) NOT NULL,
    PRIMARY KEY (student_id, test_id),
    CONSTRAINT fk_student_test FOREIGN KEY (student_id) REFERENCES students(student_id),
    CONSTRAINT fk_test_student FOREIGN KEY (test_id) REFERENCES tests(test_id)
);

-- Create 'student_homeworks' table
CREATE TABLE student_homeworks (
    student_id INT NOT NULL,
    homework_id INT NOT NULL,
    submitted_date DATE,
    grade DECIMAL(5,2),
    PRIMARY KEY (student_id, homework_id),
    CONSTRAINT fk_student_homework FOREIGN KEY (student_id) REFERENCES students(student_id),
    CONSTRAINT fk_homework_student FOREIGN KEY (homework_id) REFERENCES homeworks(homework_id)
);

-- Create 'permissions' table
CREATE TABLE permissions (
    permission_id INT NOT NULL AUTO_INCREMENT,
    permission_name VARCHAR(50) NOT NULL,
    description TEXT,
    PRIMARY KEY (permission_id)
);

-- Create 'user_permissions' table to link users with permissions
CREATE TABLE user_permissions (
    user_id INT NOT NULL,
    permission_id INT NOT NULL,
    PRIMARY KEY (user_id, permission_id),
    CONSTRAINT fk_user_permission FOREIGN KEY (user_id) REFERENCES users(user_id),
    CONSTRAINT fk_permission_user FOREIGN KEY (permission_id) REFERENCES permissions(permission_id)
);
