//*******************************************
// BMI Formula Script
// Copyright 2017 Alastair Hazell All Rights Reserved
// This script may not be copied, edited or reproduced
// without express written permission from
// Alastair Hazell
//*******************************************

function getinput(eid) {
	return document.getElementById(eid);
};

function calculate() {

  var w = parseFloat(getinput('weight').value);
  var h= parseFloat(getinput('height').value);
  var e = document.getElementById("units");
  var units = e.options[e.selectedIndex].value;
  
  if (isNaN(w) || isNaN(h)) {
   alert('Please note that numbers much be entered for both input boxes');
   return;
  }
  
  if (units == 'imperial') {
  
  	 var BMI = (w / (h*h)) * 703;
  	 var BMI = BMI.toFixed(2); 
  
  } else {
  
	  // Convert cm to m
	  h = h/100;
  
	  var BMI = w / (h*h);
  	  var BMI = BMI.toFixed(2); 
    
  }
	  // Now show all the form elements in the formula image
	  getinput('formula_weight').innerHTML = w;
	  getinput('formula_height').innerHTML = "("+h+" &times; "+h+")";
			
	  getinput('formula_result').innerHTML = BMI;

};


function changeUnit() {

	var e = document.getElementById("units");
  	var units = e.options[e.selectedIndex].value;
  	
  	 if (units == 'imperial') {
  	 	getinput('formula_title').innerHTML = "Imperial BMI Formula";
  	 	getinput('weight_unit').innerHTML = "lb";
  	 	getinput('height_unit').innerHTML = "in";
  	 	getinput('formula_result').innerHTML = "A";
  	 	getinput('formula_weight').innerHTML = "weight <span class='bmi_measure'>(lb)</span>";
  	 	getinput('formula_height').innerHTML = "height<sup>2</sup> <span class='bmi_measure'>(in<sup>2</sup>)</span>";
  	 	document.getElementById("formula_703").style.display = "block";
  	 } else {
  	 	getinput('formula_title').innerHTML = "Metric BMI Formula";
  	 	getinput('weight_unit').innerHTML = "kg";
  	 	getinput('height_unit').innerHTML = "cm";
  	 	getinput('formula_result').innerHTML = "A";
  	 	getinput('formula_weight').innerHTML = "weight <span class='bmi_measure'>(kg)</span>";
  	 	getinput('formula_height').innerHTML = "height<sup>2</sup> <span class='bmi_measure'>(m<sup>2</sup>)</span>";
  	 	document.getElementById("formula_703").style.display = "none";
  	 }

}