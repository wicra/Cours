

let Menu = {
    plats :[],
    ajouterPlat : function(nom , prix){
        const plat = {
            id: Date.now(),
            nom : nom,
            prix:  prix,
            termine: false,
        };
        this.plats.push(plat);
    },
    suprimerPlat : function(id){
        this.plats = this.plat.filter(function(plat){
            return this.plat.id != id ;
        })
    },
    marquerPlatTermine: function(id){
        let PlatIndex  = this.plats.findIndex(function(plat){
            
            if(PlatIndex !== -1){
                this.plats[PlatIndex].termine = true;
            }
        });
        
    },
    afficherPlat: function(){

    }
}

