$(document).ready(function(){
	$('.big').bind({
		mouseenter:function(){
			$(".max").show();
			$(".big").addClass("add");
		},
		mouseleave:function(){
			$(".big").removeClass("add");
			$(".max").hide();
		}
	})
});


function showTip2(bg_pic)
{
                if (typeof window.pageYOffset != 'undefined') {
                  scrollPos = window.pageYOffset;
                }
                else if (typeof document.compatMode != 'undefined' &&
                    document.compatMode != 'BackCompat') {
                  scrollPos = document.documentElement.scrollTop;
                }
                else if (typeof document.body != 'undefined') {
                  scrollPos = document.body.scrollTop;
                }

              var div22=document.getElementById(bg_pic);
              div22.style.display="block";
              div22.style.left=event.clientX-15; //鼠标目前在X轴上的位置，加10是为了向右边移动10个px方便看到内容
              div22.style.top=parseInt(event.y)+5+$(document).scrollTop();
              //alert(div22.style.top);
              div22.style.position="absolute"; //必须指定这个属性，否则div1层无法跟着鼠标动
}

function sleep(numberMillis) {
var now = new Date();
var exitTime = now.getTime() + numberMillis;
while (true) {
    now = new Date();
    if (now.getTime() > exitTime)
    return;
   }
}


function closeTip2(bg_pic)
{
    sleep(100);
    var div22=document.getElementById(bg_pic);
    div22.style.display="none";

}