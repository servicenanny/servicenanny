$(document).ready(function () {
    const audioPlayer = document.getElementById('audioPlayer');
    const playPauseBtn = document.getElementById('playPauseBtn');
    const progressBar = document.querySelector('.progress');
    const timeDisplay = document.querySelector('.time');
    const canvas = document.getElementById('waveform');
    const ctx = canvas.getContext('2d');
    
    // Создаем аудиоконтекст и анализируем данные
    const audioContext = new (window.AudioContext || window.webkitAudioContext)();
    const analyser = audioContext.createAnalyser();
    const source = audioContext.createMediaElementSource(audioPlayer);
    getAudioContext().resume();
    
    source.connect(analyser);
    analyser.connect(audioContext.destination);
    
    analyser.fftSize = 256;
    const bufferLength = analyser.frequencyBinCount;
    const dataArray = new Uint8Array(bufferLength);
    
    // Функция для отрисовки волны
    function drawWaveform() {
        requestAnimationFrame(drawWaveform);
        analyser.getByteTimeDomainData(dataArray);
    
        ctx.fillStyle = 'transparent';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
    
        ctx.lineWidth = 2;
        ctx.strokeStyle = 'white';
        ctx.beginPath();
    
        const sliceWidth = canvas.width * 1.0 / bufferLength;
        let x = 0;
    
        for (let i = 0; i < bufferLength; i++) {
            const v = dataArray[i] / 128.0;
            const y = (v * canvas.height / 2);
    
            if (i === 0) {
                ctx.moveTo(x, y);
            } else {
                ctx.lineTo(x, y);
            }
    
            x += sliceWidth;
        }
    
        ctx.lineTo(canvas.width, canvas.height / 2);
        ctx.stroke();
    }
    
    // Запускаем отрисовку волны
    drawWaveform();
    
    // Управление воспроизведением
    playPauseBtn.addEventListener('click', () => {
        if (audioPlayer.paused) {
            audioPlayer.play();
            playPauseBtn.textContent = '⏸️';
        } else {
            audioPlayer.pause();
            playPauseBtn.textContent = '▶️';
        }
    });
    
    audioPlayer.addEventListener('timeupdate', () => {
        const progress = (audioPlayer.currentTime / audioPlayer.duration) * 100;
        progressBar.style.width = `${progress}%`;
    
        const minutes = Math.floor(audioPlayer.currentTime / 60);
        const seconds = Math.floor(audioPlayer.currentTime % 60);
        timeDisplay.textContent = `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
    });
    
    audioPlayer.addEventListener('ended', () => {
        playPauseBtn.textContent = '▶️';
        progressBar.style.width = '0%';
        timeDisplay.textContent = '0:00';
    });
});
