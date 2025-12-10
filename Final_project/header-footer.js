const cows = document.querySelectorAll('.footer-left img');

cows.forEach(cow => {
    cow.addEventListener('click', () => {
        const soundFile = cow.dataset.sound;
        const audio = new Audio(soundFile);
        audio.play();
    });
});
