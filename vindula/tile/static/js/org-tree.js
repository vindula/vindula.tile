$j(document).ready(function(){
    $j('.container-tree .tree-item.arrow div.content').click(function(ev){
        ev.preventDefault();
        ev.stopPropagation();
        var $li = $j(this).parent();
        
        if ($li.hasClass('arrow'))
            $li.toggleClass('open');
    });
});