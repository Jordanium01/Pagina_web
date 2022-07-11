//Confirmar al eliminar un proyecto
function confirmar() {
    var Respuesta = confirm("¿Estas seguro de querer eliminar?")

    if (Respuesta == true) {

        return true;
    } else {

        return false;
    }
}


function DeleteGame(urlID){
    swal({
        title: "¿Estas seguro?",
        text: "EL juego sera borrado permanentemente",
        icon: "warning",
        buttons: [
          'No, cancelar',
          'Si, estoy seguro'
        ],
        dangerMode: true,
      }).then(function(isConfirm) {
        if (isConfirm) {
          swal({
            title: 'Juego eliminado',
            text: 'El juego a sido eliminado de la base de datos',
            icon: 'success'
          }).then(function() {
            window.location = 'http://127.0.0.1:8000/eliminar_proyecto/' + urlID;
          });
        } else {
          swal("Cancelado", "El juego esta a salvo hasta que alguien vuelva a presionar el boton :]", "error");
        }
      });


    return false;
}

function BorrarEstadistica(EstadisID){
    swal({
        title: "¿Estas seguro?",
        text: "La estadistica de este juego sera borrado de forma permanente",
        icon: "warning",
        buttons: [
          'No, cancelar',
          'Si, estoy seguro'
        ],
        dangerMode: true,
      }).then(function(isConfirm) {
        if (isConfirm) {
          swal({
            title: 'Estadistica eliminada',
            text: 'La estadistica a sido eliminada de la base de datos',
            icon: 'success'
          }).then(function() {
            window.location = 'http://127.0.0.1:8000/eliminar_estadistica/' + EstadisID;
          });
        } else {
          swal("Cancelado", "La estadistica esta a salvo hasta que alguien vuelva a presionar el boton :]", "error");
        }
      });


    return false;
}