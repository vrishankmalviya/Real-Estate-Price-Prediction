function onPageLoad() {
    console.log( "document loaded" );
    var url = "http://127.0.0.1:8000/get_location";  
    $.get(url,function(data, status) {
        console.log("got response for get_location request");
        if(data) {
            var locations = data.locations;
            var uiLocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for(var i in locations) {
                var opt = new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
        }
    });
  }
  