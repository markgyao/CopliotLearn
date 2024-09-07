<?php
session_start();

// Check if the user is logged in and is an admin
if (!isset($_SESSION['loggedin']) || $_SESSION['loggedin'] !== true || $_SESSION['user']['role'] !== 'admin') {
    // Redirect to login or an error page if the user is not an admin
    header("Location: login.php");
    exit();
}

// Database connection
$servername = "localhost";
$username = "root";  // Adjust with your database user
$password = "passw0rd";  // Adjust with your database password
$dbname = "vschool";  // Adjust with your database name

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Handle password update
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['change_password'])) {
    $user_id = $_POST['user_id'];
    $new_password = password_hash($_POST['new_password'], PASSWORD_BCRYPT);

    $sql = "UPDATE users SET password = ? WHERE id = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("si", $new_password, $user_id);

    if ($stmt->execute()) {
        echo "<p class='success-message'>Password updated successfully!</p>";
    } else {
        echo "<p class='error-message'>Error updating password: " . $conn->error . "</p>";
    }

    $stmt->close();
}

// Handle disabling account
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['disable_account'])) {
    $user_id = $_POST['user_id'];

    $sql = "UPDATE users SET active = 0 WHERE id = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("i", $user_id);

    if ($stmt->execute()) {
        echo "<p class='success-message'>Account disabled successfully!</p>";
    } else {
        echo "<p class='error-message'>Error disabling account: " . $conn->error . "</p>";
    }

    $stmt->close();
}

// Handle grade change
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['change_grade'])) {
    $user_id = $_POST['user_id'];
    $new_grade = $_POST['new_grade'];

    $sql = "UPDATE users SET grade = ? WHERE id = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("si", $new_grade, $user_id);

    if ($stmt->execute()) {
        echo "<p class='success-message'>Grade updated successfully!</p>";
    } else {
        echo "<p class='error-message'>Error updating grade: " . $conn->error . "</p>";
    }

    $stmt->close();
}

// Handle deleting account
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['delete_account'])) {
    $user_id = $_POST['user_id'];

    $sql = "DELETE FROM users WHERE id = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("i", $user_id);

    if ($stmt->execute()) {
        echo "<p class='success-message'>Account deleted successfully!</p>";
    } else {
        echo "<p class='error-message'>Error deleting account: " . $conn->error . "</p>";
    }

    $stmt->close();
}

// Fetch all non-admin users (i.e., users with role 'teacher' or 'parent')
$sql = "SELECT id, username, email, role, grade, active FROM users WHERE role != 'admin'";
$result = $conn->query($sql);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Manage Users</title>
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
            width: 800px;
            text-align: center;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
        }
        table, th, td {
            border: 1px solid #ddd;
            padding: 10px;
        }
        th {
            background-color: #f2f2f2;
        }
        input[type="text"], input[type="submit"], select {
            padding: 10px;
            margin-top: 10px;
            margin-bottom: 10px;
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
            display: inline-block;
            padding: 10px 20px;
            background-color: #007bff;
            color: #fff;
            text-decoration: none;
            border-radius: 4px;
            margin-top: 20px;
        }
        .back-button:hover {
            background-color: #0056b3;
        }
        .inactive {
            color: red;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Manage Users</h1>
        <table>
            <tr>
                <th>Username</th>
                <th>Email</th>
                <th>Role</th>
                <th>Grade</th>
                <th>Status</th>
                <th>Actions</th>
            </tr>
            <?php
            if ($result->num_rows > 0) {
                while ($row = $result->fetch_assoc()) {
                    $status = $row['active'] ? 'Active' : '<span class="inactive">Inactive</span>';
                    echo "<tr>";
                    echo "<td>" . $row['username'] . "</td>";
                    echo "<td>" . $row['email'] . "</td>";
                    echo "<td>" . $row['role'] . "</td>";
                    echo "<td>" . $row['grade'] . "</td>";
                    echo "<td>" . $status . "</td>";
                    echo "<td>";
                    
                    // Change password form
                    echo "<form method='POST' action='manage_users.php' style='display:inline-block;'>";
                    echo "<input type='hidden' name='user_id' value='" . $row['id'] . "'>";
                    echo "<input type='text' name='new_password' placeholder='New Password' required>";
                    echo "<input type='submit' name='change_password' value='Change Password'>";
                    echo "</form>";
                    
                    // Change grade form
                    echo "<form method='POST' action='manage_users.php' style='display:inline-block;'>";
                    echo "<input type='hidden' name='user_id' value='" . $row['id'] . "'>";
                    echo "<select name='new_grade' required>";
                    echo "<option value='Grade 1'>Grade 1</option>";
                    echo "<option value='Grade 2'>Grade 2</option>";
                    echo "<option value='Grade 3'>Grade 3</option>";
                    echo "<!-- Add more grade options as needed -->";
                    echo "</select>";
                    echo "<input type='submit' name='change_grade' value='Change Grade'>";
                    echo "</form>";
                    
                    // Disable account form
                    if ($row['active']) {
                        echo "<form method='POST' action='manage_users.php' style='display:inline-block;'>";
                        echo "<input type='hidden' name='user_id' value='" . $row['id'] . "'>";
                        echo "<input type='submit' name='disable_account' value='Disable Account'>";
                        echo "</form>";
                    }

                    // Delete account form
                    echo "<form method='POST' action='manage_users.php' style='display:inline-block;'>";
                    echo "<input type='hidden' name='user_id' value='" . $row['id'] . "'>";
                    echo "<input type='submit' name='delete_account' value='Delete Account' style='background-color:red; color:white;'>";
                    echo "</form>";

                    echo "</td>";
                    echo "</tr>";
                }
            } else {
                echo "<tr><td colspan='6'>No users found</td></tr>";
            }
            ?>
        </table>

        <!-- Back button to return to the admin page -->
        <a href="admin.php" class="back-button">Back to Admin</a>
    </div>
</body>
</html>

<?php
// Close connection
$conn->close();
?>
