jQuery(function($) {
  $('tr[data-href]').addClass('clickable')
  .click(function(e) {
    if(!$(e.target).is('a')){
        window.open($(e.target).closest('tr').data('href'));
    };
  });
});
