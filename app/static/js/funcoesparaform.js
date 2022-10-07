function Apenasletras(input){
    var regex = /[^a-z]/gi;
    // var regex = /[([aA-zZ]+)]/gi;
    input.value = input.value.replace(regex," ");
}

function mascara_cpf() {
    var cpf = document.getElementById('cpf')
    if(cpf.value.length == 3 || cpf.value.length == 7) { 
        cpf.value+="."
    } else if(cpf.value.length == 11) { 
        cpf.value +="."
    }
}

function mascara_cnpj() {
    var cpf = document.getElementById('cpf')
    if(cpf.value.length == 2 || cpf.value.length == 7) { 
        cpf.value+="."
    } else if(cpf.value.length == 11) { 
        cpf.value +="."
    }
}


