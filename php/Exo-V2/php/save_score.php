<?php
header('Content-Type: application/json');
require_once 'config.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $score = isset($_POST['score']) ? intval($_POST['score']) : 0;
    $source = isset($_POST['source']) ? $_POST['source'] : 'json';
    $success = false;
    $message = '';

    if ($source === 'mysql') {
        // Sauvegarde dans MySQL
        $pdo = getDbConnection();
        if ($pdo) {
            try {
                $stmt = $pdo->prepare("INSERT INTO scores (score) VALUES (?)");
                $success = $stmt->execute([$score]);
                $message = $success ? 'Score sauvegardé dans MySQL' : 'Erreur lors de la sauvegarde dans MySQL';
            } catch (PDOException $e) {
                error_log("Erreur MySQL : " . $e->getMessage());
                $message = 'Erreur lors de la sauvegarde dans MySQL';
            }
        } else {
            $message = 'Impossible de se connecter à MySQL';
        }
    }

    // Si MySQL échoue ou si on utilise JSON, on sauvegarde dans le fichier
    if (!$success || $source === 'json') {
        $date = date('Y-m-d H:i:s');
        $scoreData = "$date - Score: $score\n";
        $success = file_put_contents(__DIR__ . '/../data/scores.txt', $scoreData, FILE_APPEND) !== false;
        $message = $success ? 'Score sauvegardé dans le fichier' : 'Erreur lors de la sauvegarde dans le fichier';
    }

    echo json_encode(['success' => $success, 'message' => $message]);
} else {
    http_response_code(405);
    echo json_encode(['success' => false, 'message' => 'Méthode non autorisée']);
}
