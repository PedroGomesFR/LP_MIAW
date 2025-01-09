var w
function traiter_info() {
    var nom = document.getElementById('nom').value;
    var prenom = document.getElementById('prenom').value;
    var password = document.getElementById('password').value;
    var radios = document.querySelector('input[name="spe"]:checked').value;
    var options= 'toolbar=no, width=300px, height=400px'
    var diciplicePref = document.querySelector('select[name="dicipline"]').value;
    var checkboxes = document.querySelectorAll('input[type="checkbox"]:checked');
    var selectedValues = Array.from(checkboxes).map(cb => cb.name); 

    w = window.open("","Fiche_de_renseignements",options);
    w.document.write('<style>body { background-color: yellow; }</style>');;
    w.document.write("Votre nom : "+ nom + "<br>");
    w.document.write("Votre prénom : "+ prenom + "<br>");
    w.document.write("Votre mot de passe : "+ password + "<br>");
    w.document.write("Votre spécialité : "+ radios + "<br>");
    w.document.write("Votre dicipline préféré : "+ diciplicePref + "<br>");
    w.document.write("Votre inscription : "+ selectedValues + "<br>");
}
function fermer(){
    w.close();
}

function effacer(){
    document.getElementById('nom').value = "";
    document.getElementById('prenom').value = "";
    document.getElementById('password').value = "";
}


