$j(document).ready(function(){
    
    $j('.tile-section-container section .title').click(function(event){
        event.preventDefault();
        event.stopPropagation();
        
        $j(this).parent().toggleClass('active');
    });
    
});