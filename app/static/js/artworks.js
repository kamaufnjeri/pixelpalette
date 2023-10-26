document.addEventListener("DOMContentLoaded", function () {
    // variables for artwork display
    const artworksContainer = document.getElementById('artworks-container');
    const singleArtwork = document.getElementById('single-artwork');
    const artistsContainer = document.getElementById('artists-container');
    const artistArtworks = document.getElementById('artist-artworks');

    function appendChild(childTag, messageOrUrl, parentTag) {
        const tag = document.createElement(childTag);
        if (childTag === 'img') {
            tag.src = messageOrUrl;
        } 
        else {
            tag.innerHTML = messageOrUrl;
        }
        parentTag.appendChild(tag);
    }

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

    if (artworksContainer) {
        const selectionOption = document.getElementById("category-artworks");
        const showSelection = document.getElementById("show-selection");
        
        // display the artworks
        async function displayAllArtworks () {
            try {
                const artworks = await api('artworks');
                artworks.Artworks.forEach(artwork => {
                    appendArtwork(artwork);
                }); 
            } catch (error) {
                console.error(error);
            }
        }
        // display artworks on reload browser
        
        // display artwork by user selection
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
        
        window.addEventListener('load', () => {
            displayAllArtworks();
        });
        // appending thhe artworks created
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
        
        // appending an element to parent element
        
    }

    if (singleArtwork) {
        (async () => {
            try {
                const url = window.location.href.split('/');
                const id = url[url.length - 1];
                const username = url[url.length -3];
                const artwork = await api(`${username}/artworks/${id}`);
                appendChild('img', artwork.url, singleArtwork);
                const artworkDetails = document.createElement('div');
                appendChild('h2', 'Name: ' + artwork.title, artworkDetails);
                appendChild('h3', 'Owner: ' + artwork.owner, artworkDetails);
                appendChild('h4', 'Category: ' + artwork.category, artworkDetails);
                appendChild('h5', 'Description: ' + artwork.description, artworkDetails);
                appendChild('h6', 'Price: Kshs. ' + artwork.price, artworkDetails);
                singleArtwork.appendChild(artworkDetails);
            } catch (error) {
                console.error(error);
            }
        })();
    }
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
