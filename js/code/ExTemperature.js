
let lecturesTemperatures = [
    [21,23,35,32,19,20], //Cap 1
    [21,23,35,32,19,20], // Cap 2
    [21,23,35,32,19,20], // Cap 3
]

    let capteur1 = []
    let capteur2 = []
    let capteur3 = []
for(let i in lecturesTemperatures.length){


    let Stab1 = lecturesTemperatures[0]
    let Stab2 = lecturesTemperatures[1]
    let Stab3 = lecturesTemperatures[2]
    for(let o in Stab1){  
        if(Stab1[o] <= 18 || Stab1[o] >= 25){
            capteur1.push(Stab1[o]) 
        }
    }
    for(let o in Stab2){   
        if(Stab2[o] <= 18 || Stab2[o] >= 25){
            capteur2.push(Stab2[o]) 
        }
    }
    for(let o in Stab3){   
        if(Stab3[o] <= 18 || Stab3[o] >= 25){      
          capteur3.push(Stab3[o]) 
        }
    }

    alert(capteur1)
}
console.log(capteur1.join() + "Voici les erreur de temps du capteur ")
console.log(capteur2.join() + "Voici les erreur de temps du capteur ")
console.log(capteur3.join() + "Voici les erreur de temps du capteur ")

