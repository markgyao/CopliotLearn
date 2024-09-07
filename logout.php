<?php
session_start();
session_unset();
session_destroy();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Logout</title>
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
            text-align: center;
        }
        .container {
            background-color: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .message {
            font-size: 1.5em;
            margin-bottom: 20px;
        }
        .timer {
            font-size: 1.2em;
            color: #555;
            margin-bottom: 20px;
        }
        .redirect-btn {
            background-color: #007BFF;
            color: white;
            padding: 10px 20px;
            font-size: 1em;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .redirect-btn:hover {
            background-color: #0056b3;
        }
    </style>
    <script>
        function startRedirectTimer() {
            var timer = 10;
            var countdownElement = document.getElementById('countdown');
            setInterval(function() {
                if (timer > 0) {
                    countdownElement.textContent = timer;
                    timer--;
                } else {
                    window.location.href = "login.php";
                }
            }, 1000);
        }
        function redirectToLogin() {
            window.location.href = "login.php";
        }
    </script>
</head>
<body onload="startRedirectTimer()">
    <div class="container">
        <p class="message">You have been logged out successfully.</p>
        <p class="timer">You will be redirected to the login page in <span id="countdown">10</span> seconds.</p>
        <button class="redirect-btn" onclick="redirectToLogin()">Instantly Login</button>
    </div>
</body>
</html>
