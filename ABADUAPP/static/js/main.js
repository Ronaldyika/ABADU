$(document).on('submit','#message', function(e){
    e.preventDefault();
    $.ajax({
        type:'POST',
        url:"",
        data:{
            message: $('#msg').val(),
            csrfmiddlewaretoken:$( 'input[name=csrfmiddlewaretoken]' ).val()
        },
        success: function() {
            // Reload both the parent container and message container
            $('.parent').load(window.location.href + ' .parent');
            $('.message').load(window.location.href + ' .message');
            // Clear the input field after the message is sent
            $('#msg').val('');
        }
    });
});

$(document).ready(function(){
    setInterval(function(){
        $( ".message" ).load(window.location.href + " .message" );
    },2000);
});