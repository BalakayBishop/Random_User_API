
$(document).ready(function (locales) {
	// ----- AJAX FUNCTION -----
	function ajax(url, type, data, success, fail) {
		$.ajax({
			url: url,
			type: type,
			contentType: 'application/json',
			data: data,
			success: success,
			error: fail
		});
	}
	
	// ----- AJAX GET FUNCTION -----
	function ajax_get(url, success, fail) {
		$.ajax({
			url: url,
			type: 'GET',
			success: success,
			error: fail
		});
	}
	
	const options = {
		year: 'numeric',
	    month: '2-digit',
	    day: '2-digit'
	};
	
	// ----- GET ON PAGE LOAD -----
	ajax_get("/get_user_data",
		function(response) {
			let _response = response['results'][0]
			
			console.log(_response)
			
			const user_fname = _response['name']['first']
			const user_mname = _response['name']['middle']
			const user_lname = _response['name']['last']
			
			let dob = _response['dob']['date']
			dob = new Date(dob)
			const user_dob = dob.toLocaleString("en-US", options)
			
			const user_cellPhone = _response['cell']
			const user_email = _response['email']
			const user_gender = _response['gender']
			const user_city = _response['location']['city']
			const user_country = _response['location']['country']
			const user_postal = _response['location']['postcode']
			const user_street = _response['location']['number'] + " " + _response['location']['name']
			const user_pic_url = _response['picture']['medium']
			
		},
		function(jqXHR) {
		
	});
})