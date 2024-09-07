<?php
session_start();

// Include database connection
try {
    $pdo = new PDO('mysql:host=localhost;dbname=vschool', 'your_database_username', 'your_database_password');
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Error connecting to database: " . $e->getMessage());
}

$errorMessage = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $usernameOrEmail = trim($_POST['username_or_email']);
    $password = $_POST['password'];

    try {
        // Query the database for the user with the provided username or email
        $stmt = $pdo->prepare("SELECT id, username, email, password, role FROM users WHERE username = :usernameOrEmail OR email = :usernameOrEmail");
        $stmt->execute(['usernameOrEmail' => $usernameOrEmail]);
        $user = $stmt->fetch(PDO::FETCH_ASSOC);

        // Verify the password using password_verify
        if ($user && password_verify($password, $user['password'])) {
            // Start session and store user details
            $_SESSION['loggedin'] = true;
            $_SESSION['user'] = [
                'id' => $user['id'],
                'username' => $user['username'],
                'email' => $user['email'],
                'role' => $user['role']
            ];

            // Redirect based on role
            switch ($user['role']) {
                case 'admin':
                    header('Location: admin.php');
                    break;
                case 'teacher':
                    header('Location: teacher.php');
                    break;
                default:
                    header('Location: parent.php');
                    break;
            }
            exit();
        } else {
            $errorMessage = "Invalid username/email or password.";
        }
    } catch (PDOException $e) {
        die("Error: " . $e->getMessage());
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - My Secure Site</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }
        .container {
            background-color: #fff;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
            text-align: center;
            width: 400px;
            max-width: 100%;
        }
        h2 {
            color: #333;
            font-size: 2em;
            margin-bottom: 20px;
        }
        .alert {
            color: white;
            background-color: red;
            padding: 10px;
            margin-bottom: 20px;
            border-radius: 5px;
            display: none;
        }
        input[type="text"],
        input[type="password"] {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        input[type="submit"] {
            width: 100%;
            padding: 10px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #45a049;
        }
        .show-password {
            margin: 10px 0;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .show-password input {
            margin-left: 10px;
        }
        .footer {
            text-align: center;
            font-size: 1em;
            color: #666;
            margin-top: 20px;
        }
        .footer a {
            color: #007BFF;
            text-decoration: none;
        }
        .footer a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Login</h2>
        <?php if (!empty($errorMessage)): ?>
            <div class="alert" style="display: block;">
                <?php echo htmlspecialchars($errorMessage); ?>
            </div>
        <?php endif; ?>
        <form action="login.php" method="post">
            <label for="username_or_email">Username or Email:</label>
            <input type="text" id="username_or_email" name="username_or_email" required>

            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>

            <div class="show-password">
                <input type="checkbox" onclick="togglePassword()"> Show Password
            </div>

            <input type="submit" value="Login">
        </form>
    </div>
    <div class="footer">
        <p>
            <a href="https://maps.app.goo.gl/AoJ4gsH7BgkmHA9EA" target="_blank">143-30 Cherry Ave, Flushing, NY 11355</a>
            <br>
            Phone: <a href="tel:+17188866363">+1 718-886-6363</a>
        </p>
    </div>

    <script>
        function togglePassword() {
            var passwordField = document.getElementById("password");
            if (passwordField.type === "password") {
                passwordField.type = "text";
            } else {
                passwordField.type = "password";
            }
        }
    </script>
</body>
</html>
