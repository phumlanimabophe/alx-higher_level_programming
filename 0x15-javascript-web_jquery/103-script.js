$(document).ready(function () {
  $('#btn_translate').click(translate);

  $('#language_code').on('keydown', function (e) {
    if (e.keyCode === 13) {
      translate();
    }
  });
});

function translate() {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  const languageCode = $('#language_code').val();
  
  $.get(url, { lang: languageCode }, function (data) {
    $('#hello').html(data.hello);
  });
}
