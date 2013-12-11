$(function() {

	$('#habit-name-row-table > tbody > tr, #habit-actions').affix({
	    offset: { top: $('#habit-history').offset().top - $('.navbar').height()}
	});
	
	$('#habit-table td').on('click', function() {
		if ($(this).attr('disabled') !== "disabled") {
			$(this).toggleClass('success danger');
			$(this).html($(this).hasClass("success") ? "<span class=\"glyphicon glyphicon-ok complete\"></span>"
													 : "<span class=\"glyphicon glyphicon-remove todo\"></span>");
			var habitInstance = $(this).attr('name');
			var value = $("#" + habitInstance).attr('value');
			$("#" + habitInstance).attr('value', value === "true" ? "false" : "true");
		}
	});

});