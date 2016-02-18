$(function () {
  $('#linkTree h2').click(function() {
      $(this).next('ol').slideToggle('fast');
      $(this).toggleClass('selected');
  });
});
