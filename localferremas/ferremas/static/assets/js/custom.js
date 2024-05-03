(function ($) {

  "use strict";

  // Función para mostrar el spinner
  function showSpinner() {
    $('.preloader').fadeIn(); // Muestra el spinner
  }

  // Función para ocultar el spinner
  function hideSpinner() {
    $('.preloader').fadeOut(); // Oculta el spinner
  }

  // Esta función se ejecutará cuando la página haya cargado completamente
  window.onload = function () {
    // Se oculta el spinner una vez que la página esté completamente cargada
    hideSpinner();
  };

  // NAVBAR
  $(".navbar").headroom();

  $('.navbar-collapse a').click(function () {
    $(".navbar-collapse").collapse('hide');
  });

  $('.slick-slideshow').slick({
    autoplay: true,
    infinite: true,
    arrows: false,
    fade: true,
    dots: true,
  });

  $('.slick-testimonial').slick({
    arrows: false,
    dots: true,
  });

})(window.jQuery);
