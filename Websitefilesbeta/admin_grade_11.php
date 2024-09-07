<?php
session_start();
if (!isset($_SESSION['loggedin']) || $_SESSION['loggedin'] !== true || $_SESSION['user']['role'] !== 'admin') {
    header("Location: login.php");
    exit();
}

// Editable Variables
$grade = '11'; // Set the grade here (e.g., 1, 2, 3, etc.)
$pageTitle = 'Pre-K to 12 Directory Listing - Smart Club'; // Page title
$backPageLink = "http://vschool.ddns.net/admin_view.php"; // Back button link

// Directories to list (Subject => Link)
$directories = [
    'English' => 'admin_english_grade_' . $grade . '.php',
    'Math' => 'admin_math_grade_' . $grade . '.php',
    // Add more subjects if needed
];
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo $pageTitle; ?></title>
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
        <h2>Grade <?php echo $grade; ?> Directory Listing</h2>
        <ul>
            <?php
            foreach ($directories as $subject => $link) {
                echo '<li><a href="' . $link . '">' . strtoupper($subject) . '</a></li>';
            }
            ?>
        </ul>
    </div>
    <a href="<?php echo $backPageLink; ?>" class="back-button">Back to Directory Listing</a>
</body>
</html>
