function regle() {
    var check = document.getElementById("check");

    if (check.checked) {
        document.getElementById("reglement").style.visibility = "visible";
    } else {
        document.getElementById("reglement").style.visibility = "hidden";
    }
}