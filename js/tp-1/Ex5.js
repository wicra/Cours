

let demande_si_etd = prompt("Est-vous étudiant : ")
let Jour = prompt("Entrez votre Jour : ")
let prix_lundi = 10
let prix_Mardi = 8
let prix_Mercredi = 9
let prix_jeudi = 7
let prix_vendredi = 12
let prix_samedi = 15
let prix_dimanche = 15
let reduction = 0.8

if(demande_si_etd == "oui"){
    
    switch(Jour){
        case '1':
            console.log("Lundi : - Menu Pizza ")
            console.log(prix_lundi*reduction)
            break

        case '2':
            console.log("Mardi :  - Menu Pasta")
            console.log(prix_Mardi*reduction)
            break
        case '3':
            console.log("Mercredi :  - Menu Burgur")
            console.log(prix_Mercredi*reduction)
            break
        case '4':
            console.log("Jeudi : - Menu Salade")
            console.log(prix_jeudi*reduction)
            break
        case '5':
            console.log("Vendredi : - Menu Poisson")
            console.log(prix_vendredi*reduction)
            break
        case '6':
            console.log("Samedi : - Menu Special")
            console.log(prix_samedi*reduction)
            break
        case '7':
            console.log("Dimanche : - Menu Special")
            console.log(prix_dimanche*reduction)
            break

        default:
            console.log("Tu en vie pas sur terre")
            break
    }

}
else{
 
    switch(Jour){
        case '1':
            console.log("Lundi : - Menu Pizza ")
            aleconsole.log(prix_lundi)
            break

        case '2':
            console.log("Mardi :  - Menu Pasta")
            console.log(prix_Mardi)
            break
        case '3':
            console.log("Mercredi :  - Menu Burgur")
            console.log(prix_Mercredi)
            break
        case '4':
            console.log("Jeudi : - Menu Salade")
            console.log(prix_jeudi)
            break
        case '5':
            console.log("Vendredi : - Menu Poisson")
            console.log(prix_vendredi)
            break
        case '6':
            console.log("Samedi : - Menu Special")
            console.log(prix_samedi)
            break
        case '7':
            console.log("Dimanche : - Menu Special")
            console.log(prix_dimanche)
            break

        default:
            console.log("Tu en vie pas sur terre")
            break
    }
}
