// Function for fetching and displaying the translation.

$(document).ready(function () {
  function fetchAndDisplayHello () {
    const langCode = $('#language_code').val();
    const requestURL = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + langCode;

    $.get(requestURL, function (data) {
      $('#hello').text(data.hello);
    });
  }

  // Event listener for the translate button
  $('#btn_translate').click(fetchAndDisplayHello);

  // Event listener for the enter key press in the language code input
  $('#language_code').keypress(function (event) {
    // Check if the key pressed is the Enter key
    if (event.which === 13) {
      fetchAndDisplayHello();
    }
  });
});
