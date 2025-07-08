document.addEventListener('DOMContentLoaded', function() {
    const playButton = document.getElementById('play');
    const pauseButton = document.getElementById('pause');
    const audioElement = document.getElementById('audio');

    playButton.addEventListener('click', function() {
        audioElement.play();
    });

    pauseButton.addEventListener('click', function() {
        audioElement.pause();
    });

    audioElement.addEventListener('ended', function() {
        // Optionally, handle what happens when the audio ends
        console.log('Audio playback has ended.');
    });
});