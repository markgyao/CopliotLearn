<?php
session_start();

// Check if the user is logged in and is an admin
if (!isset($_SESSION['loggedin']) || $_SESSION['loggedin'] !== true || $_SESSION['user']['role'] !== 'admin') {
    // Redirect to login or an error page if the user is not an admin
    header("Location: login.php"); // Change this to your login page or error page
    exit();
}

// Database connection setup
$servername = "localhost";
$username = "root";  // Replace with your database username
$password = "passw0rd";  // Replace with your database password
$dbname = "vschool";  // Replace with your database name

// Create connection to MariaDB
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Check if the form was submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get data from the form
    $name = $_POST['name'];
    $email = $_POST['email'];
    $phone = $_POST['phone'];
    $password = password_hash($_POST['password'], PASSWORD_BCRYPT);
    $grades = json_encode($_POST['grades']);  // Storing the selected grades as JSON

    // Insert data into the database
    $sql = "INSERT INTO teachers (name, email, phone, password_hash, grades_teach)
            VALUES (?, ?, ?, ?, ?)";

    $stmt = $conn->prepare($sql);
    $stmt->bind_param("sssss", $name, $email, $phone, $password, $grades);

    if ($stmt->execute()) {
        echo "<p class='success-message'>Teacher account created successfully!</p>";
    } else {
        echo "<p class='error-message'>Error: " . $stmt->error . "</p>";
    }

    $stmt->close();
}

// Close the connection
$conn->close();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create Teacher User</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            background-color: #fff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            width: 400px;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        label {
            display: block;
            margin-bottom: 8px;
            color: #333;
        }
        input[type="text"],
        input[type="email"],
        input[type="password"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        .checkbox-group {
            margin-bottom: 20px;
        }
        .checkbox-group label {
            margin-right: 10px;
        }
        input[type="submit"] {
            width: 100%;
            padding: 10px;
            background-color: #28a745;
            border: none;
            color: #fff;
            font-size: 16px;
            cursor: pointer;
            border-radius: 4px;
        }
        input[type="submit"]:hover {
            background-color: #218838;
        }
        .success-message {
            color: green;
            text-align: center;
        }
        .error-message {
            color: red;
            text-align: center;
        }
        .back-button {
            display: block;
            width: 100%;
            padding: 10px;
            background-color: #007bff;
            color: white;
            text-align: center;
            border-radius: 4px;
            text-decoration: none;
            margin-top: 20px;
        }
        .back-button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Create Teacher Account</h1>
        <form action="create_users.php" method="post">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="phone">Phone Number:</label>
            <input type="text" id="phone" name="phone" required>

            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>

            <label for="grades">Grades You Teach:</label>
            <div class="checkbox-group">
                <label><input type="checkbox" name="grades[]" value="Grade 1"> Grade 1</label>
                <label><input type="checkbox" name="grades[]" value="Grade 2"> Grade 2</label>
                <label><input type="checkbox" name="grades[]" value="Grade 3"> Grade 3</label>
                <label><input type="checkbox" name="grades[]" value="Grade 4"> Grade 4</label>
                <label><input type="checkbox" name="grades[]" value="Grade 5"> Grade 5</label>
                <label><input type="checkbox" name="grades[]" value="Grade 6"> Grade 6</label>
                <label><input type="checkbox" name="grades[]" value="Grade 7"> Grade 7</label>
                <label><input type="checkbox" name="grades[]" value="Grade 8"> Grade 8</label>
                <label><input type="checkbox" name="grades[]" value="Grade 9"> Grade 9</label>
                <label><input type="checkbox" name="grades[]" value="Grade 10"> Grade 10</label>
                <label><input type="checkbox" name="grades[]" value="Grade 11"> Grade 11</label>
                <label><input type="checkbox" name="grades[]" value="Grade 12"> Grade 12</label>
                <label><input type="checkbox" name="grades[]" value="SHSAT"> SHSAT</label>
                <label><input type="checkbox" name="grades[]" value="ACT"> ACT</label>
                <label><input type="checkbox" name="grades[]" value="SAT"> SAT</label>
                <label><input type="checkbox" name="grades[]" value="REGENTS"> REGENTS</label>
            </div>

            <input type="submit" value="Create Teacher">
        </form>

        <!-- Back button to return to the admin page -->
        <a href="admin.php" class="back-button">Back to Admin</a>
    </div>
</body>
</html>
