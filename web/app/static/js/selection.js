//Called when dropdown option is selected
//id - the id of the dropdown that was selected
//attribute - the option that was selected
function report(elt) {
  $elt = $(elt);
  $elt.addClass('demo_activated');
  $elt.children()[0].remove();

  if ($('.demo_activated').length === 3) {
    getSelected();
  }
}

function getSelected(){
  $('html,body').animate({
    scrollTop: $('.wrapper').offset().top - 120
  }, 'slow');

  var selected = {};
  selected['age'] = $('#age').val();
  if (!selected['age']) return;
  selected['race'] = $('#race').val();
  if (!selected['race']) return;
  selected['sex'] = $('#sex').val();
  if (!selected['sex']) return;
  selected['time'] = getCurrentlySelectedDate();



  updateHeatmap(selected);
  updateTimeline(selected);
  updateStops(selected);
}


function updateHeatmap(selected) {
  $('#likelihood').hide();
  $('.loader').show();
  $.ajax({
    url : '/update_heatmap',
    type : 'POST',
    data : selected,
    success : function(response) {
      repaint(response.results);
      var avg = response.avg_prob;
      $('#likelihood').addClass(quantize(avg)).text(avg.toFixed(2));
      $('#likelihood').show();
      $('.loader').hide();

    },
    failure : function(response) {
      console.log(response);
    }
  });
}

function updateTimeline(selected) {
  $.ajax({
    url : '/update_timeline',
    type : 'POST',
    data : selected,
    success : function(response) {
      analyze(response.time_series);
    },
    failure : function(response) {
      console.log(response);
    }
  });
}

function updateStops(selected) {
  clearStops();
  $.ajax({
    url : '/update_stops',
    type : 'POST',
    data : selected,
    success : function(response) {
      paintStops(response.matches);
    },
    failure : function(response) {
      console.log(response);
    }
  });

}
