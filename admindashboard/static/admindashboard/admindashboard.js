// Page stays on scroll position after reload
document.addEventListener("DOMContentLoaded", function(event) { 
    var scrollpos = localStorage.getItem('scrollpos');
    if (scrollpos) window.scrollTo(0, scrollpos);
});

window.onbeforeunload = function(e) {
    localStorage.setItem('scrollpos', window.scrollY);
};

// Select2
$(document).ready(function() {
    $('#id_waluta').select2();
});

// Messages
var message_element = document.getElementById("message-container");
setTimeout(function(){ 
    message_element.style.display = "none"; 
}, 5000);


