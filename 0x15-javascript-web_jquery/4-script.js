// Utilize jQuery to manage the click event on `DIV#toggle_header`.
$('#toggle_header').click(function() {
	// Check if the <header> has the class 'red',
	// if so, toggle to 'green', else toggle to 'red'
  if ($('header').hasClass('red')) {
    $('header').removeClass('red').addClass('green');
  } else {
    $('header').removeClass('green').addClass('red');
  }
});
