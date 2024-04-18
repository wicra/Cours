<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

    <?php
    $multiple = 5;
    $nombre = 3;
    
    $verif = $multiple / 3;
    if( $verif == is_int($verif)){
        echo ($nombre ,"est multiple de" $multiple );
    }
    else{
        echo ("c'est pas son multiple");
    }
    ?>
</body>
</html>