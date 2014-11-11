$j(document).ready(function(){
    
    $j('.ajax_calendar .top-title span.calendarNext, .ajax_calendar .top-title span.calendarPrevious').click(function(ev){
        ev.preventDefault();
        ev.stopPropagation();
        
        var url = $(this).attr('ajax-link'),
            ctx = $j(this).parents('.ajax_calendar'),
            id_ele = ctx.attr('id');

        $j.get(url, function(data){
            var string_element = '#' + id_ele + '.ajax_calendar';

            var dom = $j(data);

            var main_content = dom.find('#content-core');

            if (main_content.length == 0) {
                main_content = dom.filter('#content-core');
            }


            var contents = main_content.find(string_element + ' .content-calendar').contents(),
                title = main_content.find(string_element + ' .top-title span.month-name').text(),
                prev = main_content.find(string_element + ' .calendarPrevious').attr('ajax-link'),
                next = main_content.find(string_element + ' .calendarNext').attr('ajax-link');
            
            $j('.content-calendar', ctx).html(contents);
            $j('.top-title span.month-name', ctx).text(title);
            $j('.calendarPrevious', ctx).attr('ajax-link', prev);
            $j('.calendarNext', ctx).attr('ajax-link', next);
        })
          
    })
        
});