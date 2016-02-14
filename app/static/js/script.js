/**
 * Created by chuckcheng on 16/2/2.
 */
$(function ($) {
    //弹出登录
    //$("#example").hover(function () {
    //    $(this).stop().animate({
    //        opacity: '1'
    //    }, 600);
    //}, function () {
    //    $(this).stop().animate({
    //        opacity: '0.6'
    //    }, 1000);
    //}).on('click', function () {
    //    $("body").append("<div id='mask'></div>");
    //    $("#mask").addClass("mask").fadeIn("slow");
    //    $("#LoginBox").fadeIn("slow");
    //});
    //
    //按钮的透明度
    //$("#loginbtn").hover(function () {
    //    $(this).stop().animate({
    //        opacity: '1'
    //    }, 600);
    //}, function () {
    //    $(this).stop().animate({
    //        opacity: '0.8'
    //    }, 1000);
    //});
    ////文本框不允许为空---按钮触发
    //$("#loginbtn").on('click', function () {
    //    var txtName = $("#txtName").val();
    //    var txtPwd = $("#txtPwd").val();
    //    if (txtName == "" || txtName == undefined || txtName == null) {
    //        if (txtPwd == "" || txtPwd == undefined || txtPwd == null) {
    //            $(".warning").css({display: 'block'});
    //        }
    //        else {
    //            $("#warn").css({display: 'block'});
    //            $("#warn2").css({display: 'none'});
    //        }
    //    }
    //    else {
    //        if (txtPwd == "" || txtPwd == undefined || txtPwd == null) {
    //            $("#warn").css({display: 'none'});
    //            $(".warn2").css({display: 'block'});
    //        }
    //        else {
    //            $(".warning").css({display: 'none'});
    //        }
    //    }
    //});
    //文本框不允许为空---单个文本触发
    $("#txtName").on('blur', function () {
        var txtName = $("#txtName").val();
        if (txtName == "" || txtName == undefined || txtName == null) {
            $("#warn").css({display: 'block'});
        }
        else {
            $("#warn").css({display: 'none'});
        }
    });
    $("#txtName").on('focus', function () {
        $("#warn").css({display: 'none'});
    });
    //
    $("#txtPwd").on('blur', function () {
        var txtName = $("#txtPwd").val();
        if (txtName == "" || txtName == undefined || txtName == null) {
            $("#warn2").css({display: 'block'});
        }
        else {
            $("#warn2").css({display: 'none'});
        }
    });
    $("#txtPwd").on('focus', function () {
        $("#warn2").css({display: 'none'});
    });
    //关闭
    $(".close_btn").hover(function () {
        $(this).css({color: 'black'})
    }, function () {
        $(this).css({color: '#999'})
    }).on('click', function () {
        $("#LoginBox").fadeOut("fast");
        $("#mask").css({display: 'none'});
    });


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
        $('#login_btn').click(function () {
            var username = $('#login_username').val()
            var password = $('#login_password').val()
            var remember_me = $('#login_remember_me').val()
            var csrf_token = $('#login_csrf_token').val()
            $.post('/auth/login', {
                'username': username,
                'password': password,
                'remrmber_me': remember_me,
                'csrf_token': csrf_token
            }, function (data) {
                if (data == 'true') {
                    window.location.reload()
                }
                else {
                    $('#login_info').show()
                }
            });
        });
    }, 'html')

    $('#register_auth_code').click(function () {
        $('#register_auth_code').attr('src','/auth/authcode?nums='+Math.random())
    });
});
