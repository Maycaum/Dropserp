function Apenasletras(input){
    var regex = /[^a-z]/gi;
    // var regex = /[([aA-zZ]+)]/gi;
    input.value = input.value.replace(regex,"");
}