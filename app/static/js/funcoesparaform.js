function Apenasletras(input){
    var regex = /[^a-z]/gi;
    // var regex = /[([aA-zZ]+)]/gi;
    input.value = input.value.replace(regex," ");
}

function mascara_cpf(i) {
    
    var v = i.value;
   
   if(isNaN(v[v.length-1])){ // impede entrar outro caractere que não seja número
      i.value = v.substring(0, v.length-1);
      return;
   }
   
   i.setAttribute("maxlength", "14");
   if (v.length == 3 || v.length == 7) i.value += ".";
   if (v.length == 11) i.value += "-";

}

function mascara_cnpj(i) {
    // var cpf = document.getElementById('cpf')
    
    var v = i.value;
       
    if(isNaN(v[v.length-1])){ // impede entrar outro caractere que não seja número
       i.value = v.substring(0, v.length-1);
       return;
    }
    
    i.setAttribute("maxlength", "18");
    if (v.length == 2 || v.length == 6) i.value += ".";
    if (v.length == 10) i.value += "/";
    if (v.length == 15) i.value += "-";
 

}

