$(document).ready(function() {
    // Устанавливаем время в секундах
    let timeLeft = 30;

    // Находим элементы таймера и ссылки
    const timerElement = document.getElementById('timer');
    const linkElement = document.getElementById('redirect_btn');

    // Функция для обновления таймера
    function updateTimer() {
        timerElement.textContent = timeLeft;

        if (timeLeft > 0) {
            timeLeft--;  // Уменьшаем время на 1 секунду
            setTimeout(updateTimer, 1000);  // Запускаем функцию снова через 1 секунду
        } else {
            linkElement.disabled = false;  // Делаем ссылку кликабельной
        }
    }

    // Запускаем таймер при загрузке страницы
    updateTimer();
});