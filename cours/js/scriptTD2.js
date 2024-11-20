function reglement(){
    if (document.getElementById("check").checked == true){

        document.getElementById("bouton").disabled = false; 

    }else{
        document.getElementById("bouton").disabled = true;
    }
}

function quelle_heure(){
    var date = new Date();
    var hour = date.getHours();
    var minute = date.getMinutes();
    var seconde = date.getSeconds();
    document.getElementById("heure").value = hour + ":" + minute + ":" + seconde;
    document.getElementById("Date").value = date;
    setTimeout("quelle_heure()", 500);
}