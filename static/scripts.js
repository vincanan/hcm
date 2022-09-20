// 포스트
function post() {
    let title = $('#title').val()
    let url = $('#url').val()
    let keywords = $('#keywords').val()

    $.ajax({
        type: 'POST',
        enctype: 'multipart/form-data',
        url: '/api/reviewspost',
        data: { title:title, url:url, keywords:keywords},
        success: function (response) {
            alert(response['msg'])
            window.location.reload()
        }
    });
}