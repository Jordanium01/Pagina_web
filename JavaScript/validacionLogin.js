const form = document.getElementById('form_login');
const email = document.getElementById('form_email');
const password = document.getElementById('form_password');


form.addEventListener('submit', e => {
    e.preventDefault();
    checkInputs();

});

function checkInputs() {
    var emailValue = email.value.trim();
    const emailRegex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    var PasswordValue = password.value.trim();

    //Validar que los campos no esten vacios
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