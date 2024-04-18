<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    

    <?php
        $technologies =
        [
        "Langages" => ["PHP","JAVA","PYTHON"],
        "Framework" => ["SYMFONY","SPRING","DJANGO"],
        "Cms" => ["WORDPRESS","MAGNOLIA","MEZZANINE"]
        ];
        foreach ($technologies as $cle => $valeur) {
            echo ($cle . ":" .  $valeur[0] . " " . $valeur[1] . " " .$valeur[2]. "<br>");
   
        }
    ?>
</body>
</html>