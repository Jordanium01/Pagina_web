//Validar con JQuery
var expr = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;

$(document).ready(() => {
    //$("#errorCorreo").hide();
    $("#form_login").submit(function() {
        //alert("formulario");
        var correo = $("#form_email").val().trim();
        var password = $("#form_password").val().trim();
        var CheckEmail = false;
        var CheckPassword = false

        if (correo.length == 0 || !expr.test(correo)) {
            //Volver la parte del css en visible
            $('#errorCorreo').css("visibility", "visible");
            //Ponerle los bordes rojos
            $('#form_email').css("border-color", "var(--color-error)");
            //Reemplazar el mensaje de error
            if (correo.length == 0) { $("#errorCorreo").text("No puede dejar su correo en blanco"); } else { $("#errorCorreo").text("No ingreso un correo válido"); }
            //Establecer los iconos
            $("#I_correo_Succes").css("visibility", "hidden");
            $("#I_correo_Error").css("visibility", "visible");
        } else { //Si el correo si fue validado
            $('#errorCorreo').css("visibility", "hidden");
            $('#form_email').css("border-color", "var(--color-success)");
            $("#I_correo_Succes").css("visibility", "visible");
            $("#I_correo_Error").css("visibility", "hidden");
            CheckEmail = true;
        }

        if (password.length == 0) {
            //Volver la parte del css en visible
            $('#errorPassw').css("visibility", "visible");
            //Ponerle los bordes rojos
            $('#form_password').css("border-color", "var(--color-error)");
            //Reemplazar el mensaje de error
            $("#errorPassw").text("No puede dejar la contraseña en blanco");
            //Establecer los iconos
            $("#I_pass_Succes").css("visibility", "hidden");
            $("#I_pass_Error").css("visibility", "visible");
        } else {
            //Volver la parte del css invisible
            $('#errorPassw').css("visibility", "hidden");
            //Ponerle los bordes verdes
            $('#form_password').css("border-color", "var(--color-success)");
            //Establecer los iconos
            $("#I_pass_Succes").css("visibility", "visible");
            $("#I_pass_Error").css("visibility", "hidden");
            CheckPassword = true;
        }

        if (CheckEmail == false || CheckPassword == false) {
            return false;
        }

    });
});