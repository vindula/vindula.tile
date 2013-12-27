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
                                        list_tiles = $j(this).sortable('toArray', {attribute:'data-name'}),
                                        base_url = $j('base').val() + '/sortable-view',
                                        context_UID = $j('#context_UID', $j(this)).val();
                                    obj_item = ui.item;


                                    for (var i=0;i<list_tiles.length;i++){ 
                                      var item = list_tiles[i],
                                          valor = '',
                                          div_parent_even = $j('[data-name='+item+']', $j(this)).parent('#even'),
                                          div_parent_odd = $j('[data-name='+item+']', $j(this)).parent('#odd');

                                          if (div_parent_even.length){
                                            valor = 'even|'+item;
                                          }else if (div_parent_odd.length){
                                            valor = 'odd|'+item;
                                          }else{
                                            valor = item;
                                          }

                                      mod_list_tiles.push(valor);
                                    }

                                    $j.post(base_url,{'list_tiles': mod_list_tiles,
                                                      'context_UID': context_UID,
                                                      },function(data){

                                                        var msg = data.response.msg,
                                                            UID = data.response.uid,
                                                            data_name = obj_item.attr('data-name'),
                                                            list_data_name = data_name.split('|');

                                                        obj_item.attr('data-name', list_data_name[0]+'|'+list_data_name[1]+'|'+UID);
                                                        console.log(msg);
                                    });

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