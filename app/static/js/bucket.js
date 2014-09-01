$(document).ready(function (){
    $('.dropdown-toggle').dropdown() // 드롭다운 작동을 위한 라인 1개

    pusher = new Pusher('dd2181a309fb7773ac46');
    
    my_channel.bind('pusher:member_added', function(member){
        console.log('login 완료');
        $('#hello_msg').append( member.info.username + '님 안녕하세요.' );
    })


    my_channel.bind('new_msg', function(data){
        $('#dropdown').append('<img src="http://graph.facebook.com/'+ data.user_id + '/picture">');

    // 위 val() 코드는 text입력 후 기존에 입력한 내용을 지움.(빈 박스로)
})          
})