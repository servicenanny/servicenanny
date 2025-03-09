$(document).ready(function() {
    // Обработка выбора города
    $('.cities').on('click', function() {
        const cityId = $(this).data('city-id');
        // Заполняем скрытое поле формы
        $('#id_city').val(cityId);
        // Отправляем форму
        $('#update_city_form').submit();
    });
});