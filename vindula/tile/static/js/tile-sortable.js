$j(function () {

    var config_global = { placeholder: "placeholder",
                          forcePlaceholderSize: true,
                          items: '.item-tile',
                          handle: ".moveTileLink",
                          // cancel:'div',
                          cursor: "move",
                          update: function(event, ui) {
                                    var mod_list_tiles = [],
                                        list_tiles = $j(this).sortable('toArray', {attribute:'data-name'}),
                                        base_url = $j('base').val() + '/sortable-view',
                                        context_UID = $j('#context_UID', $j(this)).val();


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
                                                      'context_UID': context_UID
                                                      },function(data){
                                                          console.log(data);
                                    });

                                    // console.log(list_tiles);
                                    // console.log(mod_list_tiles);


                                  }
                        };


    // $j("#content .cleft").sortable($j.extend(config_global, {
    //   connectWith: "#content > div,  #content .cright",
    // })).disableSelection();      

    


    $j("#content > div").sortable($j.extend(config_global, {
        // connectWith: ".tileportletWrapper",

    })).disableSelection();

    $j(".tileportletWrapper").sortable($j.extend(config_global, {

        // connectWith: "#content > div",
    })).disableSelection();








});