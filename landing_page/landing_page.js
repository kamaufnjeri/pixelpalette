document.addEventListener("DOMContentLoaded", function () {
    const typeCont = document.getElementById("type-cont");
    const writer = document.getElementById("writer");
    const typeText = "Discover, Collect, Create: Art in the Digital Realm";
    let index = 0;
    let isErasing = false;  // Flag to indicate if we are erasing


    //write the text
    function writeText () {
        if (isErasing) {
            // check if erasing
            eraseWords();
            return;
        }
        else if (index <= typeText.length) {
            // write
            writer.classList.remove('blinker');
            let text = typeText.substring(0, index);
            typeCont.innerHTML = text;
            index++;
        }
        else {
            // start erasing after 3 seconds
            writer.classList.add('blinker');
            setTimeout(function () {
                isErasing = true;
            }, 3000);
        }
    }

    /// erase the words
    function eraseWords() {
        if (index >= 0) {
            // erasing the words
            writer.classList.remove('blinker');
            let text = typeText.substring(0, index);
            typeCont.innerHTML = text;
            index--;
        } else {
            // after erasing wait 3 seconds before starting to write
            writer.classList.add('blinker');
            setTimeout(function () {   
                isErasing = false;
            }, 3000);
        }
    }
    setInterval(writeText, 200);
});
