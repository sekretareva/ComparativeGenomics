$(function () {
    $('#clsFormBtn').click(function () {
        var form_data = new FormData($('#clsForm')[0]);
        $('#clsSlide').html('<img width="50px" src="static/images/processing.gif">');
        $.ajax({
            type: 'POST',
            url: '/classify',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            success: function (data) {
                $('#clsSlide').html(data);
            },
        });
    });
});

$.fn.reset = function () {
    console.log("reseting");
    var form_data = new FormData($('#resetForm')[0]);
    $.ajax({
        type: 'POST',
        url: '/reset',
        data: form_data,
        contentType: false,
        cache: false,
        processData: false,
        success: function (data) {
            $('#clsSlide').html(data);
        },
    });
};

$(function () {
    $('#countFormBtn').click(function () {
        var form_data = new FormData($('#countForm')[0]);
        $('#countSlide').html('<img width="50px" src="static/images/processing.gif">');
        $.ajax({
            type: 'POST',
            url: '/count',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            success: function (data) {
                $('#countSlide').html(data);
            },
        });
    });
});
$(function () {
    $('#vslFormBtn').click(function () {
        var form_data = new FormData($('#vslForm')[0]);
        $('#vslSlide').html('<img width="50px" src="static/images/processing.gif">');
        $.ajax({
            type: 'POST',
            url: '/visualize',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            success: function (data) {
                $('#vslSlide').html(data);
            },
        });
    });
});
$(function () {
    $('#uploadBreakdownBtn').click(function () {
        var form_data = new FormData($('#uploadBreakdown')[0]);
        $('#breakdownDisplay').html('<img width="50px" src="static/images/processing.gif">');
        $.ajax({
            type: 'POST',
            url: '/uploadBreakdown',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            success: function (data) {
                $('#breakdownDisplay').html(data);
            },
        });
    });
});