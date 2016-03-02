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
    $.get('/auth/login', {is_request_form: true}, function (data) {
        $('#login_panel').append(data)
        $('.login_auth_code_img').attr('src', '/auth/authcode?nums=' + Math.random())
        $('.login_auth_code_img').click(function () {
            $('.login_auth_code_img').attr('src', '/auth/authcode?nums=' + Math.random())
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
                    $('#login_info').text(data['info'])
                    $('#login_info').show()
                }
            }, 'json');
        });
    }, 'html')

    $('#login_view_btn').click(function () {
        var username = $('#login_view_username').val()
        var password = $('#login_view_password').val()
        var verification = $('#login_view_verification').val()
        var remember_me = $('#login_view_remember_me').val()
        var csrf_token = $('#login_view_csrf_token').val()
        var next = $('#login_view_next').val()
        $.post('/auth/login', {
            'username': username,
            'password': password,
            'remrmber_me': remember_me,
            'verification': verification,
            'csrf_token': csrf_token,
            'next': next
        }, function (data) {
            if (data['success']) {
                window.location.replace(data['next'])
            }
            else {
                if (data['show_auth']) {
                    $('.login_auth_code_div').show()
                    $('.login_auth_code_img').attr('src', '/auth/authcode?nums=' + Math.random())
                }
                $('#login_view_info').text(data['info'])
                $('#login_view_info').show()
            }
        }, 'json');


    });


    $('#register_auth_code').click(function () {
        $('#register_auth_code').attr('src', '/auth/authcode?nums=' + Math.random())
    });

    //$(function () {
    //    $('[data-toggle="popover"]').popover()
    //})
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
        var id = $(this).parent().attr('id')
        var a = $(this)
        $.post('/api/collect', {id: id}, function (data) {
            if (data['state']) {
                var collects = $.cookie('collects')
                if (collects != null && collects != '') {
                    collects += ' '
                    collects += id
                }
                else
                    collects = id
                $.cookie('collects', collects, {expires: 7})
                a.find('i').attr('class', 'glyphicon glyphicon-star margin-left-3')
                a.find('span').text(data['count'])
            }
        }, 'json');
    }).css('cursor', 'pointer')
    $('.collect-ctrl').click(function () {
        var id = $(this).attr('id')
        var self = $(this)
        if ($(this).text() == '删除收藏') {
            $.post('/api/del_collect', {id: id}, function (data) {
                if (data['state']) {
                    self.text('重新收藏')
                    self.css('color', 'dodgerblue')
                }
            }, 'json')
        }
        else {
            $.post('/api/collect', {id: id}, function (data) {
                if (data['state']) {
                    self.text('删除收藏')
                    self.css('color', 'orangered')
                }
            }, 'json')
        }
    });

    //头像

    var jcrop_api,
        boundx,
        boundy,

        $preview = $('#preview-pane'),
        $pcnt = $('#preview-pane .preview-container'),
        $pimg = $('#preview-pane .preview-container img'),

        xsize = $pcnt.width(),
        ysize = $pcnt.height();

    var avatar_css
    //var select
    $('#avatar-img').Jcrop({
        onChange: updatePreview,
        onSelect: updatePreview,
        aspectRatio: xsize / ysize
    }, function () {
        // Use the API to get the real image size
        var bounds = this.getBounds();
        boundx = bounds[0];
        boundy = bounds[1];
        // Store the API in the jcrop_api variable
        jcrop_api = this;

        // Move the preview into the jcrop container for css positioning
        $preview.appendTo(jcrop_api.ui.holder);
    });

    function updatePreview(c) {
        if (parseInt(c.w) > 0) {
            var rx = xsize / c.w;
            var ry = ysize / c.h;

            var ax = 200 / c.w
            var ay = 200 / c.h

            avatar_css = {
                width: Math.round(ax * boundx) + 'px',
                height: Math.round(ay * boundy) + 'px',
                marginLeft: '-' + Math.round(ax * c.x) + 'px',
                marginTop: '-' + Math.round(ay * c.y) + 'px'
            }

            $pimg.css({
                width: Math.round(rx * boundx) + 'px',
                height: Math.round(ry * boundy) + 'px',
                marginLeft: '-' + Math.round(rx * c.x) + 'px',
                marginTop: '-' + Math.round(ry * c.y) + 'px'
            });
        }
    };

    $('#avatar-btn-save').click(function () {
        $('#avatar-img-now').css(avatar_css)
        $('#avatart-modal').modal('hide')
        $('#avatar-img-now').attr('src', $('.jcrop-preview').attr('src'))
        select = jcrop_api.tellSelect()
        $('#is_update_avatar').val(true)
        $('#select_x').val(select.x)
        $('#select_y').val(select.y)
        $('#select_x2').val(select.x2)
        $('#select_y2').val(select.y2)
    })


    //回到顶部和二维码
    $(function () {
        var $body = $(document.body);
        ;
        var $bottomTools = $('.bottom_tools');
        var $qrTools = $('.qr_tool');
        var qrImg = $('.qr_img');
        $(window).scroll(function () {
            var scrollHeight = $(document).height();
            var scrollTop = $(window).scrollTop();
            var $footerHeight = $('.page-footer').outerHeight(true);
            var $windowHeight = $(window).innerHeight();
            scrollTop > 50 ? $("#scrollUp").fadeIn(200).css("display", "block") : $("#scrollUp").fadeOut(200);
            $bottomTools.css("bottom", scrollHeight - scrollTop - $footerHeight > $windowHeight ? 40 : $windowHeight + scrollTop + $footerHeight + 40 - scrollHeight);
        });
        $('#scrollUp').click(function (e) {
            e.preventDefault();
            $('html,body').animate({scrollTop: 0});
        });
        $qrTools.hover(function () {
            qrImg.fadeIn();
        }, function () {
            qrImg.fadeOut();
        });
    });
});


//上传头像
$(function () {
    'use strict';
    // Change this to the location of your server-side upload handler:
    var url = window.location.hostname === 'blueimp.github.io' ?
        '//jquery-file-upload.appspot.com/' : 'server/php/';
    $('.avatar-img-file').fileupload({
        url: '/auth/avatar_upload',
        dataType: 'json',
        done: function (e, data) {
            jcrop_api.setImage(data.result['url'])
            $('.jcrop-preview').attr('src', data.result['url'])
        },
    }).prop('disabled', !$.support.fileInput)
        .parent().addClass($.support.fileInput ? undefined : 'disabled');
});
