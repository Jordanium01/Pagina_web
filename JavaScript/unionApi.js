//*$("#buscar").click(function(){

$(document).ready(() => {
    getAPI();
    $("#buscar").click(function() {
        getAPI();
    });
});

function getAPI() {
    $.get("Json/apiLista.json", function(data) {
        //console.log(data);
        $.each(data.categories, function(i, item) {
            /*
            $("#categorias").append(
                
                "<tr><td  class='text-center'>" + item.strTittle +
                "<img src='" + item.strGameThumbnail + "' class='img-proyect'></td>  <td>  <p class='desc-proyect'>" + item.strGameDescription + "</p></td>" +
                "<td> <iframe src =" + item.strGameStore + " frameborder = '0' class='store-proyect'>< /iframe> </td>" + "</tr>"
            );
                */

            $("#contenido-proyectos").append(
                "<div class='proyecto'>" +
                "<div class='cont-proyect-izq'>" +
                "<h2>" + item.strTittle + "</h2>" +
                "<img src='" + item.strGameThumbnail + "' class='img-proyect'>" +
                "</div>" +
                "<div>" +
                "<p class = 'desc-proyect'> " + item.strGameDescription + " </p>" +
                "</div >" +
                "<div>" +
                "<iframe src='" + item.strGameStore + "' frameborder='0' class='store-proyect'> </iframe>" +
                "</div>" +
                "</div>"
            );

        });
    });
}