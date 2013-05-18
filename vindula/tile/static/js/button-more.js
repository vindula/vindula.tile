$j(document).ready(function(){ 
    $j('.letters > li a').click(function(){
        event.preventDefault();
        event.stopPropagation();
        
        $j('.letters > li')
        .each(function(){
            $j(this).removeClass('active');
        });
        $j(this).parent().parent().addClass('active');
    })
});