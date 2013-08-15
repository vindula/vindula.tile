function activeLetters($context){
    $j('ul.letters > li > h6 > a', $context).click(function(){
        event.preventDefault();
        event.stopPropagation();
        
        $j('.letters > li')
        .each(function(){
            $j(this).removeClass('active');
        });
        $j(this).parent().parent().addClass('active');
    });
}

$j(document).ready(function(){ 
    $j('.more-items > a').click(function(){
        event.preventDefault();
        event.stopPropagation();
        
        var $this = $(this);
        
        if($this.next().hasClass('box-more-items')){
            $this.next().toggleClass('active');
        }else{
            var macro_tile = $j(this).parents('#macro-tile');
            var name_macro = macro_tile.find('#macro-name').val();
            var context_url = macro_tile.find('#url-context').val();
            
            $j.ajax({
                type: "GET",
                url: context_url+"/more-items-macro",
                data: {'name_macro': name_macro},
                success: function(data){
                    var $dom = $j(data);
                    var conteiner = $dom.filter('div').toggleClass('active');
                    
                    activeLetters($dom.filter('div'));
                    $this.after($dom.filter('div'));
                    
                }
            });
        }
        
    });
    
});