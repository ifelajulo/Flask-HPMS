$(document).ready (function() {

	console.log("Loaded");


	$('.throbber').hide();

	//alertify.alert("Hello, hello.");



	var myVar = setInterval(function() {
		sendAlert();
	}, 1000*60*5);

	var i = 1;
	console.log($('.pat'));
	console.log($('.med'));

	var patients = $('.pat');

	var limit = patients.size();

	var random = Math.round(Math.random()*limit);
	console.log(random);

	random_element = $("ul li:eq(" + random + ")");
		


	alertify.log("Just an example of a reminder that will pop up to alert nurses.");

	function sendAlert() {
		var patient_name = $("ul li:eq(" + i + ")");

		console.log($(patient_name));
		console.log(patient_name);
		console.log($(patient_name).attr("pat"));
		//alertify.log($(patient_name).attr("pat") + " requires their medication " + $(patient_name).attr("medi"));
		//alertify.log("A patient requires their medication!","",0);
		//
		alertify.log("Medication Reminder Alert: Patient Jesse Daniel Requires Medication now!");

		// Talk abou

	}

/*	interface Notification : EventTarget {

		void show();
		void cancel();

		attribute Function ondisplay;
		attribute Function onerror;
		attribute Function onclose;
		attribute Function onclick;
	}

	interface NotificationCenter {
		// Notification factory methods
		// 
		const unsigned int  PERMISSION_ALLOWED = 0;
		const unsigned int PERMISSION_NOT_ALLOWED = 1;
		const unsigned int PERMISSION_DENIED = 2;

		int checkPermission();
		void requestPermission(in Function callback);
	}

	interface Win*/

	function fetchPatient(id) {
		console.log("Fetching patient ID");
		var request = $.ajax({
			type: 'GET',
			url: '/dashboard/patients/' + id + '/',
		});


		$('.patients-list').hide();
		$('.right-sidebar').hide();
		$('.throbber').hide();

		request.done(function(data) {
			console.log("SUCCESS!");
			console.log(data);

			var patient_name = data['first_name'] + " " + data['last_name'];

			//var date_of_birth = data['date_of_birth'];

			console.log(date_of_birth);
			$(".pname").text(patient_name);


			if($('.patients-list').is(":hidden")) {
				$('.content').fadeIn().	show();
				$('.patients-list').fadeIn().show();
				$('.right-sidebar').fadeIn().show();	
				console.log("SHOWING STUFF");
			}

			$('.patents-list').show();
			$('.content').fadeIn().show();
			$('.throbber').hide();

			$('html').innerHTML() = data;
			/*$(".pdob").empty();
			$(".pdob").text("Date of Birth: ");
			$(".pdoa").empty();
			$(".pdoa").text("Date of Admission: ");

			$(".pdob").append(date_of_birth);
			$(".pdoa").append(data['date_of_admission']);

			$(".")
			$(".other_info").text("Other info: " + data["other_info"]);*/


		});
	}

	$('a.patient-link').click(function(e) {
		console.log("LINKED CLICKED.");

		$('.patients-list').show();
		$('.right-sidebar').show();
		//$('.patients-list').hide();

		/*if($('.patients-list').is(":visible")) {
			//$('.content').hide();
		}
		//$('.right-sidebar').hide();
		//$('.throbber').show();
		//e.preventDefault();
		var id = $(this).attr('patient');
		console.log(id);
		console.log("WORKING");
		//fetchPatient(id);*/
	});





});
