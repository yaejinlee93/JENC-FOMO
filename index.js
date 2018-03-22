$(function(context)
{return function()
 {
   $("#catalog").load("/catalog/index.all/" + context.cid + "/")

   $("#previous_page").click(function(){
     previous = Number($('#currentpage').text())-1;
     if (previous > 0)
     {
       $("#catalog").load("/catalog/index.all/" + context.cid + "/" + previous)
       $('#currentpage').html(previous)
     }
   })

   $("#next_page").click(function(){
     next = Number($('#currentpage').text()) + 1
     if (next <= context.pnum)
     {
       $("#catalog").load("/catalog/index.all/" + context.cid + "/" + next);
       $('#currentpage').html(next);
     }
   })
 }
}
(DMP_CONTEXT.get()));
