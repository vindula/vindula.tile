$j(function () {

    var config_global = { placeholder: "placeholder",
                          forcePlaceholderSize: true,
                          items: '.item-tile',
                          handle: ".moveTileLink",
                          // cancel:'div',
                          cursor: "move",
                          update: function(event, ui) {
                                    var list_tiles = $j(this).sortable('toArray'),
                                        base_url = $j('base').val() + '/sortable-view'
                                        context_UID = $j('#context_UID').val();


                                    $j.post(base_url,{'list_tiles': list_tiles,
                                                      'context_UID': context_UID
                                                      },function(data){
                                                          console.log(data);
                                    });

                                    console.log(list_tiles);


                                  }
                        };


    // $j("#content .cleft").sortable($j.extend(config_global, {
    //   connectWith: "#content > div,  #content .cright",
    // })).disableSelection();      

    // $j("#content .cright").sortable($j.extend(config_global, {
    //   connectWith: "#content > div, #content .cleft",
    // })).disableSelection();


     $j("#content > div").sortable($j.extend(config_global, {
      // connectWith: "#content .cleft, #content .cright",

    })).disableSelection();








});