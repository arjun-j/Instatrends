var lat,longitude;
lat=35.775445;
longitude=-78.687043;


var myCenter=new google.maps.LatLng(lat,longitude);
var marker;
function initialize() {
  var mapProp = {
    center:myCenter,
    zoom:15,
    mapTypeId:google.maps.MapTypeId.ROADMAP
  };
  var map=new google.maps.Map(document.getElementById("googleMap"),mapProp);

var marker=new google.maps.Marker({
  position:myCenter,
  animation:google.maps.Animation.BOUNCE
  });

marker.setMap(map);
}
google.maps.event.addDomListener(window, 'load', initialize);