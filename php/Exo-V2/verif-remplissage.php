<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

    <form method = 'post'>
        <input type="text">
        <input type="number" name="number" id="">
        <input type="email" name="email" id="">
        <input type="submit" value="submit">
    </form>
    <?php
        if(isset($_POST['submit'])){
            if(!empty($_POST['text']) & !empty($_POST['number']) & !empty($_POST['email'])){
                echo ("Les donnés sont bien envoyé")
            }
            else{
                echo("veuillez remplir tout les champs")
            }
        }

    ?>

</body>
</html>