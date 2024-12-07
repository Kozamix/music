document.addEventListener('DOMContentLoaded', function() {
    const audioPlayer = document.getElementById('audio-player');
    const playbackRateSelect = document.getElementById('playbackRate');

    playbackRateSelect.addEventListener('change', function() {
        audioPlayer.playbackRate = parseFloat(this.value);
    });
});
