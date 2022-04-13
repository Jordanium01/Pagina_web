const form = document.getElementById('form_contacto');
const nombre = document.getElementById('form_name');
const email = document.getElementById('form_email');
const asunto = document.getElementById('form_asunto');
const mensaje = document.getElementById('form_message');


form.addEventListener('submit', e => {
    e.preventDefault();
    checkInputs();

});

function checkInputs() {
    var nombreValue = nombre.value.trim();
    var emailValue = email.value.trim();
    const emailRegex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    var asuntoValue = asunto.value.trim();
    var mensajeValue = mensaje.value.trim();
    //const emailValue = email.Value.trim();
    //Validar que los campos no esten vacios
    if (nombreValue === '') {
        setErrorFor(nombre, 'No puede dejar su nombre en blanco');
    } else {
        setSuccesFor(nombre);
    }

    if (emailValue === '') {
        setErrorFor(email, 'No puede dejar su correo en blanco');
    } else if (!emailRegex.test(emailValue)) { //if (!emailRegex.test(emailValue)) { //isEmail(emailValue)
        setErrorFor(email, 'No ingreso un correo válido');
    } else {
        setSuccesFor(email);
    }

    if (asuntoValue === '') {
        setErrorFor(asunto, 'No puede dejar el asunto en blanco');
    } else {
        setSuccesFor(asunto);
    }


    if (mensajeValue === '') {
        setErrorFor(mensaje, 'No puede dejar el mensaje en blanco');
    } else {
        setSuccesFor(mensaje);
    }

}

//Mostrar el error

function setErrorFor(input, message) /*ID input, mensaje a mostrar*/ {
    const formControl = input.parentElement;
    const small = formControl.querySelector('small');
    formControl.className = 'form_control error'
    small.innerText = message;
}

//Mostrar el check
function setSuccesFor(input) {
    const formControl = input.parentElement;
    formControl.className = 'form_control success';
}