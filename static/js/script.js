$(function(){
    $('button').click(function(){
        $.ajax({
            url: '/returnAnswer',
            data: $('form').serialize(),
            type: 'POST',
        }).done(function (data) {
            var parsed = JSON.parse(data);
            $("#output").html(parsed['user']);
        });
    });
});