<?php
include "C:\wamp64/www/Casque_2.0/gps/templates/header.php";
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
</br>

                <form method="post" action="recherche.php">
                  <input type="text" name="monBouton" placeholder="AAAA-MM-JJ"/>
                  <input type="submit"  value="Rechercher">
                </form>
</body>
</html>
<h1><a href="notif.php">retour</a></br></h1>
<h2>
<?php

$servername = "localhost"; // Adresse du serveur MySQL
$username = "root"; // Nom d'utilisateur MySQL
$password = ""; // Mot de passe MySQL
$dbname = "casque"; // Nom de la base de données MySQL

// Créer une connexion
$conn = new mysqli($servername, $username, $password, $dbname);

// Vérifier la connexion
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

// Initialiser les variables pour la latitude et la longitude
$latitude = null;
$longitude = null;

// Requête SQL pour récupérer la dernière latitude non nulle
$sql = "SELECT latitude, longitude FROM ouvrier1 WHERE latitude IS NOT NULL ORDER BY id DESC LIMIT 1";
$result = $conn->query($sql);

// Vérifier si une ligne est trouvée
if ($result->num_rows > 0) {
    $row = $result->fetch_assoc();
    $latitude = $row["latitude"];
    $longitude = $row["longitude"];
}

// Requête SQL pour sélectionner la date correspondant à l'ID le plus élevé pour chaque ouvrier
$sql1 = "SELECT tauxgaz, date, temperature FROM ouvrier1";
$result1 = $conn->query($sql1);

if ($result1->num_rows > 0) {
  // Output data of each row
  foreach ($result1 as $row) {
    if ($row["tauxgaz"] >= 300 || $row["temperature"] >= 70) {
      echo "gaz ou haute temperature present: Taux de Gaz : " . $row["tauxgaz"] . " | temperature: " . $row["temperature"] . " - Date: " . $row["date"] . "<br>";
    }
  }
} else {
  echo "Pas d'information inquiétante";
}



?>
</h2>
