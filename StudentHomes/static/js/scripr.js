$(document).on('click', '#likePost', function (e) {
    e.preventDefault();
    $.ajax({
type:'GET',
        url:'/user/like',
        data:{
    listing: $("#likePost").attr("data")
        },
        success:function () {
            var x = $("#notliked");
            var y = $("#liked");
            if (x.is(":visible")) {
                x.hide();
                y.show();
            } else {
                x.show();
                y.hide();
            }
        }
    })
});
