/*
Document event listener for DOMContentLoaded
*/
document.addEventListener("DOMContentLoaded", function () {
    // variables for artwork display
    const artworksContainer = document.getElementById('artworks-container');
    const singleArtwork = document.getElementById('single-artwork');
    const artistsContainer = document.getElementById('artists-container');
    const artistArtworks = document.getElementById('artist-artworks');

    /*
    Function to append an element to parent
    */
    function appendChild(childTag, messageOrUrl, parentTag) {
        const tag = document.createElement(childTag);
        if (childTag === 'img') {
            tag.src = messageOrUrl;
        } else {
            tag.innerHTML = messageOrUrl;
        }
        parentTag.appendChild(tag);
    }

    /*
    Function to make API calls
    */
    async function api(endpoint) {
        try {
            const apiUrl = `/api/${endpoint}`;
            const resp = await fetch(apiUrl);
            if (!resp.ok) {
                throw new Error(`Network response was not ok: ${resp.status}`);
            }
            let data = await resp.json();
            return data;
        } catch (error) {
            throw error;
        }
    }

    // Display all artworks on page load
    if (artworksContainer) {
        const selectionOption = document.getElementById("category-artworks");
        const showSelection = document.getElementById("show-selection");

        /*
        Display all artworks function
        */
        async function displayAllArtworks() {
            try {
                const artworks = await api('artworks');
                artworks.Artworks.forEach(artwork => {
                    appendArtwork(artwork);
                });
            } catch (error) {
                console.error(error);
            }
        }

        // Display artworks based on user selection
        if (showSelection) {
            showSelection.addEventListener('click', async () => {
                try {
                    const data = await api('artworks');
                    artworksContainer.innerHTML = '';
                    data.Artworks.forEach(artwork => {
                        if (selectionOption.value === "all" || artwork.category === selectionOption.value) {
                            appendArtwork(artwork);
                        }
                    });
                } catch (error) {
                    console.error(error);
                }
            });
        }

        // Display all artworks on page load
        window.addEventListener('load', () => {
            displayAllArtworks();
        });

        /*
        Append artwork details to the container
        */
        function appendArtwork(artwork) {
            const singleArtworkContainer = document.createElement('div');
            singleArtworkContainer.classList.add('artwork');
            appendChild('img', artwork.url, singleArtworkContainer);
            appendChild('h4', "Name: " + artwork.title, singleArtworkContainer);
            appendChild('h5', 'Owner: ' + artwork.owner, singleArtworkContainer);
            appendChild('h6', 'Price: Kshs. ' + artwork.price, singleArtworkContainer);
            appendChild('a', 'View Artwork', singleArtworkContainer);
            singleArtworkContainer.querySelector('a').href = `${artwork.owner}/artworks/${artwork.id}`;
            singleArtworkContainer.querySelector('a').classList.add('btn-log');
            artworksContainer.appendChild(singleArtworkContainer);
        }
    }

    // Display single artwork details
    if (singleArtwork) {
        (async () => {
            try {
                const url = window.location.href.split('/');
                const id = url[url.length - 1];
                const username = url[url.length - 3];
                const artwork = await api(`${username}/artworks/${id}`);
                appendChild('img', artwork.url, singleArtwork);
                const artworkDetails = document.createElement('div');
                appendChild('h2', 'Name: ' + artwork.title, artworkDetails);
                appendChild('h3', 'Owner: ' + artwork.owner, artworkDetails);
                appendChild('h4', 'Category: ' + artwork.category, artworkDetails);
                appendChild('h5', 'Description: ' + artwork.description, artworkDetails);
                appendChild('h6', 'Price: Kshs. ' + artwork.price, artworkDetails);

                const showContact = document.createElement('p');
                const contact = document.createElement('span');
                const form = document.createElement('form');
                const quantity = document.createElement('input');
                const quantityLabel = document.createElement('label');
                const addToCart = document.createElement('button');
                quantity.type = "number";
                quantity.name = "quantity";
                quantity.max = 100;
                quantity.min = 1;
                addToCart.innerHTML = "Add to favorites Cart";
                quantityLabel.innerHTML = "Quantity";
                showContact.innerHTML = "To purchase artwork contact owner";
                contact.innerHTML = "Show contact";
                quantity.classList.add("quantity");
                addToCart.id = "add-to-cart";
                addToCart.classList.add("btn-log");
                quantityLabel.classList.add("quantity-label");
                form.method = "POST";
                artworkDetails.appendChild(showContact);
                artworkDetails.appendChild(contact);
                form.appendChild(quantityLabel);
                form.appendChild(quantity);
                form.appendChild(addToCart);
                artworkDetails.appendChild(form);
                singleArtwork.appendChild(artworkDetails);

                // Show contact information on click
                contact.addEventListener('click', () => {
                    contact.innerHTML = 'Email_address: ' + artwork.contact;
                });

                // Submit the form on button click
                addToCart.addEventListener("click", () => {
                    form.submit();
                });

            } catch (error) {
                console.error(error);
            }
        })();
    }

    // Display artists on the page
    if (artistsContainer) {
        (async () => {
            try {
                const artists = await api('artists');
                artists.Users.forEach(artist => {
                    const contArtist = document.createElement('div'); // Create a new div for each artist
                    contArtist.classList.add('cont-artist');
                    appendChild('h4', "Artist Name: " + artist.first_name + " " + artist.last_name, contArtist);
                    const viewMoreLink = document.createElement('a');
                    viewMoreLink.textContent = 'View More';
                    viewMoreLink.classList.add('btn-log');
                    viewMoreLink.href = `/${artist.username}/artworks`;
                    contArtist.appendChild(viewMoreLink);
                    artistsContainer.appendChild(contArtist); // Append the new div to the container
                });
            } catch (error) {
                console.error(error);
            }
        })();
    }

    // Display artworks for a specific artist
    if (artistArtworks) {
        (async () => {
            try {
                const username = artistArtworks.getAttribute('data-username');
                const ownerArtworks = await api(`${username}/artworks`);
                ownerArtworks.owner_artworks.forEach(artwork => {
                    const singleArtworkContainer = document.createElement('div');
                    singleArtworkContainer.classList.add('artwork');
                    appendChild('img', artwork.url, singleArtworkContainer);
                    appendChild('h4', "Name: " + artwork.name, singleArtworkContainer);
                    appendChild('h5', 'Category: ' + artwork.category, singleArtworkContainer);
                    appendChild('h6', 'Price: Kshs. ' + artwork.price, singleArtworkContainer);
                    appendChild('a', 'View Artwork', singleArtworkContainer);
                    singleArtworkContainer.querySelector('a').href = `artworks/${artwork.id}`;
                    singleArtworkContainer.querySelector('a').classList.add('btn-log');
                    artistArtworks.appendChild(singleArtworkContainer);
                });
            } catch (error) {
                console.error(error);
            }
        })();
    }
});
