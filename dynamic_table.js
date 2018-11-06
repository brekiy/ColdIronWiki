function grabJSON(filepath) {
    // access the JSON from the Codex repository
    var url = "https://xiaohuynh.github.io/Codex/" + filepath;
    var Httpreq = new XMLHttpRequest();
    Httpreq.open("GET", url);
    Httpreq.send(null);
    /*if (Httpreq.responseType == 404) {
        alert("JSON file not found! :(");
    }*/ //incorrect
    var json_obj;
    Httpreq.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            json_obj = JSON.parse(Httpreq.responseText);
            // debug
            console.log(json_obj);
            makeTableFromJSON(json_obj);
        } else if (this.status == 404) {
            alert("JSON file not found, recheck the filepath :(");
        }
    }
}

function makeTableFromJSON(json_obj) {

    // grab the table display element and set up for the table
    var table_display = document.getElementsByTagName("table_display");
    var table = document.createElement("table");
    var table_body = document.createElement("tbody");

    // get the number of rows and columns we have
    var rows = json_obj.length;
    if (rows < 1) {
        alert("Retrieved an empty JSON object! :(");
    }
    // var cols = json_obj[0].length; // incorrect
    var cols = Object.keys(json_obj[0]).length;
    // debug
    console.log("ROWS: " + rows + ", COLS: " + cols);
}