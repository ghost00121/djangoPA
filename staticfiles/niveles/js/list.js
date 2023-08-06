$(function () {
    $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            { "data": "IDnivel" },
            { "data": "modalidad" },
            { "data": "nivel" },
            { "data": "frecuencia" },
            { "data": "horario" },
            {
                "data": "id",
                "render": function (data, type, row) {
                    var buttons = '<a href="/erp/niveles/update/' + data + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/erp/niveles/delete/' + data + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        dom: 'Blfrtip', // Agrega el contenedor de los botones de exportación y el cambio de longitud
        buttons: [
            'copy', 'csv', 'excel', 'pdf', 'print' // Agrega los botones de exportación
        ],
        lengthChange: true, // Muestra el campo de cambio de longitud
        initComplete: function (settings, json) {

        }
    });
});

