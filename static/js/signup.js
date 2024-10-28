$(document).ready(function () {
    $('#is_worker').click(function() {
        $("#id_is_worker").prop('checked', true);
    });
    $('#is_not_worker').click(function() {
        $("#id_is_worker").prop('checked', false);
    });
});