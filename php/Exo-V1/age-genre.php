<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
    <?php

        function AgeGenre($age, $sexe){
            if($age >= 21 & $age <= 40 & $sexe == "femme" ){
                echo("bienvenue a vous madame ");
            }
            
            else{
                echo("tu n'es pas le bienvenu");
            }
        }
        AgeGenre(42,"femme");
    ?>
</body>
</html>