<?php
session_start();
if (!isset($_SESSION['loggedin']) || $_SESSION['loggedin'] !== true) {
    header("Location: login.php");
    exit();
}
?>

<?php
// Redirect to the admin_view.php file located in the data directory within the web-accessible directory
header("Location: /data/admin_view.php");
exit();
