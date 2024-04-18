<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <style>
      form{
        display: block;
        justify-content: center;
      }
      form input{
        display: block;
      }
      
    </style>


    <form method = 'post'>
        <div class="nom">
            <h4>nom</h4>
            <input type="text" name="nom">
            <div class="message">
                
            </div>
        </div>
        <div class="age">
            <h4>age</h4>
            <input type="number" name="number" id="">
            <div class="message">
                
            </div>
        </div>
        <div class="mail">
            <h4>mail</h4>
            <input type="email" name="email" id="">
            <div class="message">
                
            </div>
        </div>
        
        <input type="submit" value="submit">
    </form>

    <?php
        while(isset($_POST['submit'])){
            $nom = $_POST['text'];
            $age = $_POST['number'];
            $mail = $_POST['email'];
            $messagevide = "<p>vide</p>";
            
            if(!empty($nom) & !empty($age) & !empty($mail)){
                echo ("Les donnés sont bien envoyé");
            }
            else if(empty($age)){
                echo ("Les donnés sont bien envoyé");
            }
            else if(!empty($mail)){
                echo ("Les donnés sont bien envoyé");
            }
            else{
                echo($messagevide);
            }
        }

    ?>

</body>
</html>