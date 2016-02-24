/**
 * Created by chuckcheng on 16/2/2.
 */
$(function () {
    //注册验证
    $('.register-content').blur(function () {
        if ($(this).val() != '') {
            $(this).parent().parent().children().children('.register-tag').hide()
        } else {
            $(this).parent().parent().children().children('.register-tag').show()
        }
    });


    //插入html元素
    $.get('/auth/login', {}, function (data) {
        $('#login_panel').append(data)
        $('#login_auth_code_img').attr('src', '/auth/authcode?nums=' + Math.random())
        $('#login_auth_code_img').click(function () {
            $('#login_auth_code_img').attr('src', '/auth/authcode?nums=' + Math.random())
        });
        $('#login_btn').click(function () {
            var username = $('#login_username').val()
            var password = $('#login_password').val()
            var verification = $('#login_verification').val()
            var remember_me = $('#login_remember_me').val()
            var csrf_token = $('#login_csrf_token').val()
            $.post('/auth/login', {
                'username': username,
                'password': password,
                'remrmber_me': remember_me,
                'verification': verification,
                'csrf_token': csrf_token
            }, function (data) {
                if (data['success']) {
                    window.location.reload()
                }
                else {
                    if (data['show_auth']) {
                        $('#login_auth_code_div').show()
                        $('#login_auth_code_img').attr('src', '/auth/authcode?nums=' + Math.random())
                    }
                    $('#login_info').show()
                }
            }, 'json');
        });
    }, 'html')

    $('#register_auth_code').click(function () {
        $('#register_auth_code').attr('src', '/auth/authcode?nums=' + Math.random())
    });

    //$(function () {
    //    $('[data-toggle="popover"]').popover()
    //})
    $('#collect_a').click(function () {

    });
    function add_comment(content, parent_id, callback) {
        var post_id = $('#post_id').val()
        if (content == '') {
            $('.comment-warnning').show()
            return;
        }
        $.post('/api/add_comment', {content: content, post_id: post_id, parent_id: parent_id}, function (data) {
            if (data['state'] == 'success') {
                $('#comment-append').prepend('<div class="comment"><div class="row">\
                        <div class="col-md-1">\
                            <a href="#" target="_blank">\
                                <img src="' + data['avatar'] + '" width="70" height="70">\
                            </a>\
                        </div>\
                        <div class="col-md-11">\
                            <div class="row margin-left-1">\
                                <div class="col-md-12">\
                                    <div class="comment-title">\
                                        <a href="#" target="_blank">' + data['username'] + '</a>\
                                        <a href="#" class="float-right">回复此评论</a>\
                                        <span class="float-right comment-time">' + data['time'] + '</span>\
                                    </div>\
                                </div>\
                            </div>\
                            <div class="row margin-left-1">\
                                <div class="col-md-12 margin-top-1">\
                                    ' + content + '\
                                </div>\
                            </div>\
                        </div>\
                    </div><hr/></div>')
                $('#comment-content').val('')
                callback()
            }
            else {

            }
        }, 'json')
    }

    $('#comment-add-btn').click(function () {
        var content = $('#comment-content').val()
        add_comment(content)
    })
    function get_comments(page) {
        post_id = $('#post_id').val()
        $.post('/api/get_comments', {page: page, post_id: post_id}, function (data) {
            $('#comment').html(data)
            bindComment()
        }, 'html');
    }

    function bindComment() {
        $('#comment-page-prev').on('click', function () {
            page = parseInt($('#current-page').val())
            get_comments(page - 1)
        }).css('cursor', 'pointer');
        $('#comment-page-next').on('click', function () {
            page = parseInt($('#current-page').val())
            get_comments(page + 1)
        }).css('cursor', 'pointer');
        $('.comment-page').on('click', function () {
            page = $(this).text()
            if (page == $('#current-page').val())
                return
            get_comments(page)
        }).css('cursor', 'pointer');
        $('.comment-reply-input').hide()
        $('.comment-reply-btn').click(function () {
            if ($('#username').val() == '') {
                $('#myModal').modal()
                return
            }
            id = $(this).attr('id')
            reply = $('#comment-reply-input-' + id)
            reply.show()
        }).css('cursor', 'pointer')
        $('.comment-reply-btn').click(function () {
            id = $(this).attr('id')
            text = $('#comment-reply-input-' + id).find('.comment-reply-text')
            content = text.val()
            reply = $('#comment-reply-input-' + id)
            add_comment(content, parent_id = id, function () {
                text.val('')
                reply.hide()
            });
        })
    }

    bindComment()
    $('#comment-content').focus(function () {
        if ($('#username').val() == '') {
            $('#myModal').modal()
        }
    })
    $('.collect_a').click(function () {
        if ($('#username').val() == '') {
            $('#myModal').modal()
            return
        }
    }).css('cursor', 'pointer');

});
