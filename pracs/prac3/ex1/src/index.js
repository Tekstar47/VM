
function parseAndCreatePage(rsp) {
    let s = "";
   
    s = "total number is: " + rsp.photos.photo.length + "<br/>";

    // http://farm{farm-id}.static.flickr.com/{server-id}/{id}_{secret}_[mstb].jpg
    // http://www.flickr.com/photos/{user-id}/{photo-id}

    for (let i=0; i < rsp.photos.photo.length; i++) {
        photo = rsp.photos.photo[i];
        t_url = "http://farm" + photo.farm + ".static.flickr.com/" + photo.server + "/" + photo.id + "_" + photo.secret + "_" + "t.jpg";
        p_url = "http://www.flickr.com/photos/" + photo.owner + "/" + photo.id;
        s +=  '<a href="' + p_url + '">' + '<img alt="'+ photo.title + '"src="' + t_url + '"/>' + '</a>';
    }
    
    const appDiv = document.getElementById("app"); 
    appDiv.innerHTML = s; 
} 

const base = "https://api.flickr.com/services/rest/?";
const query = "&method=flickr.photos.search&api_key=84b84729e56df8291d37b309ef5a5812&tags=golden-retriever&per-page=50&format=json&nojsoncallback=1";
const url = base + query; 

fetch(url) 
    .then( (response) => {
        if (response.ok) {
            return response.json();
        }
        throw new Error("Network response was not ok.");
    })
    .then( (rsp) => parseAndCreatePage(rsp))
    .catch(function(error) {
        console.log("There has been a problem with your fetch operation: ",error.message);
    });

