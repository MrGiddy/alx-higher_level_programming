// toggles the class of the <header> element
// when the user clicks on the tag DIV#toggle_header
$('DIV#toggle_header').on('click', function () {
  if ($('header').hasClass('green')) {
    $('header').removeClass('green');
    $('header').addClass('red');
  } else {
    $('header').removeClass('red');
    $('header').addClass('green');
  }
});
