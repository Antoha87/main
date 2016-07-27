jQuery('body').on('click', '.add-to-compare-link', function(){
            var add_url = jQuery(this).attr('data-add');
            var del_url = jQuery(this).attr('data-del');
            var compare = jQuery(this);
            if(jQuery(this).hasClass('add')){
                jQuery.ajax({
                    url: add_url,
                    success: function(data){
                        if(data.success){
                            compare.removeClass('add').addClass('del').text('Удалить сравнение');
                        }
                    }
                });
            }

            if(jQuery(this).hasClass('del')){
                jQuery.ajax({
                    url: del_url,
                    success: function(data){
                        if(data.success){
                            compare.removeClass('del').addClass('add').text('Добавить в сравнение');
                        }
                    }
                });
            }
        })