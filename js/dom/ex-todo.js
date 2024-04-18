




function ajouterTaches(contenue){
   
    let nomtache = prompt("Nom de votre tache :")
    contenue = prompt("Ajouter votre tache :" ) // pour demander a l'user de rentrer le contenue
    let el = document.createElement("li");  // Je crée une balise li 
    const id = el.setAttribute('id',nomtache) // j'ajoute une id a la taches
    el.innerText = contenue;                // je rentre en parametre le contenue texte
    el.classList.add("taches");             // j'ajoute cette element dans la class taches
    document.querySelector("body").appendChild(el); // et j'ajoute tout ca dans le body
}


function suprimerTache(id){
    id = prompt("Donne le nom du tache a suprimer : ")
    const sup = document.querySelector("li")
    sup.remove(id) 
 
}

/*
function afficherTaches(){
    taches.forEach(function(tache) {
        console.log(tache);
    })
}

ajouterTaches("tache1","description")
ajouterTaches("tache2","description")
ajouterTaches("tache3","description")
afficherTaches()
*/