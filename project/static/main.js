
$(document).ready(function() {
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
	
	// ----- GET ON PAGE LOAD -----
	ajax_get("/get_user_data",
		function(response) {
			console.log(response['results'][0])
			let user_cellphone = response['results'][0]['cell']
		},
		function(jqXHR) {
		
		})
})