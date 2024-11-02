$(document).ready(function () {
    $('.toAnchor').on('click', function () {
        $('#offcanvasNavbar').offcanvas('hide');
    });
});

document.addEventListener("DOMContentLoaded", function(){
    var myOffcanvas = document.getElementById('offcanvasNavbar');
    var bsOffcanvas = new bootstrap.Offcanvas(myOffcanvas);
    document.getElementById("open-menu").addEventListener('click',function (e){
      e.preventDefault();
      e.stopPropagation();
      bsOffcanvas.toggle();
    });
  });