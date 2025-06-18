<?php
$username = $_GET['username'];
// Sanitize the input to prevent XSS attacks
$sanitized_username = htmlspecialchars($username, ENT_QUOTES, 'UTF-8');
echo '<div class="header"> Welcome, ' . $sanitized_username . '</div>';
?>
