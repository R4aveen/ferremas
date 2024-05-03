function accion() {
    console.log('esta funcionando');
    var elementosNav = document.querySelectorAll('.nav-enlace, .nav-boton');
    elementosNav.forEach(function(elemento) {
        elemento.classList.toggle('desaparece');
    });
}

// Ocultar el menú al cargar la página
var elementosNav = document.querySelectorAll('.nav-enlace, .nav-boton');
elementosNav.forEach(function(elemento) {
    elemento.classList.add('desaparece');
});


