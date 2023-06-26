/*
  Name: Morvin -  Admin & Dashboard  
Author: Themesdesign
Contact: andzukor@gmail.com
File: Product Filter Js
*/


$(document).ready(function () {

    $("#pricerange").ionRangeSlider({
        skin: "round",
        type: "double",
        grid: true,
        min: 0,
        max: 1000,
        from: 200,
        to: 800,
        prefix: "$"
    });

});