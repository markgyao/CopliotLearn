<?php
try {
    // Establish a database connection
    $pdo = new PDO('mysql:host=localhost;dbname=vschool', 'root', 'passw0rd');
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Insert the first admin user
    $password1 = '5169007810';
    $hashedPassword1 = password_hash($password1, PASSWORD_DEFAULT);

    $stmt = $pdo->prepare("INSERT INTO users (username, email, password, phone, role) VALUES (?, ?, ?, ?, ?)");
    $stmt->execute(['lionel509', 'lionelweng@gmail.com', $hashedPassword1, '5169007810', 'admin']);

    // Insert the second admin user
    $password2 = '13159551521love';
    $hashedPassword2 = password_hash($password2, PASSWORD_DEFAULT);

    $stmt = $pdo->prepare("INSERT INTO users (username, email, password, phone, role) VALUES (?, ?, ?, ?, ?)");
    $stmt->execute(['vivien', 'happysciencecenter@gmail.com', $hashedPassword2, '13159551521', 'admin']);

    // Insert a test teacher
    $teacherPassword = 'testpassword123';
    $hashedTeacherPassword = password_hash($teacherPassword, PASSWORD_DEFAULT);

    $stmt = $pdo->prepare("INSERT INTO users (username, email, password, phone, role) VALUES (?, ?, ?, ?, ?)");
    $stmt->execute(['testteacher', 'teacher@testschool.com', $hashedTeacherPassword, '5551234567', 'teacher']);

    echo "Admin users and test teacher inserted successfully.";

} catch (PDOException $e) {
    die("Error: " . $e->getMessage());
}