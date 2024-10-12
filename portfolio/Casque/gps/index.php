<?php 
// Connexion à la base de données
$servername = "localhost";  // Adresse du serveur MySQL
$username = "root";  // Nom d'utilisateur MySQL
$password = "";  // Mot de passe MySQL
$dbname = "casque";  // Nom de la base de données MySQL

// Créer une connexion
$conn = new mysqli($servername, $username, $password, $dbname);

// Vérifier la connexion
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

// Requête SQL pour sélectionner la date correspondant à l'ID le plus élevé pour chaque ouvrier
$sql1 = "SELECT date FROM ouvrier1 WHERE id = (SELECT MAX(id) FROM ouvrier1)";  
$result1 = $conn->query($sql1);

$sql2 = "SELECT date FROM ouvrier2 WHERE id = (SELECT MAX(id) FROM ouvrier2)";  
$result2 = $conn->query($sql2);

$sql3 = "SELECT date FROM ouvrier3 WHERE id = (SELECT MAX(id) FROM ouvrier3)";  
$result3 = $conn->query($sql3);

// Récupérer les données pour chaque ouvrier
if ($result1->num_rows > 0) {
  $row = $result1->fetch_assoc();
  $date1 = $row["date"];
} else {
  $date1 = "jamais utilisé.";
}

if ($result2->num_rows > 0) {
  $row = $result2->fetch_assoc();
  $date2 = $row["date"];
} else {
  $date2 = "jamais utilisé.";
}

if ($result3->num_rows > 0) {
  $row = $result3->fetch_assoc();
  $date3 = $row["date"];
} else {
  $date3 = "jamais utilisé.";
}

// Fermer la connexion à la base de données
$conn->close();
?>

<!DOCTYPE html>
<html>

<head>
    <title>Localiser un GPS avec une trame NMEA et OpenStreetMap</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
    <link rel="stylesheet" href="index.css">
    <link rel="icon" href="/images/casques.png" type="image/x-icon">
</head>

<body>


    <?php include "C:\wamp64/www/casque_2.0/gps/templates/header.php"?>
    <div class="ouvriers">
        <h1>
            <div class="indexcasque1">
                <a href="ouvrier1.php">Casque n°1</a> dernière utilisation : <?php echo $date1 ?> </br>
            </div>

            <div class="indexcasque2">
                <a href="ouvrier2.php">Casque n°2</a> dernière utilisation : <?php echo $date2 ?> </br>
            </div>

            <div class="indexcasque3">
                <a href="ouvrier3.php">Casque n°3</a> dernière utilisation : <?php echo $date3 ?> </br>
            </div>
        </h1>
    </div>

    <div class="imgcasque">
        <img src="images/casque.png">
    </div>
    
    
     <h1><a href="notif.php">Historique des activites</br></h1>
             

</body>

</html>