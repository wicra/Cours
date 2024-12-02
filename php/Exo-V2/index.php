<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quiz Dynamique</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <div class="container">
        <div id="source-selector">
            <label>Source des données :</label>
            <div class="toggle-switch">
                <input type="checkbox" id="data-source" class="toggle-input">
                <label for="data-source" class="toggle-label">
                    <span class="toggle-inner"></span>
                    <span class="toggle-switch"></span>
                </label>
                <span id="source-label">JSON</span>
            </div>
        </div>

        <div id="quiz-container" class="fade-in">
            <div id="timer">
                <div id="timer-circle">
                    <div id="timer-bg"></div>
                    <div id="timer-progress"></div>
                    <span id="time">30</span>
                </div>
            </div>
            <div id="question-container">
                <h2 id="question">Chargement de la question...</h2>
                <div id="choices-container"></div>
            </div>
            <div class="progress-container">
                <div class="progress-bar" style="width: 0%"></div>
            </div>
            <button id="next-btn" style="display: none;">Question suivante</button>
        </div>

        <div id="score-container" class="fade-in" style="display: none;">
            <h2>Score Final</h2>
            <p>Félicitations !</p>
            <p>Votre score : <span id="final-score">0</span>/5</p>
            <div class="progress-container">
                <div id="final-progress-bar" class="progress-bar" style="width: 0%"></div>
            </div>
            <button id="restart-btn">Recommencer le Quiz</button>
        </div>
    </div>
    <script src="js/script.js"></script>
</body>
</html>
