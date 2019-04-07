$(window).scroll(function(){
    var scroll = $(window).scrollTop();
    
    document.getElementById("myBody").style.marginTop=(-100-0.5*scroll) + "px";

    if(scroll >= 200){
        $("#myNav").addClass("bg-dark");
        $("#myNav").removeClass("navbar-light");
        $("#myNav").addClass("navbar-dark");
    } else {
        $("#myNav").removeClass("bg-dark");
        $("#myNav").removeClass("navbar-dark");
        $("#myNav").addClass("navbar-light");
    }

});