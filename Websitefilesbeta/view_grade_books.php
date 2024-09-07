<?php
session_start();
if (!isset($_SESSION['loggedin']) || $_SESSION['loggedin'] !== true) {
    header("Location: login.php");
    exit();
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Work in Progress - My Secure Site</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            position: relative;
        }
        .logout {
            position: absolute;
            top: 20px;
            right: 20px;
        }
        .logout a {
            text-decoration: none;
            color: #FF6347;
            font-size: 1.5em;
            font-weight: bold;
        }
        .logout a:hover {
            text-decoration: underline;
        }
        .container {
            background-color: #fff;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
            text-align: center;
            width: 400px;
        }
        h2 {
            color: #333;
            font-size: 2em;
            margin-bottom: 30px;
        }
        p {
            font-size: 1.2em;
            color: #555;
        }
        .back-button {
            margin-top: 20px;
            text-align: center;
        }
        .back-button a {
            text-decoration: none;
            color: #007BFF;
            font-size: 1.2em;
            font-weight: bold;
        }
        .back-button a:hover {
            text-decoration: underline;
        }
        .footer {
            position: absolute;
            bottom: 20px;
            text-align: center;
            font-size: 1.2em;
            color: #666;
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
    <div class="logout">
        <a href="logout.php">Logout</a>
    </div>
    <div class="container">
        <h2>Work in Progress</h2>
        <p>This page is currently under construction. Please check back later.</p>
        <div class="back-button">
            <a href="admin.php">Back to Dashboard</a>
        </div>
    </div>
    <div class="footer">
        <p>
            <a href="https://maps.app.goo.gl/AoJ4gsH7BgkmHA9EA" target="_blank">143-30 Cherry Ave, Flushing, NY 11355</a>
            <br>
            Phone: <a href="tel:+17188866363">+1 718-886-6363</a>
        </p>
    </div>
</body>
</html>
