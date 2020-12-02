/*====================================================
    MATERIALICE SELECT PLUGIN
====================================================*/

$(document).ready(function(){
    $('select').formSelect();
  });


  /*====================================================
    LIST DROPDOWN
====================================================*/
$('.dropdown-trigger').dropdown();
$('.dropdown-trigger-0').dropdown();



/*============================BACKGROUND INDEX*/

$(document).ready(function(){
    $('.parallax').parallax();
  });

  
/*====================================================
    ADD FIELLDS DOCTOR
====================================================*/

function addfield() {
	var postfieldIssues = document.getElementById("newfieldMed");
	var postfieldInttService = document.getElementById("newfieldInd");
	var fieldsNsMess = document.getElementById("fieldsNsMessages");
	var newIssues = document.createElement('input');
	var newInttService = document.createElement('input');
	newIssues.setAttribute("id", "readyFieldMed");
	newIssues.setAttribute("type", "text");
	newIssues.setAttribute("name", "newMed");
	newIssues.setAttribute("class","value");
	newIssues.setAttribute("placeholder", "Medication");

	newInttService.setAttribute("id", "readyFieldInd");
	newInttService.setAttribute("type", "text");
	newInttService.setAttribute("name", "newInttService");
	newInttService.setAttribute("class", "value");
	newInttService.setAttribute("placeholder", "Indication");
	
	if (!newIssues && !newInttService) {
		setTimeout(function(){fieldsNsMess.innerHTML = "Can't add field, try again or contact support!";} , 200);

	} else {
		postfieldIssues.appendChild(newIssues);
		postfieldInttService.appendChild(newInttService);
		setTimeout(function(){fieldsNsMess.innerHTML = "field added successfully!";} , 200);
				
	}
}

function RemuveField(id) {
	var getFieldInd = document.getElementById(id);
	var fieldsNsMess = document.getElementById("fieldsMessages");
	if (!getFieldInd){

		fieldsNsMess.innerHTML = "Did you add field?";
	}else{ 
	var fieldInd = getFieldInd.parentNode;

	fieldInd.removeChild(getFieldInd);
	var fieldsNsMess = document.getElementById("fieldsMessages");
	setTimeout(function(){fieldsNsMess.innerHTML = "The Field removed successfully!";} , 200);
	
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
	var fieldNsMessages = document.getElementById("fieldsNsMessagesTest");
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
		setTimeout(function(){fieldNsMessages.innerHTML = "Can't add field, try again or contact support!";} , 200);
		var toastHTML = '<span>I am toast content</span><button class="btn-flat toast-action">Undo</button>';
		M.toast({html: toastHTML});

	} else {
		newTestName.appendChild(newFieldTest);
		newDoBefore.appendChild(newFieldDoBe);
		setTimeout(function(){fieldNsMessages.innerHTML = "field added successfully!";} , 200);
				
	}
} 


/*====================================================
    REMOVE FIELLDS DOCTOR
====================================================*/
function RemuveFieldTest(id) {
	var getfieldsNs = document.getElementById(id);
	var fieldNsMessages = document.getElementById("fieldsNsMessagesTest");
	if (!getfieldsNs){
		setTimeout(function(){fieldNsMessages.innerHTML = "Did you add field!";} , 200);
	}else{ 
	var fieldTest = getfieldsNs.parentNode;

	fieldTest.removeChild(getfieldsNs);
	var fieldNsMessages = document.getElementById("fieldsMessagesTest");
	setTimeout(function(){fieldNsMessages.innerHTML = "The Field removed successfully!";} , 200);
	
	}
}

function RemuveFieldsDoBe(id) {
	var getfieldsNs = document.getElementById(id);
	if (!getfieldsNs){

	}else{ 
	var fieldTest = getfieldsNs.parentNode;
	fieldTest.removeChild(getfieldsNs);

	}
}


/*====================================================
    ADD FIELLDS NURSE
====================================================*/

function addfieldNs() {
	var postfieldIssues = document.getElementById("newMdlIssues");
	var postfieldInttService = document.getElementById("newInttService");
	var fieldsNsMess = document.getElementById("fieldsNsMessages");
	var newIssues = document.createElement('input');
	var newInttService = document.createElement('input');
	newIssues.setAttribute("id", "NewFieldIssues");
	newIssues.setAttribute("type", "text");
	newIssues.setAttribute("name", "NewFieldIssues");
	newIssues.setAttribute("class","value");
	newIssues.setAttribute("placeholder", "Medical Issues");

	newInttService.setAttribute("id", "newFieldtService");
	newInttService.setAttribute("type", "text");
	newInttService.setAttribute("name", "newFieldtService");
	newInttService.setAttribute("class", "value");
	newInttService.setAttribute("placeholder", "Intensity of Service");
	
	if (!newIssues && !newInttService) {
		setTimeout(function(){fieldsNsMess.innerHTML = "Can't add field, try again or contact support!";} , 200);

	} else {
		postfieldIssues.appendChild(newIssues);
		postfieldInttService.appendChild(newInttService);
		setTimeout(function(){fieldsNsMess.innerHTML = "field added successfully!";} , 200);
				
	}
}
/*====================================================
    REMOVE FIELLDS NURSE
====================================================*/

function RemuveFieldNsIs(id) {
	var getfieldsNs = document.getElementById(id);
	var fieldNsMessages = document.getElementById("fieldsNsMessagesTest");
	if (!getfieldsNs){
		setTimeout(function(){fieldNsMessages.innerHTML = "Did you add field!";} , 200);
	}else{ 
	var fieldTest = getfieldsNs.parentNode;

	fieldTest.removeChild(getfieldsNs);
	var fieldNsMessages = document.getElementById("fieldsMessagesTest");
	setTimeout(function(){fieldNsMessages.innerHTML = "The Field removed successfully!";} , 200);
	
	}
}

function RemuveFieldNsInt(id) {
	var getfieldsNs = document.getElementById(id);
	if (!getfieldsNs){

	}else{ 
	var fieldNsTest = getfieldsNs.parentNode;
	fieldNsTest.removeChild(getfieldsNs);

	}
}

/*============================*/
/*     TOAST MATERIAL */


$(document).ready(function(){
	$('.messages').hide(2000);
});


