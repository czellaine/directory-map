$(document).ready(function() {
    $('tr.result').click(function() {
        $.ajax({
            url: '/ajax/getLocation',
            data: {
                'acc_no': $(this).data('acc')
            },
            dataType: 'json',
            success: function(data) {
                img_path = '/app/static/img/';
                img = data.location.location + '.jpg';
                $('img#location').attr('src', img_path + img)
            }
        });
    });
});
