/*====================================================
    APPOINTMENTS
====================================================*/


/*
$.ajax({
	url: "https://randomuser.me/api/",
	dataType: "json",
	success: function (data) {
	  var info = data.results[0];
	  var fullName = info.name.first + " " + info.name.last;
	  var pictureDoctors = info.picture.large;
	  var sendInfo = document.getElementById("dataprueba");
	  fullData =  `<div class="row"><div class="col s12 m4 l2"><img id = "DoctorsPicture" src='${pictureDoctors}'><div class="row">'${fullName}'</div></div></div>'${data.info.seed+":29ec71db3956d488"}' `;
	  console.log(time().date);
	},
  });

  function time(date) {
	var timer = time();
	print(timer)
	  
  }*/
  /*====================================================
    LIST DROPDOWN
====================================================*/
$('.dropdown-trigger').dropdown();

/*====================================================
    ADD FIELLDS MEDICATION AND INDICATION
====================================================*/

function addfield() {
	var postfieldMed = document.getElementById("newfieldMed");
	var postfieldInd = document.getElementById("newfieldInd");
	var fieldsMess = document.getElementById("fieldsMessages");
	var newAssigMed = document.createElement('input');
	var newInd = document.createElement('input');
	newAssigMed.setAttribute("id", "readyFieldMed");
	newAssigMed.setAttribute("type", "text");
	newAssigMed.setAttribute("name", "newMed");
	newAssigMed.setAttribute("class","value");
	newAssigMed.setAttribute("placeholder", "Medication");

	newInd.setAttribute("id", "readyFieldInd");
	newInd.setAttribute("type", "text");
	newInd.setAttribute("name", "newInd");
	newInd.setAttribute("class", "value");
	newInd.setAttribute("placeholder", "Indication");
	
	if (!newAssigMed && !newInd) {
		setTimeout(function(){fieldsMess.innerHTML = "Can't add field, try again or contact support!";} , 200);

	} else {
		postfieldMed.appendChild(newAssigMed);
		postfieldInd.appendChild(newInd);
		setTimeout(function(){fieldsMess.innerHTML = "field added successfully!";} , 200);
				
	}
}

function RemuveField(id) {
	var getFieldInd = document.getElementById(id);
	var fieldsMess = document.getElementById("fieldsMessages");
	if (!getFieldInd){

		fieldsMess.innerHTML = "Did you add field?";
	}else{ 
	var fieldInd = getFieldInd.parentNode;

	fieldInd.removeChild(getFieldInd);
	var fieldsMess = document.getElementById("fieldsMessages");
	setTimeout(function(){fieldsMess.innerHTML = "The Field removed successfully!";} , 200);
	
	}
}

function RemuveFields(id) {
	var getFieldMed = document.getElementById(id);
	if (!getFieldMed){
		console.log("No funciona");
	}else{ 
	var fieldMed = getFieldMed.parentNode;

	fieldMed.removeChild(getFieldMed);
	console.log("Eureca Med");
	}
}

/*====================================================
    ADD FIELLDS TEST
====================================================*/

function addfieldTest() {
	var newTestName = document.getElementById("newFldTestName");
	var newDoBefore = document.getElementById("newFldDoBefore");
	var fieldsMessTest = document.getElementById("fieldsMessagesTest");
	var newFieldTest = document.createElement('input');
	var newFieldDoBe = document.createElement('input');
	newFieldTest.setAttribute("id", "readyFieldTest");
	newFieldTest.setAttribute("type", "text");
	newFieldTest.setAttribute("name", "readyTestName");
	newFieldTest.setAttribute("class","validate");
	newFieldTest.setAttribute("placeholder", "Test Name");
	newFieldDoBe.setAttribute("value", " ");

	newFieldDoBe.setAttribute("id", "readyFieldDoBe");
	newFieldDoBe.setAttribute("type", "date");
	newFieldDoBe.setAttribute("name", "readyDoBefore");
	newFieldDoBe.setAttribute("class", "validate");
	newFieldDoBe.setAttribute("placeholder", "Do Before");
	newFieldDoBe.setAttribute("value", " ");
	
	if (!newFieldTest && !newFieldDoBe) {
		setTimeout(function(){fieldsMessTest.innerHTML = "Can't add field, try again or contact support!";} , 200);

	} else {
		newTestName.appendChild(newFieldTest);
		newDoBefore.appendChild(newFieldDoBe);
		setTimeout(function(){fieldsMessTest.innerHTML = "field added successfully!";} , 200);
				
	}
}

function RemuveFieldTest(id) {
	var getFieldTest = document.getElementById(id);
	var fieldsMessTest = document.getElementById("fieldsMessagesTest");
	if (!getFieldTest){
		setTimeout(function(){fieldsMessTest.innerHTML = "Did you add field!";} , 200);
	}else{ 
	var fieldTest = getFieldTest.parentNode;

	fieldTest.removeChild(getFieldTest);
	var fieldsMessTest = document.getElementById("fieldsMessagesTest");
	setTimeout(function(){fieldsMessTest.innerHTML = "The Field removed successfully!";} , 200);
	
	}
}

function RemuveFieldsDoBe(id) {
	var getFieldTest = document.getElementById(id);
	if (!getFieldTest){

	}else{ 
	var fieldTest = getFieldTest.parentNode;
	fieldTest.removeChild(getFieldTest);

	}
}



