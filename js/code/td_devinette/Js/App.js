
// Générer un nombre aléatoire entre 1 et 100
let randomNumber = Math.floor(Math.random() * 100) + 1;

// Éléments DOM pour afficher les informations
let guesses = document.querySelector(".guesses");
let lastResult = document.querySelector(".lastResult");
let lowOrHi = document.querySelector(".lowOrHi");

// Éléments DOM pour la saisie et la soumission de l'utilisateur
let guessSubmit = document.querySelector(".guessSubmit");
let guessField = document.querySelector(".guessField");

// Initialiser le compteur de suppositions et le bouton de réinitialisation
let guessCount = 1;
let resetButton;

// Fonction pour vérifier la supposition de l'utilisateur
function checkGuess() {
  // Récupérer la supposition de l'utilisateur depuis le champ de saisie
  let userGuess = Number(guessField.value);

  // Vérifier si c'est la première supposition
  if (guessCount === 1) {
    guesses.textContent = "Propositions précédentes : ";
  }

  // Ajouter la supposition à la liste des suppositions
  guesses.textContent += userGuess + " ";

  // Vérifier si la supposition est correcte
  if (userGuess === randomNumber) {
    // Afficher un message de victoire
    lastResult.textContent = "Bravo, vous avez trouvé le nombre !";
    lastResult.style.backgroundColor = "green";
    lowOrHi.textContent = "";

    // Terminer le jeu
    setGameOver();
  } else if (guessCount === 10) {
    // Si le joueur a épuisé toutes ses tentatives, afficher un message de défaite
    lastResult.textContent = "!!! PERDU !!!";

    // Terminer le jeu
    setGameOver();
  } else {
    // Si la supposition est incorrecte, indiquer si elle est trop basse ou trop élevée
    lastResult.textContent = "Faux !";
    lastResult.style.backgroundColor = "red";
    if (userGuess < randomNumber) {
      lowOrHi.textContent = "Le nombre saisi est trop petit !";
    } else if (userGuess > randomNumber) {
      lowOrHi.textContent = "Le nombre saisi est trop grand !";
    }
  }

  // Incrémenter le compteur de suppositions
  guessCount++;

  // Effacer le champ de saisie et lui redonner le focus
  guessField.value = "";
  guessField.focus();
}

// Ajouter un écouteur d'événement au bouton de soumission
guessSubmit.addEventListener("click", checkGuess);

// Fonction pour terminer le jeu
function setGameOver() {
  // Désactiver le champ de saisie et le bouton de soumission
  guessField.disabled = true;
  guessSubmit.disabled = true;

  // Créer un bouton de réinitialisation
  resetButton = document.createElement("button");
  resetButton.textContent = "Commencer une nouvelle partie";
  document.body.appendChild(resetButton);

  // Ajouter un écouteur d'événement au bouton de réinitialisation
  resetButton.addEventListener("click", resetGame);
}

// Fonction pour réinitialiser le jeu
function resetGame() {
  // Remettre le compteur de suppositions à 1
  guessCount = 1;

  // Effacer tous les paragraphes d'information
  let resetParas = document.querySelectorAll(".resultParas p");
  for (let i = 0; i < resetParas.length; i++) {
    resetParas[i].textContent = "";
  }

  // Supprimer le bouton de réinitialisation
  resetButton.parentNode.removeChild(resetButton);

  // Activer les éléments de formulaire, vider et mettre au point le champ de texte
  guessField.disabled = false;
  guessSubmit.disabled = false;
  guessField.value = "";
  guessField.focus();

  // Réinitialiser la couleur de fond du paragraphe lastResult
  lastResult.style.backgroundColor = "white";

  // Générer un nouveau nombre aléatoire
  randomNumber = Math.floor(Math.random() * 100) + 1;
}
