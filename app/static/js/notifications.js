/*
Document event listener for DOMContentLoaded
*/
document.addEventListener("DOMContentLoaded", function () {
    // Get all notification boxes and close buttons
    const notificationBoxes = document.querySelectorAll(".notification");
    const closeBtns = document.querySelectorAll(".close");

    // Get elements for account deletion confirmation popup
    const popupBox = document.getElementById('delete-popup');
    const noBtn = document.getElementById('no-btn');
    const yesBtn = document.getElementById('yes-btn');
    const deleteBtn = document.getElementById('delete-user');

    // Add event listeners to close buttons
    closeBtns.forEach((closeBtn, index) => {
        closeBtn.addEventListener('click', () => {
            notificationBoxes[index].style.display = "none";
        });
    });

    // Check if elements for account deletion popup exist
    if (yesBtn && noBtn && deleteBtn) {
        // Event listeners for account deletion confirmation
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

    // Get elements for artwork deletion confirmation popup
    const deleteArtwork = document.getElementById('delete-artwork');
    const noBtnArtwork = document.getElementById('no-artwork');
    const yesBtnArtwork = document.getElementById('yes-artwork');
    const deleteBtnArtwork = document.getElementById('delete-artwork-btn');

    // Check if elements for artwork deletion popup exist
    if (yesBtnArtwork && noBtnArtwork && deleteBtnArtwork) {
        // Event listeners for artwork deletion confirmation
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

    // Get elements for exhibit deletion confirmation popup
    const deleteExhibit = document.getElementById('delete-exhibit');
    const noBtnExhibit = document.getElementById('no-exhibit');
    const yesBtnExhibit = document.getElementById('yes-exhibit');
    const deleteBtnExhibit = document.getElementById('delete-exhibit-btn');

    // Check if elements for exhibit deletion popup exist
    if (yesBtnExhibit && noBtnExhibit && deleteBtnExhibit) {
        // Event listeners for exhibit deletion confirmation
        noBtnExhibit.addEventListener("click", () => {
            // This should simply hide the delete confirmation box, not submit the form
            deleteExhibit.style.display = "none";
        });
        deleteBtnExhibit.addEventListener("click", () => {
            deleteExhibit.style.display = "block";
        });
    }
});
