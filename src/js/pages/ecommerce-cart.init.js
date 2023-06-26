/*
  Name: Morvin -  Admin & Dashboard  
Author: Themesdesign
Contact: andzukor@gmail.com
File: Ecommerce Cart Js
*/

var defaultOptions = {
};

$('[data-toggle="touchspin"]').each(function (idx, obj) {
    var objOptions = $.extend({}, defaultOptions, $(obj).data());
    $(obj).TouchSpin(objOptions);
});