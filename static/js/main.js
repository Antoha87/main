$(document).ready(function() {

    $('.item_container').on('click', function(e){
        e.preventDefault();
        $('.item_container').each(function(){
            if($(this).hasClass('selected')){
                $(this).removeClass('selected');
            }
        })
        $(this).addClass('selected');
    })

    var liSelected = $('nav .main_menu .popup_menu .popup_menu_table .main_rubrics li');

    liSelected.on('mouseover', function(e){
        e.preventDefault();

        var idLi = $(this).attr("id");

        liSelected.each(function(){
            if($(this).hasClass('selected')){
                $(this).removeClass('selected');
            }
        })

        $('.sub_rubric_container > div').each(function(){
                    $(this).hide();
        });

        $('div.'+idLi).show();

        $(this).addClass('selected');
    })
});
