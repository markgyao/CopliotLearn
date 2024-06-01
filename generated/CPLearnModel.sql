CREATE TABLE students (
	student_id INT NOT NULL,
	last_name CHAR(50) NOT NULL,
	first_name CHAR(50) NOT NULL,
	phone CHAR(20) NOT NULL,
	email CHAR(50) NOT NULL,
	PRIMARY KEY (student_id)
);
CREATE TABLE tests (
	test_id INT NOT NULL,
	test_name CHAR(50) NOT NULL,
	test_category_id INT NOT NULL,
	test_file_path CHAR(255) NOT NULL,
	PRIMARY KEY (test_id)
);

CREATE TABLE test_deails {
	test_id INT NOT NULL
	question_id INT NOT NULL
	quesiton_type CHAR(10) --Multiple_choice or ...
	question_answer_choice
	quesiton_ansser_details
	PRIMARY KEY (test_id, question_id)
}
CREATE TABLE student_test_history (
	test_Id INT NOT NULL,
	test_date DATE NOT NULL,
	test_score DOUBLE PRECISION NOT NULL,	-- type mapped from: DOUBLE
	PRIMARY KEY (test_id, test_date)
);

/*
CREATE TABLE Rel (
	id INT NOT NULL,
	id2 INT NOT NULL,	-- renamed from: id
	PRIMARY KEY (id, id2),
	FOREIGN KEY (id) REFERENCES Students (id) ON DELETE CASCADE,
	FOREIGN KEY (id2) REFERENCES StudentTestHistory (id) ON DELETE CASCADE
);
*/