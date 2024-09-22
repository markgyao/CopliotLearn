
DROP TABLE IF EXISTS students_homeworks;
DROP TABLE IF EXISTS students_tests;
DROP TABLE IF EXISTS homeworks;
DROP TABLE IF EXISTS classes;
DROP TABLE IF EXISTS tests;
DROP TABLE IF EXISTS gallery;
DROP TABLE IF EXISTS role_permissions;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS permissions;
DROP TABLE IF EXISTS roles;
DROP TABLE IF EXISTS test_categories;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS teachers;

-- Create 'roles' table to define roles
CREATE TABLE roles (
    id INT NOT NULL AUTO_INCREMENT,
    role_name VARCHAR(50) NOT NULL,

    PRIMARY KEY (id),
    UNIQUE (role_name)
);

-- Create 'permissions' table to define actions on resources
CREATE TABLE permissions (
    id INT NOT NULL AUTO_INCREMENT,
    permission_name VARCHAR(255) NOT NULL,
    description VARCHAR(255),
    resource VARCHAR(255) NOT NULL,  -- e.g., 'user', 'report', 'dashboard'
    action VARCHAR(50) NOT NULL,     -- e.g., 'create', 'read', 'update', 'delete'

    PRIMARY KEY (id),
    UNIQUE (permission_name)

);

-- Create 'role_permissions' table to link roles and permissions
CREATE TABLE role_permissions (
    role_id INT NOT NULL,
    permission_id INT NOT NULL,

    PRIMARY KEY (role_id, permission_id),
    CONSTRAINT fk_role_permissions_role FOREIGN KEY (role_id) REFERENCES roles(id) ON DELETE CASCADE,
    CONSTRAINT fk_role_permissions_permission FOREIGN KEY (permission_id) REFERENCES permissions(id) ON DELETE CASCADE
);

-- Create 'users' table
CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT,
    account_id VARCHAR(255) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    phone VARCHAR(50),
    email VARCHAR(100) NOT NULL,
    wechat_id VARCHAR(50),
    password_hash VARCHAR(255) NOT NULL, -- updated field for clarity
    role_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

    is_active BOOLEAN,

    PRIMARY KEY (id),
    UNIQUE (account_id),
    UNIQUE (email),
    CONSTRAINT fk_user_role FOREIGN KEY (role_id) REFERENCES roles(id) ON DELETE CASCADE
);


-- Create 'test_categories' table to define test categories
CREATE TABLE test_categories (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,          -- test category EX: SHSAT, SAT, ACT, etc.
    subject VARCHAR(255) NOT NULL,       -- main subject like EX: Algebra, Geometry, etc.
    level VARCHAR(255),         -- grade levels
    PRIMARY KEY (id)
);

-- Create 'tests' table to store test details
CREATE TABLE tests (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    category_id INT NOT NULL,
    description TEXT,
    test_content TEXT,
    test_file_path VARCHAR(255),
    test_answer_file_path VARCHAR(255),

    PRIMARY KEY (id),
    CONSTRAINT fk_test_category FOREIGN KEY (category_id) REFERENCES test_categories(id) ON DELETE CASCADE
);


-- Create 'classes' table
CREATE TABLE classes (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    teacher_id INT,
    starting_date DATE NOT NULL,
    ending_date DATE NOT NULL,
    descriptions TEXT,
    subject VARCHAR(255) NOT NULL,

    PRIMARY KEY (id),
    CONSTRAINT fk_teacher_class FOREIGN KEY (teacher_id) REFERENCES users(id) ON DELETE SET NULL -- updated from CASCADE to SET NULL
);


-- Create 'homeworks' table to store homework assignments
CREATE TABLE homeworks (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    class_id INT NOT NULL,
    description TEXT,
    homework_content TEXT,
    due_date DATE,
    file_path VARCHAR(255),
    answer_key_path VARCHAR(255),
    grade_level VARCHAR(20),  -- specify which grade the homework is for
    PRIMARY KEY (id),
    CONSTRAINT fk_homeworks_class FOREIGN KEY (class_id) REFERENCES classes(id) ON DELETE CASCADE
);


-- Create 'students_homeworks' table to store students' grades for homework
CREATE TABLE students_homeworks (
    student_id INT NOT NULL,
    homework_id INT NOT NULL,
    grade DECIMAL(5,2) NOT NULL,
    submitted_date DATE NOT NULL,  -- added for tracking submission date
    PRIMARY KEY (student_id,homework_id),
    CONSTRAINT fk_students_homeworks_student FOREIGN KEY (student_id) REFERENCES users(id) ON DELETE CASCADE,
    CONSTRAINT fk_students_homeworks_homework FOREIGN KEY (homework_id) REFERENCES homeworks(id) ON DELETE CASCADE
);


-- Create 'students_tests' table to store students' test results
CREATE TABLE students_tests (
    student_id INT NOT NULL,
    test_id INT NOT NULL,
    test_date DATE NOT NULL,
    test_score DECIMAL(5,2) NOT NULL,
    PRIMARY KEY (student_id,test_id),
    CONSTRAINT fk_students_tests_student FOREIGN KEY (student_id) REFERENCES users(id) ON DELETE CASCADE,
    CONSTRAINT fk_students_tests_test FOREIGN KEY (test_id) REFERENCES tests(id) ON DELETE CASCADE
);


-- Create 'gallery' table to store images related to students
CREATE TABLE gallery (
    image_id INT NOT NULL AUTO_INCREMENT,
    student_id INT NOT NULL,
    image_path VARCHAR(255) NOT NULL,
    description TEXT,
    upload_date DATE NOT NULL,
    image_title VARCHAR(100),  -- optional field for image title or categorization
    PRIMARY KEY (image_id),
    CONSTRAINT fk_gallery_student FOREIGN KEY (student_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE INDEX idx_student_id ON students_homeworks(student_id);
CREATE INDEX idx_test_id ON students_tests(test_id);
CREATE INDEX idx_class_id ON homeworks(class_id);