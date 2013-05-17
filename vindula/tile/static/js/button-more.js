$j(document).ready(function(){ 
    
    $j('.icon-moreaccess a').click(function(){
        event.preventDefault();
        event.stopPropagation();
        
        $j(this).parent().addClas('active');
    });
    
    $j('.letters > li').click(function(){
        event.preventDefault();
        event.stopPropagation();
        
        $j(this).addClas('active');
    })

});