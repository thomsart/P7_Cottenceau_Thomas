var answers = document.getElementById("answers");

function divMaker(div, value, class_name){
    div.innerHTML = value;
    div.className = class_name;
    answers.appendChild(div);
}

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



        initMap(response[1], response[0]);

    })
});


let map;
let service;
let infowindow;

function initMap(data, wikidata) {

    const paris = new google.maps.LatLng(48.85341, 2.3488);
    infowindow = new google.maps.InfoWindow();
    map = new google.maps.Map(document.getElementById("map"), {
        center: paris,
        zoom: 15,
    });

    const request = {
        query : data,
        fields: ["name", "geometry", "formatted_address"],
    };

    service = new google.maps.places.PlacesService(map);
    service.findPlaceFromQuery(request, (results, status) => {
        if (status === google.maps.places.PlacesServiceStatus.OK) {
            for (let i = 0; i < results.length; i++) {
                createMarker(results[i]);
            }
            map.setCenter(results[0].geometry.location);
            var address = results[0].formatted_address;
        }
        var place = document.getElementById("userText").value;
        var questionDiv = document.createElement("div");
        var answerDiv = document.createElement("div");
        var addressDiv = document.createElement("div");

        divMaker(questionDiv, place, "question_div");
        divMaker(addressDiv, address, "address_div");
        divMaker(answerDiv, wikidata, "answer_div");

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
