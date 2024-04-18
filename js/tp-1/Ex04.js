//EXO3


let nb1 = prompt("Entrez premier nombre : ")
let nb2 = prompt("Entrez deuxieme nombre : ")

let rentre_lopperation = prompt("Choisissez entre plus , moins , fois , div")

switch(rentre_lopperation){
    case "plus":
        alert(nb1+nb2)
    case "moins":
        alert(nb1-nb2)
    case "fois":
        alert(nb1*nb2)
    
    case "div":
        alert(nb1/nb2)

    default:
        alert("ca existe pas")
}

