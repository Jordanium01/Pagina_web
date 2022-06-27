//Validar con JQuery
var expr = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;

$(document).ready(() => {
    var CheckEmail = false;
    var CheckPassword = false;

    $("#form_email").blur(function(){
        CheckEmail = verifyEmail("#form_email");
     });
     

    $("#form_password").blur(function(){
        CheckPassword = verifyPassword("#form_password");
    });

    //Validar Cuando se envie el formulario
    $("#form_login").submit(function() {
        CheckEmail = verifyEmail("#form_email");
        CheckPassword = verifyPassword("#form_password");

        if (CheckEmail == false || CheckPassword == false) {
            //Evitar que el envio se realice
            return false;
        } 
    });

    //Validar cuando se de click al boton/link del formulario
    $("#linkLogin").click(function() {
            CheckEmail = verifyEmail("#form_email");
            CheckPassword = verifyPassword("#form_password");
    
            if (CheckEmail == false || CheckPassword == false) {
                //Evitar que el envio se realice
                return false;
            } 
    });

    
    
});


//Validar campo de correo
function verifyEmail(emailID){
    var correo = $(emailID).val().trim();
    if (correo.length == 0 || !expr.test(correo)) {
        //Reemplazar el mensaje de error
        if (correo.length == 0) { 
            setError(emailID, "#form_control_email", "#errorCorreo", "-No puede dejar su correo en blanco");
            return false;
        } else{ 
            setError(emailID, "#form_control_email", "#errorCorreo", "-Correo ingresado invalido");
            return false;
        }
    } else { //Si el correo si fue validado
        setSucces(emailID, "#form_control_email");
        return true;
    }
}

function verifyPassword(passID){
    var password = $(passID).val().trim();
    if (password.length == 0){
        setError(passID, "#form_control_password", "#errorPassw", "-No puede dejar su contraseña en blanco");
        return false;
    } else {
        setSucces(passID, "#form_control_password");
        return true;
    }
}

//Establecer que la seccion esta mal
function setError(intputID, controlID, messageID, message){
    $(intputID).css("border-color", "var(--color-error)");
    //Quitar clase (si no esta no la quita)
    $(controlID).removeClass("success");
    //Poner la buena
    $(controlID).addClass("error");
    $(messageID).text(message);
}

//Establecer que la seccion esta bien
function setSucces(intputID, controlID){
    $(intputID).css("border-color", "var(--color-success)");
    $(controlID).removeClass("error");
    $(controlID).addClass("success");
}
