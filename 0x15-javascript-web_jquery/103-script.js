//  fetches and prints how to say “Hello” depending on the language

$(document).ready(function () {
  // Call translate function when 'Enter' is pressed
  $('INPUT#language_code').on('keydown', function (evnt) {
    if (evnt.key === 'Enter') {
      translate();
    }
  });

  // Call translate funcion when 'Translate' button is clicked
  $('INPUT#btn_translate').on('click', translate);

  function translate () {
    // Get the language code typed in the text input field
    const code = $('INPUT#language_code').val();
    // Send a get request to api with the language code as query parameter
    $.ajax({
      url: 'https://hellosalut.stefanbohacek.dev/',
      type: 'GET',
      data: {
        lang: code
      },
      success: function (response) {
        // Insert the translation text inside a target div
        $('DIV#hello').html(response.hello).text();
      },
      error: function (xhr, status, error) {
        console.error(error);
      }
    });
  }
});
