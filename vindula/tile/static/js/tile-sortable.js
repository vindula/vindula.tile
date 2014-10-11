
function count_add_tile_list(list_itens,list_return){
  if (list_itens.length){
    for (var i=0;i<list_itens.length;i++){
      var item = list_itens[i];
      list_return.push($j(item).attr('data-name'));
    };
  };
  return list_return;
};


$j(function () {

    var config_global = { placeholder: "placeholder",
                          forcePlaceholderSize: true,
                          forceHelperSize: true,
                          items: '.item-tile',
                          handle: ".moveTileLink",
                          cancel:'.visualClear',
                          cursor: "move",
                          tolerance: 'pointer',
                          opacity: 0.7,
                          scroll: true,
                          revert: true,
                          update: function(event, ui) {
                                    var mod_list_tiles = [],
                                        // list_tiles = $j(this).sortable('toArray', {attribute:'data-name'}),
                                        base_url = $j('base').val() + '/sortable-view',
                                        linhas_tiles = $j('div.linha_tiles',$j(this)),
                                        context_UID = $j('#context_UID', $j(this)).val();
                                         
                                    obj_item = ui.item;

                                    for (var i=0;i<linhas_tiles.length;i++){ 
                                      var item = linhas_tiles[i],
                                          list_tiles = [],
                                          tiles_columns_even = $j('div#even div.item-tile:not(.column-empty)', $j(item)),
                                          tiles_columns_middle = $j('div#middle div.item-tile:not(.column-empty)', $j(item)),
                                          tiles_columns_odd = $j('div#odd div.item-tile:not(.column-empty)', $j(item));
                                          tiles_columns_full = $j('div#full div.item-tile:not(.column-empty)', $j(item));

                                          list_tiles = count_add_tile_list(tiles_columns_even,list_tiles);
                                          list_tiles = count_add_tile_list(tiles_columns_middle,list_tiles);
                                          list_tiles = count_add_tile_list(tiles_columns_odd,list_tiles);
                                          list_tiles = count_add_tile_list(tiles_columns_full,list_tiles);

                                      mod_list_tiles.push(list_tiles);
                                    };

                                    var data_request = JSON.stringify({'list_tiles': mod_list_tiles,'context_UID': context_UID})
                                    $j.post(base_url,{'data':data_request},function(data){
                                                        var msg = data.response.msg,
                                                            UID = data.response.uid,
                                                            data_name = obj_item.attr('data-name'),
                                                            list_data_name = data_name.split('|');

                                                        obj_item.attr('data-name', list_data_name[0]+'|'+list_data_name[1]+'|'+UID);
                                                        console.log(msg);
                                                      },'json'
                                    );

                                    //Adição da Class 'portletWrapper' ao tile se ele foi
                                    // movido do meio para a esquerda
                                    var tile_portle = ui.item.parents('.tileportletWrapper');
                                    if (tile_portle.length){
                                      ui.item.addClass('portletWrapper');
                                      ui.item.css('float','left');
                                      ui.item.after("<div class='visualClear'></div>");

                                    }
                                    //remoção da Class 'portletWrapper' ao tile se ele foi
                                    // movido da esquerda para o meio
                                    var tile_portle = ui.item.parents('#content');
                                    if (tile_portle.length){
                                      ui.item.removeClass('portletWrapper');
                                      ui.item.css('float','');
                                    }                                   
                                   
                                    console.log(mod_list_tiles);

                          },
                          start: function(e, ui){
                              ui.placeholder.height(ui.item.height());
                          },

                        };

    $j("#content .sortable-tiles").sortable($j.extend(config_global, {
        connectWith: ".tileportletWrapper, #content .sortable-tiles",

    })).disableSelection();

    $j(".tileportletWrapper").sortable($j.extend(config_global, {

        connectWith: "#content .sortable-tiles, .tileportletWrapper",
    })).disableSelection();

});