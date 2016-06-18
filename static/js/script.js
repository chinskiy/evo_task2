$(function(){
    $('button').click(function(){
        $.ajax({
            url: '/returnAnswer',
            data: $('form').serialize(),
            type: 'POST',
        }).done(function (data) {
            var parsed = JSON.parse(data);
            if (parsed['user'].length > 0){
             $('#output').html("Рад тебя видеть снова, " + parsed['word'] + parsed['user']);
            };
        });
    });
});

$(document).on('keypress', 'form', function(event) { 
    return event.keyCode != 13;
});
