$(function() {

	$('#habit-name-row-table > tbody > tr, #add-habit').affix({
	    offset: { top: $('#habit-history').offset().top - $('.navbar').height()}
	});

	$('#habit-name-row-table, #habit-table').css('margin-left', -$('#habit-name-row-table').width() / 2);
	
	$('#habit-table td').on('click', function() {
		if ($(this).attr('disabled') !== "disabled") {
			$(this).toggleClass('success danger');
		}
	});

});