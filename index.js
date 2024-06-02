document.addEventListener('DOMContentLoaded', () => {
    const animateBtn = document.getElementById('animateBtn');
    const animatedBox = document.getElementById('animatedBox');

    animateBtn.addEventListener('click', () => {
        if (animatedBox.style.opacity === '1') {
            animatedBox.style.opacity = '0';
            animatedBox.style.transform = 'scale(0)';
        } else {
            animatedBox.style.opacity = '1';
            animatedBox.style.transform = 'scale(1)';
        }
    });
});