// script.js

document.addEventListener('DOMContentLoaded', function () {
    const mainTitle = document.getElementById('main-title');
    const changeTitleBtn = document.getElementById('change-title-btn');

    changeTitleBtn.addEventListener('click', function () {
        const newTitle = prompt('Enter the new title:');
        mainTitle.textContent = newTitle || mainTitle.textContent;
    });
});
