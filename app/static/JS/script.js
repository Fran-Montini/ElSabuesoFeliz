document.addEventListener('DOMContentLoaded', function () {
    const cards = document.querySelectorAll('.card');

    cards.forEach(card => {
        card.addEventListener('click', function () {
            alert('Haz clic en ' + card.querySelector('.card-text').innerText);
            // Agrega otras acciones según tus necesidades
        });
    });
});