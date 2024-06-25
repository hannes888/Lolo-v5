window.onload = function() {

    const roundedInput = document.getElementById('rounded-input');
    const feedTitles = document.getElementById('feed-titles');
    const saveButton = document.getElementById("save-button");
    const titleInput = document.getElementById("title-input");

    roundedInput.addEventListener('keypress', async function(event) {
        if (event.key === 'Enter') {
            event.preventDefault();
            event.stopPropagation();
            const response = await fetch('/save_value', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                body: 'value=' + encodeURIComponent(roundedInput.value)
            });
            if (response.ok) {
                location.reload();
            }
        }
    });

    // Get the popup
    const popup = document.getElementById("popup-edit-title");

    // Get all the "Edit" buttons
    const editButtons = document.getElementsByClassName("edit-button");

    // When the user clicks an "Edit" button, open the popup and set the title
    for (let i = 0; i < editButtons.length; i++) {
        editButtons[i].onclick = function() {
            // Get the associated form
            let form = this.parentElement.previousElementSibling;

            // Get the title of the feed from the hidden input field
            let feedTitle = form.querySelector('input[name="feed_title"]').value;

            // Set the title of the popup to the title of the feed
            popup.setAttribute('title', feedTitle);

            // Display the popup
            popup.style.display = "block";
        }
    }

    saveButton.addEventListener('click', async function(event) {
        event.preventDefault();
        // Get the new title from the input field
        let newTitle = titleInput.value;

        // Get the original title from the popup
        let originalTitle = popup.getAttribute('title');

        // Send the data to the server
        const response = await fetch('/change_feed_title', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                original_title: originalTitle,
                new_title: newTitle
            })
        });
        if (response.ok) {
            location.reload();
        } else {
            console.error('Failed to update title');
        }
    });

    document.getElementById('feed-button').addEventListener('click', function(event) {
        const form = document.getElementById('feed-form');
        form.action = '/view_feed';
    });

    // Get the close button
    const span = document.getElementsByClassName("close")[0];

    // When the user clicks on <span> (x), close the popup
    span.onclick = function() {
        popup.style.display = "none";
    }

    // When the user clicks anywhere outside the popup, close it
    window.onclick = function(event) {
        if (event.target === popup) {
            popup.style.display = "none";
        }
    }
}
