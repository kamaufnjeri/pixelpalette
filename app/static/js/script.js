document.addEventListener("DOMContentLoaded", function () {
    const headerNav = document.querySelector('.container-head');
    const barIcon = document.getElementById('menu-bar');
    const navBarIcon = document.getElementById('nav-bar');
    
    
    // deals with revealing the menu bar items
    if (barIcon) {
        barIcon.addEventListener('click', () => {
            headerNav.classList.add('container-visible');
         });

    }
    // deals with hiding the menu bar item
    if (navBarIcon) {
        navBarIcon.addEventListener('click', () => {
            headerNav.classList.remove('container-visible');
         });
    }
});