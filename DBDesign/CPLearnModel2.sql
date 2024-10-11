
-- DROP TABLE IF EXISTS students_homeworks;
-- DROP TABLE IF EXISTS students_tests;
-- DROP TABLE IF EXISTS homeworks;
-- DROP TABLE IF EXISTS students;
-- DROP TABLE IF EXISTS class_schedules;
-- DROP TABLE IF EXISTS classes;
-- DROP TABLE IF EXISTS tests;
-- DROP TABLE IF EXISTS gallery;
-- DROP TABLE IF EXISTS role_permissions;
-- DROP TABLE IF EXISTS users;
-- DROP TABLE IF EXISTS permissions;
-- DROP TABLE IF EXISTS roles;
-- DROP TABLE IF EXISTS test_categories;

-- cplearn_test.permissions definition

CREATE TABLE `permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `permission_name` varchar(255) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `resource` varchar(255) NOT NULL,
  `action` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `permission_name` (`permission_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf32 COLLATE=utf32_general_ci;


-- cplearn_test.roles definition

CREATE TABLE `roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `role_name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `role_name` (`role_name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf32 COLLATE=utf32_general_ci;


-- cplearn_test.test_categories definition

CREATE TABLE `test_categories` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `subject` varchar(255) NOT NULL,
  `level` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf32 COLLATE=utf32_general_ci;


-- cplearn_test.role_permissions definition

CREATE TABLE `role_permissions` (
  `role_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`role_id`,`permission_id`),
  KEY `fk_role_permissions_permission` (`permission_id`),
  CONSTRAINT `fk_role_permissions_permission` FOREIGN KEY (`permission_id`) REFERENCES `permissions` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_role_permissions_role` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf32 COLLATE=utf32_general_ci;


-- cplearn_test.tests definition

CREATE TABLE `tests` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `category_id` int(11) NOT NULL,
  `description` text DEFAULT NULL,
  `test_content` text DEFAULT NULL,
  `test_file_path` varchar(255) DEFAULT NULL,
  `test_answer_file_path` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_test_category` (`category_id`),
  CONSTRAINT `fk_test_category` FOREIGN KEY (`category_id`) REFERENCES `test_categories` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf32 COLLATE=utf32_general_ci;


-- cplearn_test.users definition

CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `role_id` int(11) NOT NULL,
  `account_id` varchar(255) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `wechat_id` varchar(50) DEFAULT NULL,
  `password_hash` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `is_active` tinyint(1) DEFAULT 0,
  PRIMARY KEY (`id`),
  UNIQUE KEY `account_id` (`account_id`),
  UNIQUE KEY `email` (`email`),
  KEY `fk_user_role` (`role_id`),
  CONSTRAINT `fk_user_role` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf32 COLLATE=utf32_general_ci;


-- cplearn_test.classes definition

CREATE TABLE `classes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `teacher_id` int(11) DEFAULT NULL,
  `starting_date` date NOT NULL,
  `ending_date` date NOT NULL,
  `descriptions` text DEFAULT NULL,
  `subject` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_teacher_class` (`teacher_id`),
  CONSTRAINT `fk_teacher_class` FOREIGN KEY (`teacher_id`) REFERENCES `users` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf32 COLLATE=utf32_general_ci;


-- cplearn_test.gallery definition

CREATE TABLE `gallery` (
  `image_id` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(11) NOT NULL,
  `image_path` varchar(255) NOT NULL,
  `description` text DEFAULT NULL,
  `upload_date` date NOT NULL,
  `image_title` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`image_id`),
  KEY `fk_gallery_student` (`student_id`),
  CONSTRAINT `fk_gallery_student` FOREIGN KEY (`student_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf32 COLLATE=utf32_general_ci;


-- cplearn_test.homeworks definition

CREATE TABLE `homeworks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `class_id` int(11) NOT NULL,
  `description` text DEFAULT NULL,
  `homework_content` text DEFAULT NULL,
  `due_date` date DEFAULT NULL,
  `file_path` varchar(255) DEFAULT NULL,
  `answer_key_path` varchar(255) DEFAULT NULL,
  `grade_level` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_class_id` (`class_id`),
  CONSTRAINT `fk_homeworks_class` FOREIGN KEY (`class_id`) REFERENCES `classes` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf32 COLLATE=utf32_general_ci;


-- cplearn_test.students definition

CREATE TABLE `students` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(11) NOT NULL,
  `grade_level` varchar(255) NOT NULL,
  `main_parent_id` int(11) NOT NULL,
  `secondary_parent_id` int(11) DEFAULT NULL,
  `addional_info` text DEFAULT NULL,
  `food_allergy` text DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `student_id` (`student_id`),
  KEY `fk_students_main_parent` (`main_parent_id`),
  KEY `fk_students_secondary_parent` (`secondary_parent_id`),
  CONSTRAINT `fk_students_main_parent` FOREIGN KEY (`main_parent_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_students_secondary_parent` FOREIGN KEY (`secondary_parent_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_students_user` FOREIGN KEY (`student_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf32 COLLATE=utf32_general_ci;


-- cplearn_test.students_homeworks definition

CREATE TABLE `students_homeworks` (
  `student_id` int(11) NOT NULL,
  `homework_id` int(11) NOT NULL,
  `grade` decimal(5,2) NOT NULL,
  `submitted_date` date NOT NULL,
  PRIMARY KEY (`student_id`,`homework_id`),
  KEY `fk_students_homeworks_homework` (`homework_id`),
  KEY `idx_student_id` (`student_id`),
  CONSTRAINT `fk_students_homeworks_homework` FOREIGN KEY (`homework_id`) REFERENCES `homeworks` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_students_homeworks_student` FOREIGN KEY (`student_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf32 COLLATE=utf32_general_ci;


-- cplearn_test.students_tests definition

CREATE TABLE `students_tests` (
  `student_id` int(11) NOT NULL,
  `test_id` int(11) NOT NULL,
  `test_date` date NOT NULL,
  `test_score` decimal(5,2) NOT NULL,
  PRIMARY KEY (`student_id`,`test_id`),
  KEY `idx_test_id` (`test_id`),
  CONSTRAINT `fk_students_tests_student` FOREIGN KEY (`student_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_students_tests_test` FOREIGN KEY (`test_id`) REFERENCES `tests` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf32 COLLATE=utf32_general_ci;


-- cplearn_test.class_schedules definition

CREATE TABLE `class_schedules` (
  `class_id` int(11) NOT NULL,
  `day_of_week` varchar(10) NOT NULL,
  `start_time` time NOT NULL,
  `end_time` time NOT NULL,
  PRIMARY KEY (`class_id`,`day_of_week`,`start_time`,`end_time`),
  CONSTRAINT `fk_class_schedules_class` FOREIGN KEY (`class_id`) REFERENCES `classes` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf32 COLLATE=utf32_general_ci;