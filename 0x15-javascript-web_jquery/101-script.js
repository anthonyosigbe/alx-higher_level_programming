// Makes sure that the script executes after the document is fully loaded.

$(document).ready(function () {
  // When `DIV#add_item` is clicked, append a new `<li>Item</li>` to `UL.my_list`.
  $('#add_item').click(function () C{
    $('.my_list').append('<li>Item</li>');
  });

  // When `DIV#remove_item` is clicked, remove the last `<li>` element from `UL.my_list`.
  $('#remove_item').click(function () {
    $('.my_list li:last').remove();
  });

  // When `DIV#clear_list` is clicked, remove all `<li>` elements from `UL.my_list`.
  $('#clear_list').click(function () {
    $('.my_list').empty();
  });
});
