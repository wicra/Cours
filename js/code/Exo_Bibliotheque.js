let biblio = [];

function ajouterLivre(titre, description){
    let nouveauLivre ={      // un modèle de livre qu'on peut ajouter dans biblio
        id : Date.now(),    //Il permet d'obtenir un nombre au hazard pour qu'il soit unique
        titre : titre,      //la proprieté titre prend la valeur de titre
        description : description
    }
    biblio.push(nouveauLivre);
}

function suprimerLivre(id){
    biblio = biblio.filter(function(Livre){
        return Livre.id != id ;   
    } )
}

function afficherBiblio(){
    biblio.forEach(function(Livre) {
        console.log(Livre);
    })
}

ajouterLivre("livre1","dekjskdje");
ajouterLivre("livre2","dekjskdje");
ajouterLivre("livre3","dekjskdje");
suprimerLivre(biblio[2].id);
afficherBiblio();

