window.onload = function() {

    const roundedInput = document.getElementById('rounded-input');
    const saveButton = document.getElementById("save-button");
    const titleInput = document.getElementById("title-input");

    /*
    Event listener for the "Add feed" input field.
    "Enter" key adds the feed to the database.
    If the feed already exists, display a popup.
     */
    roundedInput.addEventListener('keypress', async function(event) {
        if (event.key === 'Enter') {
            event.preventDefault();
            event.stopPropagation();
            const response = await fetch('/save_feed', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                body: 'value=' + encodeURIComponent(roundedInput.value)
            });
            if (response.ok) {
                location.reload();
            } else {
                document.getElementById("feed-exists-popup").style.display = "block";
            }
        }
    });

    // Event listener for the "Try another feed" button in the "Feed already exists" popup
    document.getElementById("try-another-feed-button").addEventListener('click', function() {
        document.getElementById("feed-exists-popup").style.display = "none";
    });

    const popup = document.getElementById("popup-edit-title");
    const editButtons = document.getElementsByClassName("edit-button");

    // When the user clicks an "Edit" button, open the popup and set the title
    for (let i = 0; i < editButtons.length; i++) {
        editButtons[i].onclick = function() {
            let form = this.parentElement.previousElementSibling;
            let feedTitle = form.querySelector('input[name="feed_title"]').value;
            popup.setAttribute('title', feedTitle);
            popup.style.display = "block";
        }
    }

    /*
    Event listener for the "Save" button in the "Edit title" popup.
    Send the new title to the server and reload the page.
     */
    saveButton.addEventListener('click', async function(event) {
        event.preventDefault();
        let newTitle = titleInput.value;
        let originalTitle = popup.getAttribute('title');

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

    // Event listener for opening a feed
    document.querySelectorAll('.open-feed-button').forEach(button => {
        button.addEventListener('click', function(event) {
            const form = document.getElementById('feed-form');
            form.action = '/view_feed';
        });
    });

    const span = document.getElementsByClassName("close")[0];

    // Close the popup when the user clicks the "x" button
    span.onclick = function() {
        popup.style.display = "none";
    }

    // Close the popup when the user clicks anywhere outside the popup
    window.onclick = function(event) {
        if (event.target === popup) {
            popup.style.display = "none";
        }
    }

    // Filter categories
    $('#category-select').change(function() {
        const selectedCategory = $(this).val();


        $.ajax({
            url: '/filter_by_category',
            method: 'POST',
            data: { 'category': selectedCategory },
            success: function(response) {
                // Replace the articles with the filtered articles from the server
                $('#articles').html(response);
            }
        });
    });
}
