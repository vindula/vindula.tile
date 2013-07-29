$j(document).ready(function(){
    
    $j('.ajax_calendar .top-title a').click(function(ev){
        ev.preventDefault();
        ev.stopPropagation();
        
        var url = this.href,
            ctx = $j(this).parents('.ajax_calendar');
        
        $j.get(url, function(data){
            var dom = $j(data),
                contents = dom.find('.ajax_calendar .content-calendar').contents(),
                title = dom.find('.ajax_calendar .top-title span').text(),
                prev = dom.find('.ajax_calendar .calendarPrevious').attr('href'),
                next = dom.find('.ajax_calendar .calendarNext').attr('href');
            
            $j('.content-calendar', ctx).html(contents);
            $j('.top-title span', ctx).text(title);
            $j('.calendarPrevious', ctx).attr('href', prev);
            $j('.calendarNext', ctx).attr('href', next);
            
        })
          
    })
        
});