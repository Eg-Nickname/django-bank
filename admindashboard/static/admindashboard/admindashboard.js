function togglePopup(){
    document.getElementById("popup-1").classList.toggle("active");
}

document.addEventListener('keydown', function(event){
	if(event.key === "Escape"){
        if(document.getElementById("popup-1").classList.contains("active"))
            document.getElementById("popup-1").classList.toggle("active");
	}
});