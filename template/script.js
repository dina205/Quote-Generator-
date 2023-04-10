/* script.js */

// This code runs when the user submits the form
document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault(); // prevent the default form submission

    // Get the file input element and the selected file
    const fileInput = document.querySelector('input[type="file"]');
    const file = fileInput.files[0];

    // Display the file name in the console
    console.log(`Selected file: ${file.name}`);
});
