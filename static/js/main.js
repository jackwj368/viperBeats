document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.pack-card').forEach(card => {
    const btn = card.querySelector('.play-btn');
    const audio = new Audio(card.dataset.audio);
    let playing = false;

    btn.addEventListener('click', () => {
      if (!playing) {
        audio.play();
        btn.textContent = '⏸';
      } else {
        audio.pause();
        audio.currentTime = 0;
        btn.textContent = '▶️';
      }
      playing = !playing;
    });

    audio.addEventListener('ended', () => {
      btn.textContent = '▶️';
      playing = false;
    });
  });
});