$j(document).ready(function(){ 
    $j('ul.letters > li > h6 > a').click(function(){
        event.preventDefault();
        event.stopPropagation();
        
        $j('.letters > li')
        .each(function(){
            $j(this).removeClass('active');
        });
        $j(this).parent().parent().addClass('active');
    })
});