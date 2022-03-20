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