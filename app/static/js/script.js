document.addEventListener("DOMContentLoaded", function () {
    const headerNav = document.querySelector('.container-head');
    const barIcon = document.getElementById('menu-bar');
    
    
    // deals with revealing and hiding the header items
    if (barIcon) {
        barIcon.addEventListener('click', () => {
            headerNav.classList.toggle('container-visible');
            barIcon.classList.toggle('move-bar-icon');
         });

    }
});