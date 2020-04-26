/*====================================================
    APPOINTMENTS
====================================================*/
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
	  
  }
