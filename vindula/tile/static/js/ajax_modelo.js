$j = jQuery.noConflict();

$j(document).ready(function(){
    $j('.delete-modelo').live('click', function(ev){
        ev.preventDefault();
        ev.stopPropagation();
        
        if (confirm('Realmente deseja remover esse modelo?')) {
            var $super_this = $j(this),
                id_model = $super_this.attr('data-id_model'),
                url = this.href;
                
            if(id_model.length) {
                $j.ajax({   
                    type: "GET",
                    url: url,
                    data: {'id_model': id_model},
                    success: function(data){
                        if(data.status){
                            $item_ele = $super_this.parents('.item_lista');
                            $item_ele.hide();
                        }else{
                            alert('Não foi possível remover o modelo.');
                            return false;
                        }
                    }
                });
            }else {
                alert('Não foi possível remover o modelo.'); 
                return false;
            }
        }
        
        return false;
    });
});
