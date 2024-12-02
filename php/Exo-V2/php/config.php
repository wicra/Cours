<?php
// Configuration de la base de données
define('DB_HOST', 'localhost');
define('DB_NAME', 'quiz');
define('DB_USER', 'root');
define('DB_PASS', '');

// Fonction pour créer une connexion PDO
function getDbConnection() {
    try {
        $dsn = "mysql:host=" . DB_HOST . ";dbname=" . DB_NAME . ";charset=utf8mb4";
        $options = [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
            PDO::ATTR_EMULATE_PREPARES => false,
        ];
        return new PDO($dsn, DB_USER, DB_PASS, $options);
    } catch (PDOException $e) {
        error_log("Erreur de connexion : " . $e->getMessage());
        return null;
    }
}
