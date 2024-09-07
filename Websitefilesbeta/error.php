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
    <title>Unauthorized Access</title>
</head>
<body>
    <h2>Error: Unauthorized Access</h2>
    <p>You do not have permission to view this page. Please return to the <a href="index.html">home page</a>.</p>
    <button onclick="window.location.href='index.html';">Go to Home</button>
</body>
</html>
