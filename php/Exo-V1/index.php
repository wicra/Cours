<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <style>
        span{
            color:green;
            font-weight:bold;
        }
    </style>
    <?php
    #fonction 
    
    function nom($prenom,$age,){
        echo("bonjour je m'appelle ,<span>$prenom</span> j'ai <span>$age</span>,ans");

    }
    nom("wicra",49)

    ?>

</body>
</html>