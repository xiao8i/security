name = 'id';
value = 'xiao8i';
var todayDate = new Date();
todayDate.setHours(todayDate.getDate() + 7);
document.cookie = name + "=" + value + "; path=/; expires=" + todayDate.toGMTString() + "";
alert(document.cookie)