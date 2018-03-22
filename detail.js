$(document).ready(function()
{
  $(".smallsrc").mouseenter(function()
  {
    var want = $(this).html();
    $(".mainpic").html(want);
  });
});
