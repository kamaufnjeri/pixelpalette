const notificationBoxes = document.querySelectorAll(".notification");
const closeBtns = document.querySelectorAll(".close");
const popupBox = document.getElementById('delete-popup');
const noBtn = document.getElementById('no-btn');
const yesBtn = document.getElementById('yes-btn');
const deleteBtn = document.getElementById('delete-user');

closeBtns.forEach((closeBtn, index) => {
    closeBtn.addEventListener('click', () => {
        notificationBoxes[index].style.display = "none";
    });
});
if (yesBtn && noBtn && deleteBtn) {
    yesBtn.addEventListener('click', () => {
        document.getElementById("delete-user-form").submit();
    });
    noBtn.addEventListener("click", () => {
        popupBox.style.display = "none";
    }
    );
    deleteBtn.addEventListener("click", () => {
        popupBox.style.display = "flex";
    }
    );
}
