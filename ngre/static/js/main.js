const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(function(){
    alert('test');
    $('#message').fadeOut('slow');
},3000);