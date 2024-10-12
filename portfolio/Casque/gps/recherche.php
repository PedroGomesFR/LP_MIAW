<h2>
<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "casque";

include "C:\wamp64/www/Casque_2.0/gps/templates/header.php";

// Créer une connexion
$conn = new mysqli($servername, $username, $password, $dbname);

// Vérifier la connexion
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (isset($_POST['monBouton'])) {
        // Vérifier l'état de la connexion avant d'utiliser real_escape_string
        if ($conn->connect_errno) {
            die("Erreur de connexion : " . $conn->connect_error);
        }

        $valeurBouton = $conn->real_escape_string($_POST['monBouton']);

        // Vérifier l'état de la connexion avant d'exécuter la requête SQL
        if ($conn->connect_errno) {
            die("Erreur de connexion : " . $conn->connect_error);
        }

        $sql = "SELECT * FROM ouvrier1 WHERE date LIKE '%$valeurBouton%'";

        $result = $conn->query($sql);

        if ($result === false) {
            die("Erreur lors de l'exécution de la requête : " . $conn->error);
        }

        $found = false;

        if ($result->num_rows > 0) {
            while ($row = $result->fetch_assoc()) {
                $tauxgaz = $row["tauxgaz"];
                $temperature = $row["temperature"];
                if ($tauxgaz >= 300 || $temperature >= 70) {
                    echo "Gaz ou haute température présent : Taux de Gaz : " . $tauxgaz . " | Température : " . $temperature . " - Date : " . $row["date"] . "<br>";
                    $found = true;
                }
            }
        }

        if (!$found) {
            echo "Pas d'information trouvée";
        }
    }
}

// Fermer la connexion
$conn->close();
?>
</h2>