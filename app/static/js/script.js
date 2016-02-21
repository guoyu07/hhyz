/**
 * Created by chuckcheng on 16/2/2.
 */
$(function ($) {




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

    $(function () {
        $('[data-toggle="popover"]').popover()
    })
});
