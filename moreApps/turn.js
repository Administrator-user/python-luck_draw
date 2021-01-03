//设定颜色列表及索引变量
var Arraycolor=new Array("#000000","#ff0000","#00ff00","#0000ff","#ff8800","#88ff00","#ffff00","#00ff88","#0088ff","#00ffff","#8800ff","#ff0088","#ff00ff","#ffffff");
var n=0;
//设置颜色
function turncolors(){
n++;
if (n==(Arraycolor.length-1)) n=0;
document.bgColor = Arraycolor[n];
setTimeout("turncolors()",1);
}
//设置音频音量
var vol = document.getElementById("sound");
function setvol(){
vol.volume = 0.01;
};
turncolors();
setvol();