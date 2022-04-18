function togglePopup(){
    document.getElementById("popup-1").classList.toggle("active");
}

function togglePopup1(){
    document.getElementById("popup-2").classList.toggle("active");
}

document.addEventListener('keydown', function(event){
	if(event.key === "Escape"){
        if(document.getElementById("popup-1").classList.contains("active"))
            document.getElementById("popup-1").classList.toggle("active");
        if(document.getElementById("popup-2").classList.contains("active"))
            document.getElementById("popup-2").classList.toggle("active");
	}
});

$(document).ready(function() {
    $('#NewExchaneListing_exchange_from').select2();
    $('#NewExchaneListing_exchange_to').select2();
    $('#id_exchange_from').select2();
    $('#id_exchange_to').select2();
});

$(function(){         
    var message_ele = document.getElementById("message_container");
    setTimeout(function(){ 
    message_ele.style.display = "none"; 
    }, 3000);
  });

$(function(){         
    $('.innerBar').animate({ width: "0%" }, 3000);
  });