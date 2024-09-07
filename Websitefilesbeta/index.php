<?php
session_start();

// Check if the user is logged in; if not, redirect to the login page
if (!isset($_SESSION['loggedin'])) {
    header('Location: login.php');
    exit();
}

// Your site's home page content
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home - VSchool</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            min-height: 100vh;
        }
        .header {
            background-color: #4CAF50;
            padding: 10px;
            color: white;
            text-align: center;
        }
        .logout {
            position: absolute;
            top: 10px;
            right: 10px;
        }
        .logout a {
            color: white;
            text-decoration: none;
            font-weight: bold;
        }
        .main-content {
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
        }
        .main-content button {
            padding: 10px 20px;
            font-size: 16px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .main-content button:hover {
            background-color: #45a049;
        }
        .footer {
            background-color: #f1f1f1;
            padding: 10px;
            text-align: center;
            position: relative;
        }
        .footer p {
            margin: 5px 0;
        }
        .footer a {
            text-decoration: none;
            color: #4CAF50;
        }
    </style>
</head>
<body>

    <div class="header">
        <h1>Welcome to VSchool</h1>
        <div class="logout">
            <a href="logout.php">Logout</a>
        </div>
    </div>

    <div class="main-content">
        <p>This is your home page. You can add more content here as needed.</p>
        <button onclick="window.location.href='login.php'">Go to Login</button>
    </div>

    <div class="footer">
        <p><a href="https://maps.google.com/?q=143-30+Cherry+Ave,+Flushing,+NY+11355" target="_blank">143-30 Cherry Ave, Flushing, NY 11355</a></p>
        <p>Phone: <a href="tel:+17188866363">+1 (718) 886-6363</a></p>
    </div>

</body>
</html>
