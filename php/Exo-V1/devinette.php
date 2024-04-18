<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
        $nbDevine = 2;
        $compt = 0;
        $nbHazard = rand(1,9);
        while($nbHazard != $nbDevine){
            $compt = $compt +1;
          	echo ($nbHazard);
 
        }
		echo $compt

    ?>
</body>
</html>