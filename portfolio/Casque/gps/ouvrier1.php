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

// Initialiser les variables pour la latitude et la longitude
$latitude = null;
$longitude = null;
$tauxgaz = null;
$temperature = null;

// Requête SQL pour récupérer la dernière latitude non nulle
$sql = "SELECT latitude, longitude FROM ouvrier1 WHERE latitude IS NOT NULL ORDER BY id DESC LIMIT 1";
$result = $conn->query($sql);

// Vérifier si une ligne est trouvée
if ($result->num_rows > 0) {
    $row = $result->fetch_assoc();
    $latitude = $row["latitude"];
    $longitude = $row["longitude"];
} else {
    echo "0 results";
}

// Requête SQL pour récupérer la dernière ligne avec taux de gaz et température non nuls
$sql2 = "SELECT tauxgaz, temperature FROM ouvrier1 ORDER BY id DESC LIMIT 1";
$result2 = $conn->query($sql2);

// Vérifier si une ligne est trouvée
if ($result2->num_rows > 0) {
    $row2 = $result2->fetch_assoc();
    $tauxgaz = $row2["tauxgaz"];
    $temperature = $row2["temperature"];
} else {
    echo "0 results";
}

// Fermer la connexion à la base de données
$conn->close();
?>

<!DOCTYPE html>
<html>

<head>
    <title>Ouvrier N°1</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
    <link rel="stylesheet" href="index.css">
</head>

<body>

    <?php include "C:/wamp64/www/Casque_2.0/gps/templates/header.php" ?>

    <a href="index.php">
        <h1>Ouvrier N°1</h1>
    </a>

    <div id="map" style="width: 600px; height: 400px;"></div>

    <script>
    var map = L.map('map');
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    // Utiliser les valeurs de latitude et de longitude récupérées depuis la base de données
    var latitude = <?php echo $latitude !== null ? $latitude : '0'; ?>; // Latitude
    var longitude = <?php echo $longitude !== null ? $longitude : '0'; ?>; // Longitude

    // Ajuster automatiquement le niveau de zoom pour que la carte soit centrée sur le marqueur
    map.setView([latitude, longitude], 12);

    // Ajouter un marqueur à la position spécifiée
    var marker = L.marker([latitude, longitude]).addTo(map)
        .bindPopup('Position GPS');
    </script>

    <div class="gaz">
        capteur de gaz :
        <?php 
        if ($tauxgaz >= 370) {
            echo "<div class='gazd'>Attention GAZ présent!!!</div>";
        } else {
            echo "Pas de gaz présent.";
        }
        ?>
    </div>

    <br>

    <div class="temp">
        capteur de température : 
        <?php 
        if ($temperature >= 18) {
            echo "<div class='tempd'>Attention forte température!! : " . $temperature . "°C</div>";
        } else {
            echo "Température normale : " . $temperature . "°C";
        }
        ?>
    </div>

</body>

</html>
