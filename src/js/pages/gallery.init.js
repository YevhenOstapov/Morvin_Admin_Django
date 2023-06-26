/*
  Name: Veltrix - Admin & Dashboard  
Author: Themesbrand
Website: https://themesbrand.com/
Contact: andzukor@gmail.com
File: Rating Js File
*/


$('.gallery-popup').magnificPopup({
    type: 'image',
    closeOnContentClick: true,
    mainClass: 'mfp-fade',
    gallery: {
        enabled: true,
        navigateByImgClick: true,
        preload: [0,1] // Will preload 0 - before current, and 1 after the current image
    }
});