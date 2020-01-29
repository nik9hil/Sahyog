$(document).ready(function() {
"use strict";

/*
|----------------------------------------------------------------------------
| PRELOADER
|----------------------------------------------------------------------------
*/
// makes sure the whole site is loaded
$(window).on('load', function() {
   // will first fade out the loading animation
   $(".spinner").fadeOut();
   //then background color will fade out slowly
   $(".pre-loader").delay(200).fadeOut("slow");
});



/*
|----------------------------------------------------------------------------
| STICKY NAVBAR
|----------------------------------------------------------------------------
*/

    $('.dropdown-menu a.dropdown-toggle').on('click', function(e) {
      var $el = $(this);
      var $parent = $(this).offsetParent(".dropdown-menu");
      if (!$(this).next().hasClass('show')) {
        $(this).parents('.dropdown-menu').first().find('.show').removeClass("show");
      }
      var $subMenu = $(this).next(".dropdown-menu");
      $subMenu.toggleClass('show');
      
      $(this).parent("li").toggleClass('show');

      $(this).parents('li.nav-item.dropdown.show').on('hidden.bs.dropdown', function (e) {
        $('.dropdown-menu .show').removeClass("show");
      });
      
      if (!$parent.parent().hasClass('navbar-nav')) {
        $el.next().css({"top": $el[0].offsetTop, "left": $parent.outerWidth() - 4});
      }

      return false;
    });

    if($(window).width() < 1200) {
      $(document).on('click', function(event) {
        var clickover = $(event.target);
        var _opened = $('#navbarSupportedContent').hasClass('show');
        if(_opened === true && !(clickover.is('.navbar-nav li, .navbar-nav .dropdown *'))) {
          $('button.navbar-toggler').trigger('click');
        }
      });
    }



  if ( matchMedia( 'only screen and (min-width: 991px)' ).matches ) {
     $(document).on('scroll', function() {
        var scrollPos = $(this).scrollTop();

        if( scrollPos > 150 ) {
           $('.fixed-nav').addClass('fixed');
        } else {
           $('.fixed-nav').removeClass('fixed');
        }
     });
  }


  if($(window).width() < 992) {
    $(document).on('click', function(event) {
      var clickover = $(event.target);
      var _opened = $('#navbarNav').hasClass('show');
      if(_opened === true && !(clickover.is('.navbar-nav li, .navbar-nav .dropdown *'))) {
        $('button.navbar-toggler').trigger('click');
      }
    });
  }

/*
|----------------------------------------------------------------------------
| SCROLL THROUGH PAGE
|----------------------------------------------------------------------------
*/

    /* ---------------------------------------------
    Smooth scroll
    --------------------------------------------- */
    $('a[href*="#"]:not([href="#"]):not(a[data-toggle="collapse"], a[data-toggle="tab"])').on('click', function () {
        if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
            var target = $(this.hash);
            target = target.length ? target : $('[name' + this.hash.slice(1) + ']');
            if (target.length) {
                $('html, body').animate({
                    scrollTop: target.offset().top
                }, 1000);
                return false;
            }
        }
    });


/*
|----------------------------------------------------------------------------
| REPLACE WITH YOUR COMMENT
|----------------------------------------------------------------------------
*/
if ( matchMedia( 'only screen and (min-width: 768px)' ).matches ) {
  var baseHeight = $('.base-content').height(),
      subHeight = $('.sub-content').height();

  $('.base-content .img-responsive').css('min-height', baseHeight + 'px');
  $('.sub-content .img-responsive').css('min-height', subHeight + 'px');
}


/*
|----------------------------------------------------------------------------
| EVENT TIMING
|----------------------------------------------------------------------------
*/

$('#spc-event').countdown({
  date: "May 7, 2019 15:03:26",
  render: function (date) {
    this.el.innerHTML = "<ul>"
                + "<li><div><h6>" + date.days + "</h6>days</div></li>"
                        + "<li><div><h6>" + this.leadingZeros(date.hours) + "</h6>hours</div></li>"
                        + "<li><div><h6>" + this.leadingZeros(date.min) + "</h6>minutes</div></li> "
                        + "<li><div><h6>" + this.leadingZeros(date.sec) + "</h6>seconds</div></li>"
                        + "</ul>";
  }
});

$('#event-1').countdown({
	date: "May 7, 2019 15:03:26",
	render: function (date) {
   	this.el.innerHTML = "<ul>"
   							+ "<li><div><h6>" + date.days + "</h6>days</div></li>"
                        + "<li><div><h6>" + this.leadingZeros(date.hours) + "</h6>hours</div></li>"
                        + "<li><div><h6>" + this.leadingZeros(date.min) + "</h6>minutes</div></li> "
                        + "<li><div><h6>" + this.leadingZeros(date.sec) + "</h6>seconds</div></li>"
                        + "</ul>";
  }
});

$('#event-2').countdown({
	date: "June 7, 2019 4:01:6",
	render: function (date) {
   	this.el.innerHTML = "<ul>"
   							+ "<li><div><h6>" + date.days + "</h6>days</div></li>"
                        + "<li><div><h6>" + this.leadingZeros(date.hours) + "</h6>hours</div></li>"
                        + "<li><div><h6>" + this.leadingZeros(date.min) + "</h6>minutes</div></li> "
                        + "<li><div><h6>" + this.leadingZeros(date.sec) + "</h6>seconds</div></li>"
                        + "</ul>";
  }
});

$('#event-3').countdown({
	date: "August 7, 2019 11:13:2",
	render: function (date) {
   	this.el.innerHTML = "<ul>"
   							+ "<li><div><h6>" + date.days + "</h6>days</div></li>"
                        + "<li><div><h6>" + this.leadingZeros(date.hours) + "</h6>hours</div></li>"
                        + "<li><div><h6>" + this.leadingZeros(date.min) + "</h6>minutes</div></li> "
                        + "<li><div><h6>" + this.leadingZeros(date.sec) + "</h6>seconds</div></li>"
                        + "</ul>";
  }
});

$('#event-4').countdown({
  date: "May 7, 2019 15:03:26",
  render: function (date) {
    this.el.innerHTML = "<ul>"
                + "<li><div><h6>" + date.days + "</h6>days</div></li>"
                        + "<li><div><h6>" + this.leadingZeros(date.hours) + "</h6>hours</div></li>"
                        + "<li><div><h6>" + this.leadingZeros(date.min) + "</h6>minutes</div></li> "
                        + "<li><div><h6>" + this.leadingZeros(date.sec) + "</h6>seconds</div></li>"
                        + "</ul>";
  }
});

$('#event-5').countdown({
  date: "June 7, 2019 4:01:6",
  render: function (date) {
    this.el.innerHTML = "<ul>"
                + "<li><div><h6>" + date.days + "</h6>days</div></li>"
                        + "<li><div><h6>" + this.leadingZeros(date.hours) + "</h6>hours</div></li>"
                        + "<li><div><h6>" + this.leadingZeros(date.min) + "</h6>minutes</div></li> "
                        + "<li><div><h6>" + this.leadingZeros(date.sec) + "</h6>seconds</div></li>"
                        + "</ul>";
  }
});

$('#event-6').countdown({
  date: "August 7, 2019 11:13:2",
  render: function (date) {
    this.el.innerHTML = "<ul>"
                + "<li><div><h6>" + date.days + "</h6>days</div></li>"
                        + "<li><div><h6>" + this.leadingZeros(date.hours) + "</h6>hours</div></li>"
                        + "<li><div><h6>" + this.leadingZeros(date.min) + "</h6>minutes</div></li> "
                        + "<li><div><h6>" + this.leadingZeros(date.sec) + "</h6>seconds</div></li>"
                        + "</ul>";
  }
});

/*
|----------------------------------------------------------------------------
| CAROUSEL SLIDERS
|----------------------------------------------------------------------------
*/
$('.home .owl-carousel').owlCarousel({
   items: 1,
   autoplay: true,
   nav: true,
   dots: false,
   navText: ["&#xe167;", "&#xe168;"],
   loop: true
});

$('.pet-profile .owl-carousel').owlCarousel({
   items: 1,
   autoplay: true
});

$('.testimonials .owl-carousel').owlCarousel({
   items: 1,
   autoplay: true
});



/*
|----------------------------------------------------------------------------
| SUCCESS STORIES - COUNTER
|----------------------------------------------------------------------------
*/
$('.stat-count').counterUp({
  delay: 30,
  time: 2000
});


/*
|----------------------------------------------------------------------------
| REPLACE WITH YOUR COMMENT
|----------------------------------------------------------------------------
*/
$('#pets-container').mixItUp();

/*
|----------------------------------------------------------------------------
| CONTACT FORM ANIMATION
|----------------------------------------------------------------------------
*/
var inputBox = $('.form-control');

inputBox.on('focus', function() {
   $(this).closest('.input-group').addClass('active');
});

inputBox.on('blur', function() {
   if( $(this).val() === "" ) {
      $(this).closest('.input-group').removeClass('active');
   }
});


/*
|----------------------------------------------------------------------------
| FLICKR FEED
|----------------------------------------------------------------------------
*/
$('.flickr-feed').jflickrfeed({
   limit: 4,
   qstrings: {
      // id: '44802888@N04'
      tags: 'pet, pets'
   },
   itemTemplate: '<li><a href="{{image_b}}" class="anima-lightbox" target="_blank"><img src="{{image_m}}" alt="{{title}}"></a></li>'
});



/*
|----------------------------------------------------------------------------
| AJAX SUBSCRIBE
|----------------------------------------------------------------------------
*/
$("#subscribe").ajaxChimp({
    callback: mailchimpCallback,
    url: "http://bdpark.us7.list-manage1.com/subscribe/post?u=d6649e6cfae99f3bc710a85a5&id=07db0b4bd6" // Replace your mailchimp post url inside double quote "".  
});

function mailchimpCallback(resp) {
     if(resp.result === 'success') {
        $('.subscribe .success-msg')
            .html(resp.msg)
            .delay(500)
            .fadeIn(1000);

        $('.subscribe .error-msg').fadeOut(500);
        
    } else if(resp.result === 'error') {
        $('.subscribe .error-msg')
            .html(resp.msg)
            .delay(500)
            .fadeIn(1000);
            
        $('.subscribe .success-msg').fadeOut(500);
    }  
};


// Function for email address validation
function isValidEmail(emailAddress) {

var pattern = new RegExp(/^(("[\w-\s]+")|([\w-]+(?:\.[\w-]+)*)|("[\w-\s]+")([\w-]+(?:\.[\w-]+)*))(@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$)|(@\[?((25[0-5]\.|2[0-4][0-9]\.|1[0-9]{2}\.|[0-9]{1,2}\.))((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\.){2}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\]?$)/i);

    return pattern.test(emailAddress);

};


/*
|----------------------------------------------------------------------------
| AJAX CONTACT FORM
|----------------------------------------------------------------------------
*/
$("#contact-form").on('submit', function(e) {
    e.preventDefault();
    var data = {
        name: $("#name").val(),
        email: $("#email").val(),
        phone: $("#phone").val(),
        message: $("#message").val()
    };

    if ( isValidEmail(data['email']) && (data['message'].length > 1) && (data['name'].length > 1) ) {
        $.ajax({
            type: "POST",
            url: "sendmail.php",
            data: data,
            success: function() {
                $('.contact-form .success-msg').delay(500).fadeIn(1000);
                $('.contact-form .error-msg').fadeOut(500);
            }
        });
    } else {
        $('.contact-form .error-msg').delay(500).fadeIn(1000);
        $('.contact-form .success-msg').fadeOut(500);
    }

    return false;
});


/*
|----------------------------------------------------------------------------
| TAB TOGGLE
|----------------------------------------------------------------------------
*/
$('#address-map-tab a').on('click', function (e) {
  e.preventDefault();
  $(this).tab('show');
});

$('#anima-tab a').on('click' ,function (e) {
  e.preventDefault();
  $(this).tab('show');
});



/*
|----------------------------------------------------------------------------
| GALLERY LIGHTBOX
|----------------------------------------------------------------------------
*/
$('.anima-lightbox').nivoLightbox();


/*
|----------------------------------------------------------------------------
| VIDEO PLAYER
|----------------------------------------------------------------------------
*/
$('.video-player').fitVids();


/*
|----------------------------------------------------------------------------
| PARALLAX BAKGROUND
|----------------------------------------------------------------------------
*/
$(window).stellar({
  horizontalScrolling: false
});


/*
|----------------------------------------------------------------------------
| COLLAPSE NAVBAR ON CLICK
|----------------------------------------------------------------------------
*/
if ( matchMedia( 'only screen and (max-width: 767px)' ).matches ) {
  $('.nav a').on('click', function(){
     $(".navbar-toggle").click();
  });
}

});