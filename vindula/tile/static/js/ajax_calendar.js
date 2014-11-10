$j(document).ready(function(){
    
    $j('.ajax_calendar .top-title a').click(function(ev){
        ev.preventDefault();
        ev.stopPropagation();
        
        var url = this.href,
            ctx = $j(this).parents('.ajax_calendar'),
            id_ele = ctx.attr('id');

        $j.get(url, function(data){
            var string_element = '#content-core ' + id_ele + '.ajax_calendar';

            var dom = $j(data),
                contents = dom.find(string_element + ' .content-calendar').contents(),
                title = dom.find(string_element + ' .top-title span').text(),
                prev = dom.find(string_element + ' .calendarPrevious').attr('href'),
                next = dom.find(string_element + ' .calendarNext').attr('href');
            
            $j('.content-calendar', ctx).html(contents);
            $j('.top-title span', ctx).text(title);
            $j('.calendarPrevious', ctx).attr('href', prev);
            $j('.calendarNext', ctx).attr('href', next);
        })
          
    })
        
});