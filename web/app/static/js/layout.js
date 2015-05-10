  $(document).ready(function() {
    $('#selection_div').onePageNav({
      currentClass: 'current',
      changeHash: false,
      scrollSpeed: 750
    });

    var top = $('#selection_div').offset().top - parseFloat($('#selection_div').css('margin-top').replace(/auto/, 0));

    $(window).scroll(function (event) {
      // what the y position of the scroll is
      var y = $(this).scrollTop();

      // whether that's below the form
      if (y >= top) {
        // if so, ad the fixed class
        $('#selection_div').addClass('fixed');
        $('#get_selected').hide();
      } else {
        // otherwise remove it
        $('#selection_div').removeClass('fixed');
        toggleScroller();
      }
    });
  });
