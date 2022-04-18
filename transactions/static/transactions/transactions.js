function togglePopup(){
    document.getElementById("popup-1").classList.toggle("active");
}

document.addEventListener('keydown', function(event){
	if(event.key === "Escape"){
        if(document.getElementById("popup-1").classList.contains("active"))
            document.getElementById("popup-1").classList.toggle("active");
	}
});

function togglePopup2(){
    document.getElementById("popup-2").classList.toggle("active");
}

document.addEventListener('keydown', function(event){
	if(event.key === "Escape"){
        if(document.getElementById("popup-2").classList.contains("active"))
            document.getElementById("popup-2").classList.toggle("active");
	}
});

function togglePopup3(){
    document.getElementById("popup-3").classList.toggle("active");
}

document.addEventListener('keydown', function(event){
	if(event.key === "Escape"){
        if(document.getElementById("popup-3").classList.contains("active"))
            document.getElementById("popup-3").classList.toggle("active");
	}
});

function toggleFilter(){
    document.getElementById("filter-options").classList.toggle("filter-active");
}
$(function(){         
    var message_ele = document.getElementById("message_container");
    setTimeout(function(){ 
       message_ele.style.display = "none"; 
    }, 3000);
 });

$(function(){         
    $('.innerBar').animate({ width: "0%" }, 3000);
 });

 $(document).ready(function() {
    $('#NewTransaction_waluta').select2();
    $('#id_waluta2').select2();
    $('#id_waluta').select2();
    $('#id_daterange').select2();
});