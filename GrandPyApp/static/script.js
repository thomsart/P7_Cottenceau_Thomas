function postFormData(url, data){
    // we send the content of the form to the server
    return fetch(url, {
        method: "POST",
        body: data
    })
    .then(response => response.json())
    .catch(error => console.log(error));
}

let userInput = document.querySelector("#question");
userInput.addEventListener("submit", function (event) {
    event.preventDefault();
    postFormData("/ajax", new FormData(userInput))
    .then(response => {
        var answerDiv = document.getElementById("answers");
        answerDiv.innerHTML = response[0];
        initMap(response[1]);
    })
});


let map;
let service;
let infowindow;

function initMap(data) {

    const paris = new google.maps.LatLng(48.85341, 2.3488);
    infowindow = new google.maps.InfoWindow();
    map = new google.maps.Map(document.getElementById("map"), {
        center: paris,
        zoom: 15,
    });

    const request = {
        query : data,
        fields: ["name", "geometry"],
    };

    service = new google.maps.places.PlacesService(map);
    service.findPlaceFromQuery(request, (results, status) => {
        if (status === google.maps.places.PlacesServiceStatus.OK) {
            for (let i = 0; i < results.length; i++) {
                createMarker(results[i]);
            }
            map.setCenter(results[0].geometry.location);
        }
    });

}

function createMarker(place) {
    const marker = new google.maps.Marker({
        map,
        position: place.geometry.location,
    });
    google.maps.event.addListener(marker, "click", () => {
        infowindow.setContent(place.name);
        infowindow.open(map);
    });
}
