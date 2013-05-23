
function executaAjax(ctx, b_start){
    var url = ctx.find('input#absolute_url').val(),
        b_size = parseInt(ctx.find('input#b_size').val()),
        params = {};


    if (b_start==null)
        b_start = parseInt(ctx.find('input#b_start').val())

    params['b_size'] = b_size;
    params['b_start'] = b_start;

    ctx.find('#spinner').removeClass('display-none');
    ctx.find('div.row').addClass('display-none');

    $j.ajax({
          url: url,
          data: params,
          dataType: 'GET',
          success: function(data){
                var dom = $j(data);
                // dom.filter('script').each(function(){
                //     var content_script = this.text || this.textContent || this.innerHTML || ''
                //     if (content_script)
                //         $j.eval(content_script);
                //     else
                //         $j.get(this.src, function(data){
                //             $j.eval(data);
                //         })
                // });
                var content = dom.find('div#tile-listagem-horizontal-two-columns').contents();
                ctx.html(content);
            },
        });
}


//TODO: Criar um arquivo javacript para uma navegacao por ajax GENERICA, atualmente eh preciso criar um arquivo js para cada navegacao por ajax (news, biblioteca e servicos)
$j(document).ready(function(){
    $j('div#cycle-next, div#cycle-prev').live('click',function(){
        var $conteiner = $j(this).parents('div').find('#tile-listagem-horizontal-two-columns'),
            b_start = parseInt($j(this).find('input').val());
        executaAjax($conteiner,b_start);
    });

});