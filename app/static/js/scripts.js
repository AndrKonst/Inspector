$(function() {
    var timer = null;
    var on_hint_fl = 0;
    $(".feature_rec_name").hover(function (e) {
            var elem = $(e.currentTarget);
            timer = setTimeout(function () {
            timer = null;
            $.get('/feature/' + elem.text().trim()).done(function (data) {
            $('#hint').html(data);
            var left = e.pageX - $('#hint').width()/2
            var top = e.pageY - $('#hint').height() - 20
            $('#hint').css({'left': left, 'top': top});
            $('#hint').show();});
        }, 500);
        }, function () {
            if (timer) {
                        clearTimeout(timer);
                        timer = null;
            } else {
                setTimeout(function () {
                    if (on_hint_fl ===0) $('#hint').hide();
                }, 200);
            }

        });
    $('#hint').hover(function () {
        on_hint_fl = 1;
    }, function () {
        on_hint_fl = 0;
        $('#hint').hide();
    });
});
