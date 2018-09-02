$(document).ready(function(){
      $('.slider').bxSlider({
      	auto:true,
      	nextText: '<i class="fa fa-angle-right" aria-hidden="true"></i>',
      	prevText: '<i class="fa fa-angle-left" aria-hidden="true"></i>',
      	pager:false,
      });


      $('.testimonial-slider').bxSlider({
      	minSlides: 1,
        maxSlides: 2,
        slideWidth: 500,
        slideMargin: 20,
        auto:true,
      	controls:false,
      	speed: 800,
      });
    });

$(document).ready(function(){
  if ($(window).width() >= 768){  
    $('.form-wrapper').addClass('show');
  }
});

$(window).resize(function(){
  if ($(window).width() >= 768){  
    $('.form-wrapper').addClass('show');
  }
  if ($(window).width() <= 768){  
    $('.form-wrapper').removeClass('show');
  }
});

$('.form-header').click(function(e){
  if ($(window).width() >= 768){  
    e.stopPropagation();
  }    
});

$(window).on('scroll', function(event) {
    var scrollValue = $(window).scrollTop();
    if (scrollValue > 44) {
         $('.navbar').addClass('affix');
    } 
    else
      $('.navbar').removeClass('affix');
});

$('.top-header').parallaxie({
});