$(document).ready(function() {
    // Обработка выбора города
    $('.cities').on('click', function() {
        const cityId = $(this).data('city-id');
        alert(cityId)
        // Заполняем скрытое поле формы
        $('#id_city').val(cityId);
        alert($('#id_city').val())
        // Отправляем форму
        $('#update_city_form').submit();
    });
});