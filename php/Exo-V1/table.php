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
            array("INE", "Nom", "Prenom", "Spécialité", "Moyenne", "Mention"),
            array("1230", "ALLON", "LEVY", "TIN", "13", "BIEN"),
            array("123", "BACARD", "HUGO", "CDI", "12", "A BIEN"),
            array("1234", "BAKER", "MATTHEW", "INFO", "17", "TRES BIEN")
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