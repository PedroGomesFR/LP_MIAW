    <!DOCTYPE html>
    <html lang="fr">
    
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="index.css">
        <meta http-equiv="refresh" content="10">
        <link rel="icon" href="/images/casques.png" type="image/x-icon">
        <title>Casques</title>
    </head>
    
        <body>
        <header>
            <div class="moni">
                <h1> Monitoring Chantier </h1>
            </div>
            
    
            <div class="notif blink">
    <div class="notif">
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

    // Requête SQL pour vérifier si une valeur spécifique est présente dans la base de données
    $valeur_specifique = "300";
    $sql1 = "SELECT tauxgaz FROM ouvrier1 WHERE tauxgaz >= '$valeur_specifique'";
    $result1 = $conn->query($sql1);

    $sql2 = "SELECT tauxgaz FROM ouvrier2 WHERE tauxgaz >= '$valeur_specifique'";
    $result2 = $conn->query($sql2);

    $sql3 = "SELECT tauxgaz FROM ouvrier3 WHERE tauxgaz >= '$valeur_specifique'";
    $result3 = $conn->query($sql3);

    // Fermer la connexion à la base de données
    $conn->close();

    // Connexion à la base de données pour l'insertion
    $servername2 = "localhost";  // Adresse du serveur MySQL
    $username2 = "root";  // Nom d'utilisateur MySQL
    $password2 = "";  // Mot de passe MySQL
    $dbname2 = "natifgaz";  // Nom de la base de données MySQL
    // Créer une connexion à la base de données pour l'insertion
    $conn2 = new mysqli($servername2, $username2, $password2, $dbname2);

    // Vérifier la connexion à la base de données pour l'insertion
    if ($conn2->connect_error) {
        die("Connection failed: " . $conn2->connect_error);
    }
    // Insérer les résultats dans la table notifgaz
    if ($result1->num_rows > 0) {
        $row = $result1->fetch_assoc();
        $tauxgaz1 = $row["tauxgaz"];
        $sql_insert1 = "INSERT INTO ouvrier1 (tauxgaz) VALUES ('$tauxgaz1')";
        $conn2->query($sql_insert1);
        if ($tauxgaz1 <= 300){
        echo "Attention, Gaz Présent chez l'ouvrier n°1</br>";
        }
    }

    if ($result2->num_rows > 0) {
        $row = $result2->fetch_assoc();
        $tauxgaz2 = $row["tauxgaz"];
        $sql_insert2 = "INSERT INTO tauxgaz (natifgaz) VALUES ('$tauxgaz2')";
        $conn2->query($sql_insert2);
        if ($tauxgaz2 <= 300){
            echo "Attention, Gaz Présent chez l'ouvrier n°2</br>";
            }
    }

    if ($result3->num_rows > 0) {
        $row = $result3->fetch_assoc();
        $tauxgaz3 = $row["tauxgaz"];
        $sql_insert3 = "INSERT INTO tauxgaz (natifgaz) VALUES ('$tauxgaz3')";
        $conn2->query($sql_insert3);
        if ($tauxgaz3 <= 300){
            echo "Attention, Gaz Présent chez l'ouvrier n°3 </br>";
            }
    }

    // Fermer la connexion à la base de données pour l'insertion
    $conn2->close();
?>

</div>
</div>
</header>

</body>

</html>