$(document).ready(function() {
    $('tr.result').click(function() {
        $.ajax({
            url: '/ajax/getLocation',
            data: {
                'acc_no': $(this).data('acc')
            },
            dataType: 'json',
            success: function(data) {
                $('img#location').attr('src', data.file)
            }
        });
    });
});
