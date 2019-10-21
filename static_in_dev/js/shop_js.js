

$(document).scroll(function () {
    var y = $(this).scrollTop();
    if (y > 800) {
        $('.bottomMenu').fadeIn();
    } else {
        $('.bottomMenu').fadeOut();
    }

});