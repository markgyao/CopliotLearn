-- Drop child tables first (if they exist)
DROP TABLE IF EXISTS student_homeworks;
DROP TABLE IF EXISTS student_tests;
DROP TABLE IF EXISTS test_details;
DROP TABLE IF EXISTS students_tests;
DROP TABLE IF EXISTS students_homeworks;
DROP TABLE IF EXISTS teachers_classes;
DROP TABLE IF EXISTS homeworks;
DROP TABLE IF EXISTS classes;
DROP TABLE IF EXISTS tests;
DROP TABLE IF EXISTS test_categories;
DROP TABLE IF EXISTS gallery;
DROP TABLE IF EXISTS role_permissions;
DROP TABLE IF EXISTS permissions;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS roles;

-- Create 'roles' table to define roles
CREATE TABLE roles (
    id INT NOT NULL AUTO_INCREMENT,
    role_name VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

-- Create 'users' table
CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT,
    last_name VARCHAR(50) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    role_id INT NOT NULL,
    created_at DATE, 
    updated_at DATE, 
    is_active BOOLEAN,
    PRIMARY KEY (id),
    CONSTRAINT fk_user_role FOREIGN KEY (role_id) REFERENCES roles(id)
);

-- Create 'permissions' table to define actions on resources
CREATE TABLE permissions (
    id INT NOT NULL AUTO_INCREMENT,
    permission_name VARCHAR(255) NOT NULL,
    description VARCHAR(255),
    resource VARCHAR(255) NOT NULL,  -- e.g., 'user', 'report', 'dashboard'
    action VARCHAR(50) NOT NULL,     -- e.g., 'create', 'read', 'update', 'delete'
    PRIMARY KEY (id)
);

-- Create 'role_permissions' table to link roles and permissions
CREATE TABLE role_permissions (
    id INT NOT NULL AUTO_INCREMENT,
    role_id INT NOT NULL,
    permission_id INT NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_role_permissions_role FOREIGN KEY (role_id) REFERENCES roles(id) ON DELETE CASCADE,
    CONSTRAINT fk_role_permissions_permission FOREIGN KEY (permission_id) REFERENCES permissions(id) ON DELETE CASCADE
);

-- Create 'test_categories' table to define test categories
CREATE TABLE test_categories (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,          -- test category EX: SHSAT, SAT, ACT, etc.
    subject VARCHAR(255) NOT NULL,       -- main subject like EX: Algebra, Geometry, etc.
    level VARCHAR(255) NOT NULL,         -- grade levels
    PRIMARY KEY (id)
);

-- Create 'tests' table to store test details
CREATE TABLE tests (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    category_id INT NOT NULL,
    test_file_path VARCHAR(255) NOT NULL,
    test_answer_file_path VARCHAR(255) NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_test_category FOREIGN KEY (category_id) REFERENCES test_categories(id) ON DELETE CASCADE
);

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
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    teacher_id INT NOT NULL,
    starting_date DATE NOT NULL,
    ending_date DATE NOT NULL,
    descriptions TEXT,
    subject VARCHAR(255) NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_teacher_class FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id) ON DELETE CASCADE
);

-- Create 'homeworks' table to store homework assignments
CREATE TABLE homeworks (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    class_id INT NOT NULL,
    description TEXT,
    due_date DATE NOT NULL,
    file_path VARCHAR(255) NOT NULL,
    answer_key_path VARCHAR(255),
    grade_level VARCHAR(20) NOT NULL,  -- specify which grade the homework is for
    PRIMARY KEY (id),
    CONSTRAINT fk_homeworks_class FOREIGN KEY (class_id) REFERENCES classes(id) ON DELETE CASCADE
);

-- Create 'teachers_classes' table to store which teacher teaches which classes
CREATE TABLE teachers_classes (
    id INT NOT NULL AUTO_INCREMENT,
    teacher_id INT NOT NULL,
    class_id INT NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_teachers_classes_teacher FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id) ON DELETE CASCADE,
    CONSTRAINT fk_teachers_classes_class FOREIGN KEY (class_id) REFERENCES classes(id) ON DELETE CASCADE
);

-- Create 'students_homeworks' table to store students' grades for homework
CREATE TABLE students_homeworks (
    id INT NOT NULL AUTO_INCREMENT,
    homework_id INT NOT NULL,
    student_id INT NOT NULL,
    grade DECIMAL(5,2) NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_students_homeworks_student FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    CONSTRAINT fk_students_homeworks_homework FOREIGN KEY (homework_id) REFERENCES homeworks(id) ON DELETE CASCADE
);

-- Create 'students_tests' table to store students' test results
CREATE TABLE students_tests (
    id INT NOT NULL AUTO_INCREMENT,
    student_id INT NOT NULL,
    test_id INT NOT NULL,
    test_date DATE NOT NULL,
    test_score DECIMAL(5,2) NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_students_tests_student FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    CONSTRAINT fk_students_tests_test FOREIGN KEY (test_id) REFERENCES tests(id) ON DELETE CASCADE
);

-- Create 'gallery' table to store images related to students
CREATE TABLE gallery (
    image_id INT NOT NULL AUTO_INCREMENT,
    student_id INT NOT NULL,
    image_path VARCHAR(255) NOT NULL,
    description TEXT,
    upload_date DATE NOT NULL,
    PRIMARY KEY (image_id),
    CONSTRAINT fk_gallery_student FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE
);

-- Create 'user_permissions' table to link users with permissions
CREATE TABLE user_permissions (
    user_id INT NOT NULL,
    permission_id INT NOT NULL,
    PRIMARY KEY (user_id, permission_id),
    CONSTRAINT fk_user_permission FOREIGN KEY (user_id) REFERENCES users(id),
    CONSTRAINT fk_permission_user FOREIGN KEY (permission_id) REFERENCES permissions(id)
);
