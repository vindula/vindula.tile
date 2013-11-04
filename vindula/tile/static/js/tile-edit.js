$j = jQuery.noConflict();

$j(document).ready(function(){

	var common_content_filter = '#content=*,dl.portalMessage.error,dl.portalMessage.info';
    var common_jqt_config = {fixed:false,speed:'fast',mask:{color:'#000',opacity: 0.4,loadSpeed:0,closeSpeed:0}};

    // common_jqt_config['onLoad'] = function (e) {launchCKInstances();
    //                                             $j('#fieldset-global-settings').parent().attr('id','content');
    //                                             };
    // common_jqt_config['onBeforeClose'] = function(e){removeEditor()};

    // Modal Tile portlet
    $j('a.manage-tile').prepOverlay({
        subtype: 'ajax',
        filter: common_content_filter,
        closeselector: '[name=form.button.cancel],[name=form.actions.cancel]',
        formselector: '[name=edit_form]',
        noform:'reload',
        width: '50%',
        config: common_jqt_config
        });

});