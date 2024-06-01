// Adds, removes and clears LI elements from a list

$(document).ready(function () {
  // Add new element to the list when user clicks DIV#add_item
  $('DIV#add_item').on('click', function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  // Remove the last element when user clicks DIV#remove_item
  $('DIV#remove_item').on('click', function () {
    $('UL.my_list li:last-child').remove();
  });
  // Remove all elements of the list when user clicks DIV#clear_list
  $('DIV#clear_list').on('click', function () {
    $('UL.my_list').empty();
  });
});
