  $(document).ready(function() {
    // $('#selection_div').onePageNav({
    //   currentClass: 'current',
    //   changeHash: false,
    //   scrollSpeed: 750
    // });

    

    $(window).scroll(function (event) {
      // what the y position of the scroll is
      //var top = $('#selection_div').offset().top - parseFloat($('#selection_div').css('margin-top').replace(/auto/, 0));
      var top = $(window).height() - $('#selection_div').height();
      var y = $(this).scrollTop();

      // whether that's below the form
      if (y >= top) {
        // if so, ad the fixed class
        var height = $('#selection_div').height();
        $('#selection_div').addClass('fixed');
        $('#selection_div').height(height)
        $('#get_selected').hide();
      } else {
        // otherwise remove it
        $('#selection_div').removeClass('fixed');
      }
    });
  });
