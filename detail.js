// $(document).ready(function() {
//   $(".thumbnail").mouseenter( function(){
//     var replacement = $( this ).html();
//     $('#image_viewer').html(replacement);
//   });
// });

$(document).ready(function() {
  $(".mythumbnail").mouseenter( function(){
    var replacement = $( this ).attr('src');
    $('#main_image').attr('src', replacement);
  });
});
