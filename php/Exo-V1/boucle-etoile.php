<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
    function etoile($nbEtoile){
        for($x = 0 ; $x <= $nbEtoile ; $x++){
            echo("*");
        }
        
    }
    etoile(5)
    function etoilecarre($carre){
        for($x = 0 ; $x <= $carre ; $x++){
            echo("*****" <br>);
        }

    }
    etoilecarre(4)

    ?>

</body>
</html>