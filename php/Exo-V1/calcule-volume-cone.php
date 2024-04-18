<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php

    function volume($rayon,$hauteur){
        $volume = ((($rayon**2) * $hauteur)* pi)/3;
        echo($volume);
    }
    
    volume(4,6)
    ?>
</body>
</html>