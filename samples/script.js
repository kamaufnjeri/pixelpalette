const imageInput = document.getElementById('image-input');
const imagePreview = document.getElementById('image-preview');
const imageName = document.getElementById('image-name');

imageInput.addEventListener('change', function (e) {
    const file = e.target.files[0];

    if (file) {
        const reader = new FileReader();

        reader.onload = function (event) {
            imagePreview.src = event.target.result;
        };

        reader.readAsDataURL(file);

        imageName.textContent = `Selected Image: ${file.name}`;
    } else {
        imagePreview.src = '';
        imageName.textContent = '';
    }
});
