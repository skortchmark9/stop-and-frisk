function selection_init(){
  //populate dropdown
	createAge();
  $('#likelihood').click(function() {
    getSelected();
  });
}

//Populates the age dropdown
function createAge(){
  var age = document.getElementById("age");
  for(i=10; i<=100; i++){
    var as = document.createElement("option");
    as.setAttribute("value", i);
    as.appendChild(document.createTextNode(i));
    age.appendChild(as);
  }
}


//Populates the height dropdown
function createHeight(){
  var height = document.getElementById("height");
  for(i=30;i<=120;i++){
    var as = document.createElement("option");
    var h = Math.floor(i/12)+"\' "+i%12+"\"";
    as.setAttribute("value", h);
    as.appendChild(document.createTextNode(h));
    height.appendChild(as);
  }
}

//Populates the weight dropdown
function createWeight(){
  var weight = document.getElementById("weight");
  for(i=1;i<=500;i++){
    var as = document.createElement("option");
    var w = i;
    as.setAttribute("value", w+" lbs");
    as.appendChild(document.createTextNode(w));
    weight.appendChild(as);
  }
}

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
    scrollTop: $('#heatmap_div').offset().top
  }, 'slow');

  var selected = {};
  selected['age'] = $('#age').val();
  selected['race'] = $('#race').val();
  selected['sex'] = $('#sex').val();
  selected['time'] = getCurrentlySelectedDate();

  updateHeatmap(selected);
  updateTimeline(selected);
  updateStops(selected);
}


function updateHeatmap(selected) {
  $.ajax({
    url : '/update_heatmap',
    type : 'POST',
    data : selected,
    success : function(response) {
      repaint(response.results);
      var avg = response.avg_prob;
      $('#likelihood').text(avg.toFixed(2));
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
