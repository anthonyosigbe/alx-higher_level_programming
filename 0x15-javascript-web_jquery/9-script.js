// Ensure that the code executes only after the document has been completely loaded.

$(document).ready(function () {
  // Utilize jQuery's ajax method to retrieve the data from the URL.
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: function (response) {
      // Modify the text of `DIV#hello` with the "hello" value from the fetched data.
      $('#hello').text(response.hello);
    }
  });
});
