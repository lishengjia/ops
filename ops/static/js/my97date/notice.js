function tips_pop(){
  var MsgPop=document.getElementById("winpop");
  var popH=parseInt(MsgPop.style.height);
   if (popH==0){
   MsgPop.style.display="block";
  show=setInterval("changeH('up')",2);
   }
  else {
   hide=setInterval("changeH('down')",2);
  }
}
function changeH(str) {
 var MsgPop=document.getElementById("winpop");
 var popH=parseInt(MsgPop.style.height);
 if(str=="up"){
  if (popH<=100){
  MsgPop.style.height=(popH+10).toString()+"px";
  }
  else{  
  clearInterval(show);
  }
 }
 if(str=="down"){ 
  if (popH>=4){
  MsgPop.style.height=(popH-4).toString()+"px";
  }
  else{
  clearInterval(hide);
  MsgPop.style.display="none";
  }
 }
}
window.onload=function(){
document.getElementById('winpop').style.height='0px';
setTimeout("tips_pop()",800);
}
