function msg(){
    alert("Hai this is first alert...!")
}
setInterval(liveclock,1000);
function liveclock(){
    var time = new Date();
    var hrs = time.getHours();
    var min = time.getMinutes();
    var sec = time.getSeconds();
    if (hrs>12){
        hrs =hrs-12;}
    if (hrs==0){
        hrs=12;}
    document.getElementById('li-cl').innerHTML=hrs+':'+min+':'+sec;
}
liveclock();