$('document').ready(() => {
  $('INPUT#btn_translate').click(() => {
    $.get('https://www.fourtonfish.com/hellosalut/?lang=' + $('INPUT#language_code').val(), (data) => {
      $('DIV#hello').text(data.hello);
    });
  });
  $('INPUT#language_code').keypress((event) => {
    if (event.which === 13) {
      $.get('https://www.fourtonfish.com/hellosalut/?lang=' + $('INPUT#language_code').val(), (data) => {
        $('DIV#hello').text(data.hello);
      });
    } else return true;
  });
});
