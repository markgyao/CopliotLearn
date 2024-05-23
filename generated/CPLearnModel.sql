CREATE TABLE Students (
	id INT NOT NULL,
	last_name CHAR(50) NOT NULL,
	first_name CHAR(50) NOT NULL,
	phone CHAR(20) NOT NULL,
	email CHAR(50) NOT NULL,
	PRIMARY KEY (id)
);
CREATE TABLE Tests (
	id INT NOT NULL,
	test_name_id CHAR(50) NOT NULL,
	test_category_id INT NOT NULL,
	test_level INT NOT NULL,
	test_file CHAR(255) NOT NULL,
	PRIMARY KEY (id)
);
CREATE TABLE StudentTestHistory (
	id INT NOT NULL,
	testId INT NOT NULL,
	testDate DATE NOT NULL,
	score DOUBLE PRECISION NOT NULL,	-- type mapped from: DOUBLE
	PRIMARY KEY (id)
);
CREATE TABLE Rel (
	id INT NOT NULL,
	id2 INT NOT NULL,	-- renamed from: id
	PRIMARY KEY (id, id2),
	FOREIGN KEY (id) REFERENCES Students (id) ON DELETE CASCADE,
	FOREIGN KEY (id2) REFERENCES StudentTestHistory (id) ON DELETE CASCADE
);
