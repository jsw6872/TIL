$("span[class='search-img'],input[class='searchbar']").mousemove(function () {
    $('span.search-img').css('backgroundColor', 'white');
    $('input.searchbar').css('backgroundColor', 'white');
    $("span[class='search-img'],input[class='searchbar']").css('cursor', 'Text');
});
$("span[class='search-img'],input[class='searchbar']").mouseout(function () { 
    $('span.search-img').css('backgroundColor', '');
    $('input.searchbar').css('backgroundColor', '');
});

$('#head-btn-1').click(function() { 
    $('.main-contents').append(`<div class="main-contents-list">
    <div class="input-check-button">
        <!-- div에 마우스 올리면 체크박스 보이기  -->
        <input type="checkbox" class="checkbox">
    </div>
    
    <div class="main-icons">
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20"  fill="rgb(255,185,0)" class="bi bi-folder-fill" viewBox="0 0 16 16">
            <path d="M9.828 3h3.982a2 2 0 0 1 1.992 2.181l-.637 7A2 2 0 0 1 13.174 14H2.825a2 2 0 0 1-1.991-1.819l-.637-7a1.99 1.99 0 0 1 .342-1.31L.5 3a2 2 0 0 1 2-2h3.672a2 2 0 0 1 1.414.586l.828.828A2 2 0 0 0 9.828 3zm-8.322.12C1.72 3.042 1.95 3 2.19 3h5.396l-.707-.707A1 1 0 0 0 6.172 2H2.5a1 1 0 0 0-1 .981l.006.139z"/>
          </svg>
    </div>

    <div class="main-name">
        문서
    </div>


    <div class="main-date">
        <span class="main-date-font" style="font-size: 13px;">2022년 01월 23일</span>
    </div>

    <div class="main-size">
        <span style="font-size: 13px;">10</span>
    </div>

</div>`)
});

// 전체 체크
$("#allcheck").click(function(){
    $.map($("input[type=checkbox]"), function(n){
        return $(".checkbox").attr("checked", true);
        });
        if($("#allcheck").prop("checked")) {
            $("input[type=checkbox]").prop("checked",true);
            $('.main-contents-list').css('backgroundColor', '#e1dfdd');
        }
        else
        {
            $("input[type=checkbox]").prop("checked",false);
            $('.main-contents-list').css('backgroundColor', '');
        }
});

// 전체 체크
// $("#allcheck").click(function(){
    // if($(this).is(":checked")){ //대상이 체크 되어 있을 때
    	//모든 체크박스 체크
//         $(".checkbox").attr("checked", true);
//         console.log('c',$(".checkbox").attr("checked"));
//         $('.main-contents-list').css('backgroundColor', '#e1dfdd');
        
//     }else if ($(".checkbox").is(':checked').length<4) {
//         $(this).attr('checked',unchecked);
//     } else{ //대상이 체크 해제 되어 있을 때
//         $(".checkbox").attr("checked", false);
//     	//모든 체크박스 체크해제
//         console.log($(".checkbox").attr("checked"));
//         $('.main-contents-list').css('backgroundColor', '');
//     }
// });


// 하나씩 체크
$('.checkbox').click(function(){
    if($(this).is(':checked')){
        var main_list = $(this).parent().parent();        
        $(this).attr('checked', true);
        main_list.css('backgroundColor', '#e1dfdd');
    } else{
        $('.checkbox').attr('checked', false);
        console.log('u',$(this).attr("checked"));
        var main_list = $(this).parent().parent();
        main_list.css('backgroundColor', '');
    }
});

// 삭제
$('#head-btn-3').click(function () {
    if($('.checkbox').is(':checked')){
        var remove_list = $('.checkbox').parent().parent().remove();
        remove_list.remove()
    }
});

