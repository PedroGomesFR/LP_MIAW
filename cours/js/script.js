// function calcul_carre(){
//     var n = document.ex1.valeur1.value;
//     alert("le carré de "+n+" = "+n*n);
// }

function calcul_carre_p(){
    return alert("le carré de "+n+" = "+n*n);
} 

function multiplication(){
    var n = document.ex2.valeur2.value;
    for (i=1; i<=10; i++){
        document.write(n * i);
        document.write("<br>");
    }
}

function table_multiplication_prompt(N) {
 if (N == "") {
    N = 9
    for (i=1; i<=10; i++){
        document.write(N * i);
        document.write("<br>");
    }
 }else{
    for (i=1; i<=10; i++){
        document.write(N * i);
        document.write("<br>");
    }
 }
}

function table_multi(n){
    for (i=1; i<=10; i++){
        document.write("<br>");
        document.write(n * i);
    }
}

function table_multiplication_prompt_multi(){
    for (i=1; i<=10; i++){
        document.write("<br>");
        for (j=1; j<=10; j++){
            document.write(i * j);
            document.write("<br>");
        }
    }
}

function table_multiplication_textarea(n) {
    let result = "";
    for (let i = 1; i <= 10; i++) {
        let valtotal = n * i;
        result += `${n} x ${i} = ${valtotal}\n`;
    }
    document.getElementById("resultat").value = result;
}


