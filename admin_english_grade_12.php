<?php
session_start();
if (!isset($_SESSION['loggedin']) || $_SESSION['loggedin'] !== true || $_SESSION['user']['role'] !== 'admin') {
    header("Location: login.php");
    exit();
}

// Editable Variables
$grade = '12'; // Set the grade here
$subject = 'English'; // Set the subject here
$directory = '/opt/cplearn/data/prek_to_12/high_school/grade_' . $grade . '/' . $subject; // Path to the directory
$webDirectory = '/data/prek_to_12/high_school/grade_' . $grade . '/' . $subject; // Web accessible path
$backPage = 'admin_grade_' . $grade . '.php'; // Back button page link

$message = "";

// Handle renaming of files
if (isset($_POST['rename']) && isset($_POST['new_name']) && isset($_POST['old_name'])) {
    $oldName = $directory . '/' . $_POST['old_name'];
    $newName = $directory . '/' . $_POST['new_name'];
    
    if (file_exists($oldName) && !empty($_POST['new_name'])) {
        rename($oldName, $newName);
        $message = "<p style='color: green; text-align: center;'>File renamed successfully.</p>";
    } else {
        $message = "<p style='color: red; text-align: center;'>Failed to rename file.</p>";
    }
}

// Fetch list of files
$files = array_diff(scandir($directory), array('.', '..'));
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Grade <?php echo $grade; ?> - <?php echo $subject; ?> Directory Listing</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
            display: flex;
            flex-direction: row;
            justify-content: flex-start;
            align-items: flex-start;
            min-height: 100vh;
            overflow-x: hidden;
        }
        .file-list-container {
            background-color: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
            width: 20%;
            box-sizing: border-box;
            transition: all 0.5s ease;
            z-index: 1;
            position: relative;
            overflow-y: auto;
            max-height: 90vh;
        }
        .preview-container {
            background-color: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
            width: 75%;
            box-sizing: border-box;
            margin-left: 20px;
            opacity: 0;
            transform: translateX(100%);
            transition: all 0.5s ease;
        }
        .preview-container.visible {
            opacity: 1;
            transform: translateX(0);
        }
        h2 {
            color: #333;
            text-align: center;
            margin-bottom: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            word-wrap: break-word;
        }
        table, th, td {
            border: 1px solid #ddd;
        }
        th, td {
            padding: 10px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
        .actions button, .actions form input[type="submit"], .back-button a {
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 6px 10px;
            font-size: 0.9em;
            cursor: pointer;
            margin-right: 8px;
            margin-bottom: 5px;
            transition: background-color 0.3s;
        }
        .actions button:hover, .actions form input[type="submit"]:hover, .back-button a:hover {
            background-color: #0056b3;
        }
        .actions input[type="text"] {
            padding: 5px;
            font-size: 1em;
            border: 1px solid #ddd;
            border-radius: 5px;
            margin-bottom: 5px;
        }
        object {
            width: 100%;
            height: 90vh;
            border: 1px solid #ddd;
        }
        .back-button {
            margin-top: 20px;
            padding: 10px 20px;
            font-size: 1em;
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            text-decoration: none;
            display: inline-block;
            transition: background-color 0.3s;
        }
        .back-button:hover {
            background-color: #0056b3;
        }

        /* Disclaimer styling */
        .disclaimer {
            color: red;
            text-align: center;
            font-size: 0.9em;
            margin-top: 20px;
        }

        /* Media query for phone screens */
        @media (max-width: 768px) {
            body {
                flex-direction: column;
                align-items: stretch;
                padding: 10px;
            }
            .file-list-container, .preview-container {
                width: 100%;
                margin: 0;
                box-shadow: none;
                border-radius: 0;
            }
            .preview-container {
                transform: translateX(0);
                opacity: 1;
            }
            table th, table td {
                font-size: 0.9em;
            }
            .actions button, .actions form input[type="submit"], .back-button a {
                font-size: 0.8em;
                padding: 5px;
            }
        }
    </style>
</head>
<body>
    <div class="file-list-container" id="fileListContainer">
        <?php echo $message; ?>
        <h2>Grade <?php echo $grade; ?> - <?php echo $subject; ?></h2>
        <table>
            <tr>
                <th>File Name</th>
                <th>Actions</th>
            </tr>
            <?php foreach ($files as $file): ?>
                <tr>
                    <td><?php echo htmlspecialchars($file); ?></td>
                    <td class="actions">
                        <button onclick="previewFile('<?php echo $webDirectory . '/' . $file; ?>')">Preview</button>
                        <button onclick="printFile('<?php echo $webDirectory . '/' . $file; ?>')">Print</button>
                        <form style="display:inline;" method="POST" action="">
                            <input type="hidden" name="old_name" value="<?php echo htmlspecialchars($file); ?>">
                            <input type="text" name="new_name" placeholder="New name">
                            <input type="submit" name="rename" value="Rename">
                        </form>
                    </td>
                </tr>
            <?php endforeach; ?>
        </table>

        <!-- Disclaimer for phone users -->
        <p class="disclaimer">
            Disclaimer: On phones, the preview may only show the first page. To see the entire document, please click "Print".
        </p>

        <div class="back-button">
            <a href="<?php echo $backPage; ?>" style="color:white;">Back to Grade <?php echo $grade; ?> Directory</a>
        </div>
    </div>
    
    <div class="preview-container" id="previewContainer">
        <object id="filePreview" data="" type="application/pdf">
            <p>Your browser does not support PDFs. Please download the PDF to view it: <a id="pdfDownloadLink" href="">Download PDF</a>.</p>
        </object>
    </div>

    <script>
        function previewFile(filePath) {
   
