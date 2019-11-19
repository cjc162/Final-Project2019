window.onload = function() {
	displayPhotos();
}

function displayPhotos() {
	var i;
	var id = 0;
	for (i = 0; i < images.value.length; i++) {
		if (i % 3 == 0) {
			id++;
			$('.container').append('<div id="row' + id + '" class="row"><div>');
		}
		$('#row' + id).append('<div class="col-md-4" class="img" id="img' + images.value[i].id + '"><div>');
		$('#img' + images.value[i].id).append('<div class="hovereffect" id="hover' + images.value[i].id + '"><img src=/static/images/' + images.value[i].path + ' height="300px" width="100%"/><div>');
		$('#hover' + images.value[i].id).append('<div class="overlay"><h2>' + images.value[i].name + '</h2><a class="info" href="/img_desc/' + images.value[i].id + '">Read More</a><div>');
	}
}