
const box = document.querySelector(".speech_zone");

// we create the loader.
const loader = document.querySelector(".loader");
loader.className += " hidden";

// We select the container named answer to put later our div we create -
// with the function divMaker.
var answers = document.getElementById("answers");

function divMaker(div, value, class_name){
    // we create a function able to makes div in which we'll put the texts
    // we'll get from the API
    div.innerHTML = value;
    div.className = class_name;
    answers.appendChild(div);
    loader.className += " hidden";
}

// This function will be use to post what the user writes in the form.
function postFormData(url, data){
    // we send the content of the form to the server.
    loader.className -= " hidden";
    return fetch(url, {
        method: "POST",
        body: data
    })
    .then(response => response.json())
    .catch(error => console.log(error));
}

// Now we listen the form named question to use the function postFormData -
// that we just create.
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

// Now we use the service to GoogleMap API that allows us to -
// generate a map with the name of the place we parsed from the form.  
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
 
        // We create the div we need to organise our Chat.
        var place = document.getElementById("userText").value;
        var questionDiv = document.createElement("div");
        var answerDiv = document.createElement("div");
        var addressDiv = document.createElement("div");

        // If the user enter nthing or something which return nothing,
        // address will be undefined and in this case there's no reason
        // to create 'questionDiv' and 'addressDiv'.
        if(address === undefined){   
        }else{
            divMaker(questionDiv, place, "question_div");
            divMaker(addressDiv, address, "address_div");
        }
        divMaker(answerDiv, wikidata, "answer_div");
    });
}

//  Always from the GoogleMap API we use the function which create
// a marker i.e. the red logo we see on the map to select the place.
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


// if (results[0] === undefined) {
//     return console.log("ok pd"); 
// }