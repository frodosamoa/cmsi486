$(function() {

	$('#habit-name-row-table > tbody > tr, #habit-actions').affix({
	    offset: { top: $('#habit-history').offset().top - $('.navbar').height()}
	});
	
	$('#habit-table td').on('click', function() {
		if ($(this).attr('disabled') !== "disabled") {
			$(this).toggleClass('success danger');
			var habitInstance = $(this).attr('name');
			var value = $("#" + habitInstance).attr('value');
			$("#" + habitInstance).attr('value', value === "true" ? "false" : "true");
		}
	});

});