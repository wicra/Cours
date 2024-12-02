let currentQuestion = null;
let score = 0;
let timer = null;
let timeLeft = 30;
let totalQuestions = 5;
let currentQuestionNumber = 0;
let dataSource = 'json'; // Par défaut, on utilise JSON

// Éléments du DOM
const questionElement = document.getElementById('question');
const choicesContainer = document.getElementById('choices-container');
const nextButton = document.getElementById('next-btn');
const timerElement = document.getElementById('time');
const timerProgress = document.getElementById('timer-progress');
const scoreContainer = document.getElementById('score-container');
const quizContainer = document.getElementById('quiz-container');
const finalScoreElement = document.getElementById('final-score');
const restartButton = document.getElementById('restart-btn');
const progressBar = document.querySelector('.progress-bar');
const finalProgressBar = document.getElementById('final-progress-bar');
const dataSourceToggle = document.getElementById('data-source');
const sourceLabel = document.getElementById('source-label');

// Gestionnaire du changement de source de données
dataSourceToggle.addEventListener('change', function() {
    dataSource = this.checked ? 'mysql' : 'json';
    sourceLabel.textContent = this.checked ? 'MySQL' : 'JSON';
    restartQuiz(); // Redémarrer le quiz avec la nouvelle source
});

// Fonction pour mettre à jour la barre de progression
function updateProgress() {
    const progress = (currentQuestionNumber / totalQuestions) * 100;
    progressBar.style.width = `${progress}%`;
}

// Fonction pour démarrer le timer
function startTimer() {
    timeLeft = 30;
    timerElement.textContent = timeLeft;
    updateTimerProgress();
    
    if (timer) clearInterval(timer);
    
    timer = setInterval(() => {
        timeLeft--;
        timerElement.textContent = timeLeft;
        updateTimerProgress();
        
        if (timeLeft <= 0) {
            clearInterval(timer);
            handleTimeout();
        }
        
        // Change la couleur en fonction du temps restant
        if (timeLeft <= 5) {
            timerProgress.style.background = `conic-gradient(#f44336 ${(timeLeft/30)*360}deg, transparent 0deg)`;
        } else if (timeLeft <= 10) {
            timerProgress.style.background = `conic-gradient(#ff9800 ${(timeLeft/30)*360}deg, transparent 0deg)`;
        } else {
            timerProgress.style.background = `conic-gradient(#4CAF50 ${(timeLeft/30)*360}deg, transparent 0deg)`;
        }
    }, 1000);
}

// Fonction pour mettre à jour le cercle de progression du timer
function updateTimerProgress() {
    const progress = (timeLeft / 30) * 360;
    timerProgress.style.background = `conic-gradient(#4CAF50 ${progress}deg, transparent 0deg)`;
}

// Fonction pour gérer le timeout
function handleTimeout() {
    clearInterval(timer);
    disableAllChoices();
    showNextButton();
    
    // Afficher la bonne réponse
    const choices = document.querySelectorAll('.choice-btn');
    const correctChoice = choices[currentQuestion.correct];
    correctChoice.classList.add('correct');
}

// Fonction pour désactiver tous les choix
function disableAllChoices() {
    const choices = document.querySelectorAll('.choice-btn');
    choices.forEach(choice => {
        choice.disabled = true;
    });
}

// Fonction pour afficher le bouton suivant
function showNextButton() {
    nextButton.style.display = 'block';
}

// Fonction pour charger une nouvelle question
async function loadQuestion() {
    try {
        const response = await fetch(`php/get_question.php?source=${dataSource}`);
        const data = await response.json();
        currentQuestion = data;
        currentQuestionNumber++;
        
        questionElement.textContent = data.question;
        choicesContainer.innerHTML = '';
        
        data.choices.forEach((choice, index) => {
            const button = document.createElement('button');
            button.className = 'choice-btn fade-in';
            button.textContent = choice;
            button.onclick = () => handleChoice(index);
            button.style.animationDelay = `${index * 0.1}s`;
            choicesContainer.appendChild(button);
        });
        
        nextButton.style.display = 'none';
        updateProgress();
        startTimer();
    } catch (error) {
        console.error('Erreur lors du chargement de la question:', error);
        questionElement.textContent = 'Erreur lors du chargement de la question';
    }
}

// Fonction pour gérer le choix d'une réponse
function handleChoice(choiceIndex) {
    clearInterval(timer);
    disableAllChoices();
    
    const choices = document.querySelectorAll('.choice-btn');
    const correctChoice = choices[currentQuestion.correct];
    const selectedChoice = choices[choiceIndex];
    
    correctChoice.classList.add('correct');
    
    if (choiceIndex === currentQuestion.correct) {
        score++;
    } else {
        selectedChoice.classList.add('incorrect');
    }
    
    showNextButton();
}

// Fonction pour sauvegarder le score
async function saveScore() {
    const formData = new FormData();
    formData.append('score', score);
    formData.append('source', dataSource);
    
    try {
        const response = await fetch('php/save_score.php', {
            method: 'POST',
            body: formData
        });
        const data = await response.json();
        console.log(data.message);
    } catch (error) {
        console.error('Erreur lors de la sauvegarde du score:', error);
    }
}

// Fonction pour afficher le score final
function showFinalScore() {
    quizContainer.style.display = 'none';
    scoreContainer.style.display = 'block';
    finalScoreElement.textContent = score;
    
    // Mise à jour de la barre de progression finale
    const finalProgress = (score / totalQuestions) * 100;
    finalProgressBar.style.width = `${finalProgress}%`;
    
    saveScore();
}

// Fonction pour redémarrer le quiz
function restartQuiz() {
    score = 0;
    currentQuestionNumber = 0;
    quizContainer.style.display = 'block';
    scoreContainer.style.display = 'none';
    progressBar.style.width = '0%';
    loadQuestion();
}

// Événements
nextButton.onclick = () => {
    if (currentQuestionNumber >= totalQuestions) {
        showFinalScore();
    } else {
        loadQuestion();
    }
};

restartButton.onclick = restartQuiz;

// Démarrage du quiz
loadQuestion();
