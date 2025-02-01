document.addEventListener("DOMContentLoaded", function() {
    // Обработчики для видео
    const videos = document.querySelectorAll('.video');

    videos.forEach(video => {
        const playButton = video.closest('.card-review').querySelector('.play-btn-video');

        // Управление воспроизведением видео
        playButton.addEventListener('click', function() {
            if (video.paused) {
                video.play();
                playButton.innerHTML = '<i class="bi bi-pause-fill"></i>';
                playButton.classList.add('playing');
            } else {
                video.pause();
                playButton.innerHTML = '<i class="bi bi-play-fill"></i>';
                playButton.classList.remove('playing');
            }
        });

        // Обновление прогресс-бара для видео
        video.addEventListener('timeupdate', function() {
            const progressBar = video.closest('.card-review').querySelector('.progress-bar');
            if (progressBar) {
                const progress = (video.currentTime / video.duration) * 100;
                progressBar.style.width = `${progress}%`;
            }
        });
    });

    // Обработчики для аудио
    const audios = document.querySelectorAll('.audio');

    audios.forEach(audio => {
        const playButton = audio.closest('.controls-box').querySelector('.play-btn');
        const progressBar = audio.closest('.controls-box').querySelector('.progress-bar');
        const progressContainer = audio.closest('.controls-box').querySelector('.progress-container');
        const speedText = audio.closest('.controls-box').querySelector('.speed-text');

        // Управление воспроизведением аудио
        playButton.addEventListener('click', function() {
            if (audio.paused) {
                audio.play();
                playButton.innerHTML = '<i class="bi bi-pause-fill"></i>';
            } else {
                audio.pause();
                playButton.innerHTML = '<i class="bi bi-play-fill"></i>';
            }
        });

        // Перемотка по клику на прогресс-бар
        progressContainer.addEventListener('click', function(e) {
            const progressContainerWidth = progressContainer.offsetWidth; 
            const clickX = e.offsetX; 
            const newTime = (clickX / progressContainerWidth) * audio.duration; 
            audio.currentTime = newTime;  // Устанавливаем новое время
        });

        // Обновление прогресс-бара для аудио
        audio.addEventListener('timeupdate', function() {
            const progress = (audio.currentTime / audio.duration) * 100;
            progressBar.style.width = `${progress}%`;
        });

        // Изменение скорости воспроизведения аудио
        speedText.addEventListener('click', function() {
            if (audio.playbackRate === 1) {
                audio.playbackRate = 1.5;
                speedText.textContent = '1.5x';
            } else if (audio.playbackRate === 1.5) {
                audio.playbackRate = 2;
                speedText.textContent = '2x';
            } else {
                audio.playbackRate = 1;
                speedText.textContent = '1x';
            }
        });
    });
});
