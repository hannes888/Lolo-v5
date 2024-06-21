window.onload = function() {
    const input = document.getElementById('rounded-input');
    const feedTitles = document.getElementById('feed-titles');
    input.addEventListener('keypress', async function(event) {
        if (event.key === 'Enter') {
            event.preventDefault();
            const response = await fetch('/save_value', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                body: 'value=' + encodeURIComponent(input.value)
            });
            if (response.ok) {
                location.reload();
            }
        }
    });

    document.getElementById('feed-button').addEventListener('click', function(event) {
    const form = document.getElementById('feed-form');
    form.action = '/view_feed';
    });

    // Get the popup
    const popup = document.getElementById("popup-edit-title");

    // Get all the "Edit" buttons
    const editButtons = document.getElementsByClassName("edit-button");

    // Get the close button
    const span = document.getElementsByClassName("close")[0];

    // When the user clicks an "Edit" button, open the popup
    for (let i = 0; i < editButtons.length; i++) {
        editButtons[i].onclick = function() {
            popup.style.display = "block";
        }
    }

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


    function saveTitle() {
        // Get the input field
        var inputField = document.getElementById("title-input");

        // Get the value of the input field
        var title = inputField.value;

        // Log the title to the console
        console.log("New title: " + title);

        // Close the popup
        document.getElementById("popup-edit-title").style.display = "none";
    }
}




