<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

    <form method='post'>
        <input id="nb1" name="nb1" type='number'>
        
        <select name="Calcule">
          <option value="">--choisisez--</option>
          <option value="Plus">Plus</option>
          <option value="Moins">Moins</option>
          <option value="Diviser">Diviser</option>
          <option value="Multiplier">Multiplier</option>
        </select>
        
        <input id="nb2" name="nb2" type='number'>
        <input type='submit' name='submit'>
    </form>

    <?php
        if(isset($_POST['submit'])){
            if(!empty($_POST['nb1']) && !empty($_POST['nb2']) && !empty($_POST['Calcule'])){
                $nb1 = $_POST['nb1'];
                $nb2 = $_POST['nb2'];
                $operation = $_POST['Calcule'];
                echo "$nb1 $operation $nb2 = <br>";
                switch($operation){
                    case "Plus":
                        echo ($nb1 + $nb2);
                        break;
                    case "Moins":
                        echo ($nb1 - $nb2);
                        break;
                    case "Diviser":
                        echo ($nb1 / $nb2);
                        break;
                    case "Multiplier":
                        echo ($nb1 * $nb2);
                        break;
                    default:
                        echo "Opération non reconnue";
                }
            } else {
                echo "Veuillez remplir tous les champs.";
            }
        }
    ?>

</body>
</html>
