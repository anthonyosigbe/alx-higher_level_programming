// Make sure the script runs after the document has been fully loaded.

$(document).ready(function () {
  // Add a click event listener to `INPUT#btn_translate`.
  $('#btn_translate').click(function () {
    // Retrieve the language code entered by the user.
    const langCode = $('#language_code').val();
    // Build the URL for the API request.
    const requestURL = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + langCode;

    // Initiate the AJAX request to the API.
    $.get(requestURL, function (data) {
      // Show the translation of "Hello" in `DIV#hello`.
      $('#hello').text(data.hello);
    });
  });
});
