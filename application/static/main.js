$(document).ready (function() {

	console.log("Loaded");

	$('.patients-list').hide();
	$('.right-sidebar').hide();
	$('.throbber').hide();
	$('.throbber').hide();

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

			var date_of_birth = data['date_of_birth'];

			console.log(date_of_birth);
			$(".pname").text(patient_name);


			if($('.patients-list').is(":hidden")) {
				$('.content').fadeIn().	show();
				$('.patients-list').fadeIn().show();
				$('.right-sidebar').fadeIn().show();	
			}

			$('.throbber').hide();
			$(".pdob").empty();
			$(".pdob").text("Date of Birth: ");
			$(".pdoa").empty();
			$(".pdoa").text("Date of Admission: ");

			$(".pdob").append(date_of_birth);
			$(".pdoa").append(data['date_of_admission']);
			$(".other_info").text("Other info: " + data["other_info"]);


		});
	}

	$('a.patient-link').click(function(e) {
		console.log("LINKED CLICKED.");
		//$('.patients-list').hide();

		if($('.patients-list').is(":visible")) {
			//$('.content').hide();
		}
		//$('.right-sidebar').hide();
		$('.throbber').show();
		e.preventDefault();
		var id = $(this).attr('patient');
		console.log(id);
		console.log("WORKING");
		fetchPatient(id);
	});





});
