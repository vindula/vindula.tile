$j(document).ready(function(){ 
    
    $j('.icon-moreaccess > a').click(function(){
        event.preventDefault();
        event.stopPropagation();
        
        $j(this).parent().find('.box-more-items').toggleClass('active');
    });
    
    $j('.letters > li > a').click(function(){
        event.preventDefault();
        event.stopPropagation();
        $j('.letters > li')
        .each(function(){
            $j(this).removeClass('active');
        });
        $j(this).addClass('active');
    })

});