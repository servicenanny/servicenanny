$(document).ready(function () {
    $('#is_worker').click(function() {
        $("#id_client_type").prop('value', 'N');
    });
    $('#is_not_worker').click(function() {
        $("#id_client_type").prop('value', 'P');
    });
});