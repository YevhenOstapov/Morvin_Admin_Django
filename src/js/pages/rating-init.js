/*
  Name: Morvin -  Admin & Dashboard  
Author: Themesdesign
Contact: andzukor@gmail.com
File: Rating Js
*/


$(function () {
    $('input.check').on('change', function () {
        alert('Rating: ' + $(this).val());
    });
    $('.rating-tooltip').rating({
        extendSymbol: function (rate) {
            $(this).tooltip({
                container: 'body',
                placement: 'bottom',
                title: 'Rate ' + rate
            });
        }
    });
    $('.rating-tooltip-manual').rating({
        extendSymbol: function () {
            var title;
            $(this).tooltip({
                container: 'body',
                placement: 'bottom',
                trigger: 'manual',
                title: function () {
                    return title;
                }
            });
            $(this).on('rating.rateenter', function (e, rate) {
                title = rate;
                $(this).tooltip('show');
            })
                .on('rating.rateleave', function () {
                    $(this).tooltip('hide');
                });
        }
    });
    $('.rating').each(function () {
        $('<span class="badge bg-info"></span>')
            .text($(this).val() || '')
            .insertAfter(this);
    });
    $('.rating').on('change', function () {
        $(this).next('.badge').text($(this).val());
    });
});