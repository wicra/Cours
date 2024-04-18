<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
    <?php
    
        // Contenu à afficher dans le tableau
        $contenu = array(
            array("*", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"),
            array("1", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"),
            array("*", "1", "2", "3", "4", "5", "6", "7", "8", "9", "20"),
            array("*", "1", "2", "3", "4", "5", "6", "7", "8", "9", "30"),
            array("*", "1", "2", "3", "4", "5", "6", "7", "8", "9", "40"),
            array("1", "1", "2", "3", "4", "5", "6", "7", "8", "9", "50"),
            array("*", "1", "2", "3", "4", "5", "6", "7", "8", "9", "60"),
            array("*", "1", "2", "3", "4", "5", "6", "7", "8", "9", "70"),
            array("*", "1", "2", "3", "4", "5", "6", "7", "8", "9", "80"),
            array("1", "1", "2", "3", "4", "5", "6", "7", "8", "9", "90"),
            array("*", "1", "2", "3", "4", "5", "6", "7", "8", "9", "100"),

        );

        // Nombre de lignes et de colonnes
        $lignes = count($contenu);
        $colonnes = count($contenu[0]);

        // Début du tableau
        echo "<table border='1'>";

        // Boucle pour les lignes
        for ($i = 0; $i < $lignes; $i++) {
            echo "<tr>";

            // Boucle pour les colonnes
            for ($j = 0; $j < $colonnes; $j++) {
                echo "<td>" . $contenu[$i][$j] . "</td>";
            }

            echo "</tr>";
        }

        // Fin du tableau
        echo "</table>";
    ?>
</body>
</html>