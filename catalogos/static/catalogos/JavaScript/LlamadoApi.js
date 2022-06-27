$(document).ready(() => {
    getAPI();
    console.log("llamado");
});

function getAPI() {
    $.get("/static/catalogos/Json/apiLista.json", function(data) {
        //console.log(data);
        $.each(data.categories, function(i, item) {
            $("#contenido-proyectos").append(
                "<div class='proyecto'>" +
                "<div class='cont-proyect-izq'>" +
                "<h2>" + item.strTittle + "</h2>" +
                '<img src="' + item.strGameThumbnail + '" class="img-proyect">' +
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