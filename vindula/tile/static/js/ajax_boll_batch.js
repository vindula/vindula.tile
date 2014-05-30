function executaAjaxTile(ctx, b_start){
    var url = ctx.find('input#absolute_url').val(),
        b_size = parseInt(ctx.find('input#b_size').val()),
        params = {},
        ctx_id = "#"+ctx.attr('id');
    
    if (!url)
		url = ctx[0].getElementsByClassName("absolute_url")[0].value;
    
    if (!b_size)
    	b_size = ctx[0].getElementsByClassName("b_size")[0].value;

    if (b_start==null)
        b_start = parseInt(ctx.find('input#b_start').val())

    params['b_size'] = b_size;
    params['b_start'] = b_start;

    params['ajax_load'] = true;

    ctx.find('.spinner').removeClass('display-none');
    ctx.find('div.lista-news').addClass('display-none');

    $j.ajax({
          url: url,
          data: params,
          dataType: 'GET',
          success: function(data){
                var dom = $j(data);
                if (dom.find('.social-box').length){
                    dom.find('.social-box').vindula(null, {user_token: window.token});    
                }
                var content = dom.find(ctx_id).contents();
                
                ctx.html(content);
            },
        });
}


//TODO: Criar um arquivo javacript para uma navegacao por ajax GENERICA, atualmente eh preciso criar um arquivo js para cada navegacao por ajax (news, biblioteca e servicos)
$j(document).ready(function(){
    $j('.list_tile div#cycle-next, .list_tile div#cycle-prev').live('click',function(){
        var $conteiner = $j(this).parents('div.list_tile'),
            b_start = parseInt($j(this).find('input').val());
        executaAjaxTile($conteiner,b_start);
    });
});