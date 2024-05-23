CREATE TABLE Person (
	person_id INT NOT NULL,
	name VARCHAR(255) NOT NULL,
	PRIMARY KEY (person_id)
);
CREATE TABLE Customer (
	customer_id INT NOT NULL,
	email VARCHAR(255) NOT NULL,
	PRIMARY KEY (customer_id)
);
CREATE TABLE Employee (
	employee_id INT NOT NULL,
	salary DECIMAL NOT NULL,
	PRIMARY KEY (employee_id)
);
CREATE TABLE Product (
	product_id INT NOT NULL,
	name VARCHAR(255) NOT NULL,
	price DECIMAL NOT NULL,
	PRIMARY KEY (product_id)
);
CREATE TABLE Order (
	order_id INT NOT NULL,
	date DATE NOT NULL,
	status VARCHAR(255) NOT NULL,
	PRIMARY KEY (order_id)
);
CREATE TABLE Placed (
	customer_id INT NOT NULL,
	order_id INT NOT NULL,
	payment_method VARCHAR(255) NOT NULL,
	PRIMARY KEY (customer_id, order_id),
	FOREIGN KEY (customer_id) REFERENCES Customer (customer_id) ON DELETE CASCADE,
	FOREIGN KEY (order_id) REFERENCES Order (order_id) ON DELETE CASCADE
);
CREATE TABLE Handled (
	employee_id INT NOT NULL,
	order_id INT NOT NULL,
	PRIMARY KEY (employee_id, order_id),
	FOREIGN KEY (employee_id) REFERENCES Employee (employee_id) ON DELETE CASCADE,
	FOREIGN KEY (order_id) REFERENCES Order (order_id) ON DELETE CASCADE
);
CREATE TABLE Contains (
	order_id INT NOT NULL,
	product_id INT NOT NULL,
	quantity INT NOT NULL,
	PRIMARY KEY (order_id, product_id),
	FOREIGN KEY (order_id) REFERENCES Order (order_id) ON DELETE CASCADE,
	FOREIGN KEY (product_id) REFERENCES Product (product_id) ON DELETE CASCADE
);
