const headerNav = document.querySelector('.container-head');
const barIcon = document.getElementById('menu-bar');

barIcon.addEventListener('click', () => {
   headerNav.classList.toggle('container-visible');
   barIcon.classList.toggle('move-bar-icon');
});

async function users() {
   try {
       const resp = await fetch('/api/users');
       if (!resp.ok) {
           throw new Error(`Network response was not ok: ${resp.status}`);
       }
       let data = await resp.json();
       console.log(data);
   } catch (error) {
       console.error("Error:", error);
   }
}

users();