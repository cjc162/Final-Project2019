window.onload = function() {
	createCarousel();

	$('.carousel').carousel({
  		interval: 4000
	})
}

function createCarousel() {
	$('.container').append('<div id="carousel_images" class="carousel slide" data-ride="carousel"><div class="carousel-inner"></div></div>');

	var i;
	for (i = 0; i < images.value.length; i++) {
		if (i == 0) {
			$('.carousel-inner').append('<div class="carousel-item active"><img class="d-block w-100" src="/static/images/' + images.value[i].path + '" height="400px" width="100%"></div>');
		} else {
			$('.carousel-inner').append('<div class="carousel-item"><img class="d-block w-100" src="/static/images/' + images.value[i].path + '" height="400px" width="100%"></div>');
		}
	}

	$('.carousel-inner').append('<a class="carousel-control-prev" href="#carousel_images" role="button" data-slide="prev"><span class="carousel-control-prev-icon" aria-hidden="true"></span><span class="sr-only">Previous</span></a>');
	$('.carousel-inner').append('<a class="carousel-control-next" href="#carousel_images" role="button" data-slide="next"><span class="carousel-control-next-icon" aria-hidden="true"></span><span class="sr-only">Next</span></a>');
}