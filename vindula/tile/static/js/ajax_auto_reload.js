
function auto_reload(){
	$j('div.auto_reload').each(function(){
		var url_view_reload = $j('input[name="url_auto_reload"]', $j(this)).val()
			$ctx = $j(this),
			$itens = $j("div.content_itens", $ctx),
			$div = $j('<div />'),
			$img = $j('<img />');
		
		$itens.css('height', $ctx.height()+'px');

		$div.css('text-align','center');
		$div.css('float','left');
		$div.css('width','100%');

		$img.attr('src','/vindula-api/static/img/ajax-loader.gif');
		$img.css('height', '30px');
		$img.css('margin', '20px');

		$div.html($img);
		$itens.html($div);

		$j.get(url_view_reload,{'ajax_load':'1'}, function(data){
			var dom = $j(data),
            contents = dom.find('#content-core div.content_itens').contents();
	        $itens.html(contents);    
	        $itens.css('height', '100%');
            
        });
	});

};


$j(document).ready(function(){
	
	var tempo_rotacao = 30000;
	window.setInterval(function(){
		auto_reload();
	},tempo_rotacao);

});