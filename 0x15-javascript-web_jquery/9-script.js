#!/usr/bin/node

$(document).ready(() => {
  $.ajax({
    url: 'https://stefanbohacek.com/hellosalut/?lang=fr',
    success: (result) => {
      $('DIV#hello').html(result.hello);
    }
  });
});
