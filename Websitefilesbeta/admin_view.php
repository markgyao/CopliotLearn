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
    <title>Directory Listing - Smart Club</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            min-height: 100vh;
        }
        .container {
            background-color: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
            width: 80%;
            max-width: 900px;
            margin-bottom: 20px;
        }
        h2 {
            color: #333;
            text-align: center;
            margin-bottom: 20px;
        }
        ul {
            list-style-type: none;
            padding: 0;
            margin: 0;
        }
        ul li {
            padding: 10px;
            margin-bottom: 5px;
            border-bottom: 1px solid #ddd;
            display: flex;
            justify-content: space-between;
        }
        ul li a {
            text-decoration: none;
            color: #007BFF;
            font-weight: bold;
            flex-grow: 1;
            text-transform: uppercase;
        }
        ul li a:hover {
            text-decoration: underline;
        }
        .back-button {
            padding: 10px 20px;
            font-size: 1em;
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            text-decoration: none;
            display: inline-block;
        }
        .back-button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Directory Listing</h2>
        <ul>
            <?php
            $directory = '/opt/cplearn/data'; // Replace with your directory path

            function listSubdirectories($dir) {
                $exclude = 'admin_important_papers'; // Directory to exclude
                $files = scandir($dir);
                foreach ($files as $file) {
                    if ($file !== '.' && $file !== '..' && $file !== $exclude) {
                        $filePath = $dir . '/' . $file;
                        if (is_dir($filePath)) {
                            // Convert directory name to uppercase and replace underscores with spaces
                            $displayName = strtoupper(str_replace('_', ' ', $file));
                            $subdirectoryName = strtolower(str_replace(' ', '_', $file)); // Convert name to lowercase and replace spaces with underscores

                            // Check if the directory is "act" and link to admin_view_act.php
                            if ($subdirectoryName === 'act') {
                                echo '<li><a href="admin_view_act.php">' . $displayName . '</a></li>';
                            } 
                            // Check if the directory is "prek_to_12" and link to admin_view_prek_to_12.php
                            else if ($subdirectoryName === 'prek_to_12') {
                                echo '<li><a href="admin_view_prek_to_12.php">' . $displayName . '</a></li>';
                            }
                            else {
                                echo '<li><a href="admin_' . $subdirectoryName . '.php">' . $displayName . '</a></li>';
                            }
                        }
                    }
                }
            }

            listSubdirectories($directory);
            ?>
        </ul>
    </div>
    <a href="http://vschool.ddns.net/admin.php" class="back-button">Back to Dashboard</a>
</body>
</html>
