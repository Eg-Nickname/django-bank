$(document).ready(function() {
    $('#NewTransactionOrder_waluta').select2();
    $('#NewTransactionOrder_transaction_delay').select2();
    $('#id_waluta').select2();
    $('#id_transaction_delay').select2();
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