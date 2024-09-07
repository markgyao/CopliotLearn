<?php
session_start();

// Check if the user is logged in and is an admin
if (!isset($_SESSION['loggedin']) || $_SESSION['user']['role'] != 'admin') {
    header('Location: login.php');
    exit();
}

// Include database connection
try {
    $pdo = new PDO('mysql:host=localhost;dbname=vschool', 'your_database_username', 'your_database_password');
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Error connecting to database: " . $e->getMessage());
}

// Initialize variables
$userId = $_GET['id'];
$user = null;
$successMessage = "";

// Fetch the user data
try {
    $stmt = $pdo->prepare("SELECT username, email, phone FROM users WHERE id = :id");
    $stmt->execute(['id' => $userId]);
    $user = $stmt->fetch(PDO::FETCH_ASSOC);
    if (!$user) {
        die("User not found.");
    }
} catch (PDOException $e) {
    echo "Error: " . $e->getMessage();
}

// Handle password update
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['new_password'])) {
    $newPassword = hash('sha256', $_POST['new_password']);

    try {
        $stmt = $pdo->prepare("UPDATE users SET password = :password WHERE id = :id");
        $stmt->execute(['password' => $newPassword, 'id' => $userId]);
        $successMessage = "Password updated successfully!";
    } catch (PDOException $e) {
        echo "Error: " . $e->getMessage();
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reset Password</title>
    <style>
        .form-container {
            width: 300px;
            margin: 50px auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .form-container input[type="text"],
        .form-container input[type="email"],
        .form-container input[type="password"],
        .form-container input[type="submit"] {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        .form-container input[type="submit"] {
            background-color: #4CAF50;
            color: white;
            cursor: pointer;
        }
        .form-container input[type="submit"]:hover {
            background-color: #45a049;
        }
        .back-button {
            margin-top: 20px;
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            display: block;
            text-align: center;
        }
        .back-button:hover {
            background-color: #45a049;
        }
        .success-message {
            color: green;
            font-weight: bold;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h2>Reset Password for <?php echo htmlspecialchars($user['username']); ?></h2>
        <?php if ($successMessage): ?>
            <div class="success-message">
                <?php echo $successMessage; ?>
            </div>
        <?php endif; ?>
        <form action="reset_password.php?id=<?php echo $userId; ?>" method="post">
            <label for="email">Email:</label>
            <input type="email" id="email" value="<?php echo htmlspecialchars($user['email']); ?>" disabled>

            <label for="phone">Phone:</label>
            <input type="text" id="phone" value="<?php echo htmlspecialchars($user['phone']); ?>" disabled>

            <label for="new_password">New Password:</label>
            <input type="password" id="new_password" name="new_password" required>

            <input type="submit" value="Update Password">
        </form>

        <!-- Explicitly Link Back to Manage Users -->
        <a href="manage_users.php" class="back-button">Back to Manage Users</a>
    </div>
</body>
</html>
