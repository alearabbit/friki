$(document).ready(function (){
    pusher = new Pusher('dd2181a309fb7773ac46');
    my_channel = pusher.subscribe('presence-kjh-room');
    // 위 줄에서 읽고 + 채널을 구독을 함 (인증하는 경우 presence-XX 형식은 필수)
    my_channel.bind('pusher:subscription_succeeded', function(members){
        console.log('subscription Success!!');
        members.each(function(member){
            $('#user-room').append('<li id=member_'+member.id+'>' + '<a target="_blank" href="http://www.facebook.com/'+member.user_id +'">'+member.info.username +'</a>' + '</li>');
        })

    })
    // 사용자가 로그인해 구독했을 때, 기존 사용자들을 보여줌
    // each는 js에서 사용하나 pusher에서 제공해주는 것. for i in members와 같은 역할.
    my_channel.bind('pusher:member_added', function(member){
        console.log('Member added');
        $('#chat-table').append('<tr><td colspan=2>' + member.info.username + '님이 입장하셨습니다.' + '</td></tr>');
        // $('#chat-room').append('<p>' + '  ' + member.id + '님이 입장하셨습니다.' + '</p>');
        // $('#user-room').append('<p>' + member.id + '</p>');
        $('#user-room').append('<li id=member_'+member.id+'>' + '<a target="_blank" href="http://www.facebook.com/'+member.user_id +'">'+member.info.username +'</a>'+ '</li>');

    })
    // function(member)에서 member는 pusher 서버에서 날려준 jsondata. 이름은 임의 설정한 것.
    // member는 새로 들어온 사용자 1명에 대한 data임. member_added는 pusher에서 정해둔 것.
    // member.id의 id는 py에서 channel_data['user_id'] = username의 id와 동일한 접근
    // member.info.username 여기서 info는 py의 user_info이지만 .info만 써도 접근 가능함
    my_channel.bind('pusher:member_removed', function(member){
        console.log('Member removed');
        $('#member_' + member.id).remove();
        $('#chat-table').append('<tr><td colspan=2>' + member.info.username + '님이 퇴장하셨습니다.' + '</td></tr>');

    })

    my_channel.bind('new_msg', function(data){
        $('#chat-table').append('<tr><td colspan=2><p><strong><a target="_blank" href="http://www.facebook.com/'+data.user_id +'">'+'<img src="http://graph.facebook.com/'+ data.user_id + '/picture"></a>' + '<a target="_blank" href="http://www.facebook.com/'+data.user_id +'">'+ data.username + '</a>'+': </strong>' + data.msg + '</p><small>' + data.time + '</small></td></tr>');
        $('#input-chat').val('');
    // 위 val() 코드는 text입력 후 기존에 입력한 내용을 지움.(빈 박스로)
    })
    $('#chat-button').click(function(){
        $.ajax({
            url: '/send_msg',
            type: 'POST',
            dataType: 'JSON',
            data: {
                msg: $('input[name="input-chat"]').val()
            },
            success: function(data) {
                if(data.success){
                    console.log('send msg success!');
                }
                else{
                    console.log('send msg fail!')
                }
            },
            error: function(data) {
                console.log('Server Error!');
            }
        })
    })
               
})