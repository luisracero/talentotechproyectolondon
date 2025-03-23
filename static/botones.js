
function seleccionarOpcion(boton) {
    document.querySelectorAll('opcion-btn').forEach(function (btn) {
        btn.classList.remove('seleccionado');
    });
    boton.classList.add('seleccionado');
}