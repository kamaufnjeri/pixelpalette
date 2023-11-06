document.addEventListener("DOMContentLoaded", function () {
    const notificationBoxes = document.querySelectorAll(".notification");
    const closeBtns = document.querySelectorAll(".close");

    // popup for deleting an account
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
        });
        deleteBtn.addEventListener("click", () => {
            popupBox.style.display = "flex";
        });
    }
    const deleteArtwork = document.getElementById('delete-artwork');
    const noBtnArtwork = document.getElementById('no-artwork');
    const yesBtnArtwork = document.getElementById('yes-artwork');
    const deleteBtnArtwork = document.getElementById('delete-artwork-btn');

    if (yesBtnArtwork && noBtnArtwork && deleteBtnArtwork) {
        yesBtnArtwork.addEventListener('click', () => {
            document.getElementById("delete-artwork-form").submit();
        });
        noBtnArtwork.addEventListener("click", () => {
            // This should simply hide the delete confirmation box, not submit the form
            deleteArtwork.style.display = "none";
        });
        deleteBtnArtwork.addEventListener("click", () => {
            deleteArtwork.style.display = "block";
        });
    }
    const deleteExhibit = document.getElementById('delete-exhibit');
    const noBtnExhibit = document.getElementById('no-exhibit');
    const yesBtnExhibit = document.getElementById('yes-exhibit');
    const deleteBtnExhibit = document.getElementById('delete-exhibit-btn');
    console.log(deleteExhibit)

    if (yesBtnExhibit && noBtnExhibit && deleteBtnExhibit) {
        noBtnExhibit.addEventListener("click", () => {
            // This should simply hide the delete confirmation box, not submit the form
            deleteExhibit.style.display = "none";
        });
        deleteBtnExhibit.addEventListener("click", () => {
            deleteExhibit.style.display = "block";
        });
    }
});