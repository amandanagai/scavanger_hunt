    $(function(){
      var $submitSearch = $('.submitSearch');
      var $userId = $('#user_id').val();
      var $huntId = $('#hunt_id').val();
      var markers = [];
      var map;

      function initMap(lat, lng) {
        map = new google.maps.Map(document.getElementById('map'), {
          zoom: 15,
          center: {lat: lat, lng: lng}
        });
      }

      $.ajax({
        method: 'get',
        url: `/users/${$userId}/hunts/${$huntId}/locations/`,   
        beforeSend: function (xhr) {
            xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");
        }       
      })
      .then(function(res){
        var hunt_midpoint = Math.floor(res.length/2)  
        var params = hunt_midpoint ? [res[hunt_midpoint][0], res[hunt_midpoint][1]] : [37.769, -122.446]
        initMap(...params);
        if (res) {
          setMapOnAll(map, res);
        }

        function setMapOnAll(map, res) {
          for (let i = 0; i < res.length; i++) {
            var newMarkerCoords = {lat: res[i][0], lng: res[i][1]};
            var newMarker = new google.maps.Marker({
              position: newMarkerCoords,
              map: map,
              huntLocationId: res[i][3],
              label: `#${res[i][2]}`
            });
            markers.push(newMarker)
          }
        }
        for (let j = 0; j < markers.length; j++) {    
          markers[j].addListener('dblclick', function(e){
            this.setMap(null);
            markers = markers.filter(function(marker) {
              return marker.huntLocationId !== this.huntLocationId;
            });
            // e.preventDefault();
            $.ajax({
              method: 'post',
              url: `/users/${$userId}/hunts/${$huntId}/locations/delete?_method=DELETE`, 
              data: {
                lat: this.position.lat(),
                lng: this.position.lng(),
                huntLocationId: this.huntLocationId
              }
            })
          });
        }

      })

      $submitSearch.on("click", function(e){
        e.preventDefault();
        var $place = $('.place').val();
      
      $.ajax({
          method: 'post',
          url: `/users/${$userId}/hunts/${$huntId}/locations/geocode`,   
          data: {
              place: $place
          },
          headers: {
              "X-Requested-With": "XMLHttpRequest"        
          }
        })
      .then(function(res){
        var newPlace = {lat: res[0], lng: res[1]};
        var search = res[2];
        createMarker(newPlace, map);
        $('#hints_form').css({ "display": 'block'});
        $('#search_form').css({ "display": 'none'});
        $('#search_form').append() // ADD MARKER ID TO FORM


        function createMarker(newPlace, map) {
          var marker = new google.maps.Marker({
            map: map,
            position: newPlace,
          });

          var infoWindow = new google.maps.InfoWindow({
            content: `${search}: click to add location to hunt`
          });

          infoWindow.open(map, marker);
          // marker.addListener('mouseover', function() {
          //   infoWindow.open(map, marker);
          // });
            
          marker.addListener('click', function(e){
              // e.preventDefault();
              $.ajax({
                method: 'post',
                url: `/users/${$userId}/hunts/${$huntId}/locations/`,    
                data: {
                  lat: newPlace['lat'],
                  lng: newPlace['lng'],
                  place: search
                }
              })
              .then(function(res){ 
                  var added = new google.maps.Marker({
                    map: map,
                    position: newPlace,
                    label: `#${res[3]}`
                  });
              })
          });
          infoWindow.addListener('click', function(e){
              // e.preventDefault();
              $.ajax({
                method: 'post',
                url: `/users/${$userId}/hunts/${$huntId}/locations/`,    
                data: {
                  lat: newPlace['lat'],
                  lng: newPlace['lng'],
                  place: search
                }
              })
              .then(function(res){ 
                  var added = new google.maps.Marker({
                    map: map,
                    position: newPlace,
                    label: `#${res[3]}`
                  });
              })
          });        
        }

        });
        })
    })