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
    <title>Admin Dashboard - Smart Club</title>
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
            transition: background-color 0.3s, color 0.3s;
        }
        .dark-mode {
            background-color: #333;
            color: #f4f4f4;
        }
        .container {
            background-color: #fff;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
            text-align: center;
            width: 400px;
            transition: background-color 0.3s, color 0.3s;
        }
        .dark-mode .container {
            background-color: #444;
            color: #f4f4f4;
        }
        h2 {
            color: #333;
            font-size: 2em;
            margin-bottom: 30px;
            transition: color 0.3s;
        }
        .dark-mode h2 {
            color: #f4f4f4;
        }
        ul {
            list-style-type: none;
            padding: 0;
            margin: 0;
        }
        ul li {
            margin: 20px 0;
        }
        ul li a {
            text-decoration: none;
            color: #007BFF;
            font-size: 1.5em;
            font-weight: bold;
            transition: color 0.3s;
        }
        .dark-mode ul li a {
            color: #1E90FF;
        }
        ul li a:hover {
            text-decoration: underline;
        }
        .logout, .dark-mode-toggle {
            position: absolute;
            top: 20px;
            right: 20px;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .logout a, .dark-mode-toggle button {
            text-decoration: none;
            color: #FF6347;
            font-size: 1.5em;
            font-weight: bold;
            background: none;
            border: none;
            cursor: pointer;
            transition: color 0.3s;
        }
        .dark-mode .logout a, .dark-mode .dark-mode-toggle button {
            color: #FF7F50;
        }
        .logout a:hover, .dark-mode-toggle button:hover {
            text-decoration: underline;
        }
        .footer {
            position: absolute;
            bottom: 20px;
            text-align: center;
            font-size: 1.2em;
            color: #666;
            transition: color 0.3s;
        }
        .dark-mode .footer {
            color: #999;
        }
        .footer a {
            color: #007BFF;
            text-decoration: none;
            transition: color 0.3s;
        }
        .dark-mode .footer a {
            color: #1E90FF;
        }
        .footer a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="logout">
        <div class="dark-mode-toggle">
            <button onclick="toggleDarkMode()">?</button>
        </div>
        <a href="logout.php">Logout</a>
    </div>
    <div class="container">
        <h2>Admin Dashboard</h2>
        <ul>
            <li><a href="create_user.php">Create User</a></li>
            <li><a href="manage_users.php">Manage Users</a></li>
            <li><a href="admin_view.php">View All Admin Files</a></li>
            <li><a href="view_grade_books.php">View Grade Books</a></li>
            <li><a href="view_student_contacts.php">View Student Contacts</a></li>
            <li><a href="admin_important_papers.php">Important Papers</a></li>
            <li><a href="items.php">Items</a></li>
            <li><a href="printer_status.php">Printer Status</a></li>
        </ul>
        <p>Total Files in /opt/cplearn: 
            <?php
                function countFiles($dir) {
                    $fileCount = 0;
                    $files = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($dir));
                    foreach ($files as $file) {
                        if ($file->isFile()) {
                            $fileCount++;
                        }
                    }
                    return $fileCount;
                }

                $directory = '/opt/cplearn';
                $totalFiles = countFiles($directory);
                echo $totalFiles;
            ?>
        </p>
    </div>
    <div class="footer">
        <p>
            <a href="https://maps.app.goo.gl/AoJ4gsH7BgkmHA9EA" target="_blank">143-30 Cherry Ave, Flushing, NY 11355</a>
            <br>
            Phone: <a href="tel:+17188866363">+1 718-886-6363</a>
        </p>
    </div>

    <script>
        function toggleDarkMode() {
            document.body.classList.toggle('dark-mode');
        }
    </script>
</body>
</html>
