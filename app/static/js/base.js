$(document).ready(function(){
  $('.td1').hover(
    function(){
        $(this).addClass('topmenu');
    },
    function(){
        $(this).removeClass('topmenu');
    }
  );
});
// $(document).ready(function() {
//     $(".td1").accordion({collapsible: true, active: false});
// });


$(document).ready(function(){
  $('.td2').hover(
    function(){
        $(this).addClass('topmenu');
    },
    function(){
        $(this).removeClass('topmenu');
    }
  );
});
$(document).ready(function() {
    $(".td2").accordion({collapsible: true, active: false});
});


$(document).ready(function(){
  $('.td3').hover(
    function(){
        $(this).addClass('topmenu');
    },
    function(){
        $(this).removeClass('topmenu');
    }
  );
});
$(document).ready(function() {
    $(".td3").accordion({collapsible: true, active: false});
});


$(document).ready(function(){
    $('.img1').fadeTo(0,1)
    $('.img1').hover(
        function(){
            $(this).fadeTo('fast',0.5);
        },
        function(){
            $(this).fadeTo('fast',1);
        }); 
})
$(document).ready(function(){
    $('.img2').fadeTo(0,1)
    $('.img2').hover(
        function(){
            $(this).fadeTo('fast',0.5);
        },
        function(){
            $(this).fadeTo('fast',1);
        }); 
})
$(document).ready(function(){
    $('.img3').fadeTo(0,1)
    $('.img3').hover(
        function(){
            $(this).fadeTo('fast',0.5);
        },
        function(){
            $(this).fadeTo('fast',1);
        }); 
})
$(document).ready(function(){
    $('.img4').fadeTo(0,1)
    $('.img4').hover(
        function(){
            $(this).fadeTo('fast',0.5);
        },
        function(){
            $(this).fadeTo('fast',1);
        }); 
})
$(document).ready(function(){
    $('.img5').fadeTo(0,1)
    $('.img5').hover(
        function(){
            $(this).fadeTo('fast',0.5);
        },
        function(){
            $(this).fadeTo('fast',1);
        }); 
})
$(document).ready(function(){
    $('.img6').fadeTo(0,1)
    $('.img6').hover(
        function(){
            $(this).fadeTo('fast',0.5);
        },
        function(){
            $(this).fadeTo('fast',1);
        }); 
})
$(document).ready(function(){
    $('.img7').fadeTo(0,1)
    $('.img7').hover(
        function(){
            $(this).fadeTo('fast',0.5);
        },
        function(){
            $(this).fadeTo('fast',1);
        }); 
})
$(document).ready(function(){
    $('.img8').fadeTo(0,1)
    $('.img8').hover(
        function(){
            $(this).fadeTo('fast',0.5);
        },
        function(){
            $(this).fadeTo('fast',1);
        }); 
})
$(document).ready(function(){
    $('.img9').fadeTo(0,1)
    $('.img9').hover(
        function(){
            $(this).fadeTo('fast',0.5);
        },
        function(){
            $(this).fadeTo('fast',1);
        }); 
})
//function a(v1,v2,v3,v4){
//  $(v1).fadeOut(1000)
//  $(v2).fadeIn(1000,function(){
//      a(v2,v3,v4,v1);
//  })
//}

$(document).ready(function() {
        $('.best1').dblclick(function() {
            $(this).fadeOut('fast');
        });
});
$(document).ready(function(){
        $('.best2').click(function(){
            $(this).effect('explode');
        });
});
$(document).ready(function(){
        $('.best3').click(function(){
            $(this).effect('bounce', {times:3}, 500)
        });
});