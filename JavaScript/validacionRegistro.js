const form = document.getElementById('form_registro');
const nombre = document.getElementById('form_name');
const email = document.getElementById('form_email');
const password = document.getElementById('form_password');
const password_2 = document.getElementById('form_password_2');


form.addEventListener('submit', e => {
    e.preventDefault();
    checkInputs();

});

function checkInputs() {
    var nombreValue = nombre.value.trim();
    var emailValue = email.value.trim();
    const emailRegex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    var PasswordValue = password.value.trim();
    var Password2Value = password_2.value.trim();

    //Validar que los campos no esten vacios
    if (nombreValue === '') {
        setErrorFor(nombre, 'No puede dejar su nombre en blanco');
    } else {
        setSuccesFor(nombre);
    }

    if (emailValue === '') {
        setErrorFor(email, 'No puede dejar su correo en blanco');
    } else if (!emailRegex.test(emailValue)) { //if (!emailRegex.test(emailValue)) { //isEmail(emailValue)
        setErrorFor(email, 'No ingreso un email válido');
    } else {
        setSuccesFor(email);
    }

    if (PasswordValue === '') {
        setErrorFor(password, 'No puede dejar la contraseña blanco');
    } else {
        setSuccesFor(password);
    }


    if (Password2Value === '') {
        setErrorFor(password_2, 'No puede dejar la contraseña blanco');
    } else if (Password2Value != PasswordValue) {
        setErrorFor(password_2, 'Las contraseñas deben de ser iguales');
    } else {
        setSuccesFor(password_2);
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