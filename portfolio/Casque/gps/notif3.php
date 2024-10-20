<?php include "C:\wamp64/www/Casque_2.0/gps/templates/header.php"?>

<h1><a href="notif.php">ouvrier n°1</a></br></h1>
<h2>
<?php

$servername = "localhost";  // Adresse du serveur MySQL
$username = "root";  // Nom d'utilisateur MySQL
$password = "";  // Mot de passe MySQL
$dbname = "natifgaz";  // Nom de la base de données MySQL

// Créer une connexion
$conn = new mysqli($servername, $username, $password, $dbname);

// Vérifier la connexion
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

// Requête SQL pour sélectionner la date correspondant à l'ID le plus élevé pour chaque ouvrier
$sql1 = "SELECT tauxgaz,date FROM ouvrier3 WHERE id = (SELECT MAX(id) FROM ouvrier3)";  
$result1 = $conn->query($sql1);

echo"ouvrier n°3 : ";

if ($result1->num_rows > 0) {
    $row = $result1->fetch_assoc();
    $gaz = $row["tauxgaz"];
    $date = $row["date"];
    echo"il y-avait du gaz present chez l'ouvrier N°1 a : ", $date,"</br>";
  } else {
    echo"Pas d'information inquiétante</br>";
  }
  
  ?>
  </h2>