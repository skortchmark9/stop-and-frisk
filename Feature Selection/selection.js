function init(){
	createAge();
  createHeight();
  createWeight();
}

function createAge(){
  var age = document.getElementById("age");
  for(i=1;i<=100;i++){
    var as = document.createElement("option");
    as.setAttribute("value", i+" years old");
    as.appendChild(document.createTextNode(i));
    age.appendChild(as);
  }
}

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

function report(id, attribute) {
  if (attribute=="") return; 

  var holder = document.createElement("span");
  holder.setAttribute("class", "selection button_style");
  holder.setAttribute("name", id);
  holder.setAttribute("id", id+"holder");

  var cancel = document.createElement("button");
  cancel.setAttribute("class", "cancel");
  cancel.setAttribute("type", "button");
  var x = document.createTextNode("x");
  cancel.appendChild(x);
  cancel.setAttribute("name", id);
  cancel.onclick=function(){removeAttribute(this.name)};

  var attributetext = document.createTextNode(attribute);
  
  var list = document.getElementById("list");

  var dropdown = document.getElementById(id);

  holder.appendChild(attributetext);
  holder.appendChild(cancel);

  dropdown.style.left = parseFloat(getComputedStyle(dropdown).left) + 42 + 'px';

  list.appendChild(holder);

  dropdown.style.display='none';
} 

function removeAttribute(name){
	var dropdown = document.getElementById(name);
  	dropdown.style.display='inline';
  	dropdown.selectedIndex = 0;

  	document.getElementById(name+"holder").remove();
}

function getSelected(){
	var list = document.getElementById("list");
	var selected = "Selected Options:\n";
	for(i=1;i<list.childNodes.length;i++){
		var at = list.childNodes[i];
		selected += at.getAttribute("name") + ": " + at.childNodes[0].textContent + "\n";
		console.log(list.childNodes[i]);
	}
	alert(selected);
}