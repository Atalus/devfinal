var nombre = "Jocelyn"//variable Global
var n1 = 4;
function suma(){
	var n1 = document.querySelector('#primerValor').value; //variable Local únicamente va a vivir dentro de la unción
	var n2 = document.querySelector('#segundoValor').value;
	var resultado = parseInt(n1) + parseInt(n2);
	alert(resultado);
	if(resultado > 15){
		document.querySelector('#colorido').style.backgroundColor="yellow";
	}else if (resultado === 15) {
		document.querySelector('#colorido').style.backgroundColor="green"
	}else {
		document.querySelector('#colorido').style.backgroundColor="orange"
	}
};
function resta(){
	var n2 = document.querySelector('#segundoValor').value;
	var resultado = parseInt(n1) - parseInt(n2);
	alert(resultado);
	if(resultado <10){
		document.querySelector('#colorido').style.backgroundColor="blue";
	}
};
function colorNuevo() {
	document.querySelector('#colorido').style.backgroundColor = "red";
	document.querySelector('#colorido').style.fontFamily = "comic";
};
alert(nombre);



compu = Math.random()*3;
if (compu<1) {
	compuTirada
}