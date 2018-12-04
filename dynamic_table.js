function grabJSON(filepath) {
    // access the JSON from the Codex directory
    var url = "https://xiaohuynh.github.io/Codex/" + filepath;
    var Httpreq = new XMLHttpRequest();
    Httpreq.open("GET", url);
    Httpreq.send(null);
    var json_obj;
    Httpreq.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            json_obj = JSON.parse(Httpreq.responseText);
            makeTableFromJSON(json_obj);
        } else if (this.status == 404) {
            alert("JSON file not found, recheck the filepath :(");
        }
    }
}

function makeTableFromJSON(json_obj) {
    // grab the table display element and set up for the table
    var table_display = document.getElementById("dynamic_table");
    var table = document.createElement("table");
    var table_body = table.createTBody();
    var table_header = table.createTHead();

    // cleaning the old table is part of setup
    while(table_display.firstChild) {
        table_display.removeChild(table_display.firstChild);
    }

    // get the number of rows and columns we have
    var rows = json_obj.length;
    if (rows < 1) {
        alert("Retrieved an empty JSON object! :(");
    }
    var cols = Object.keys(json_obj[0]).length;
    // console.log("DEBUG -> ROWS: " + rows + ", COLS: " + cols);

    // start some variables outside the loops and reuse them
    var table_row = table_header.insertRow(0); 
    var table_col;
    var json_keys = Object.keys(json_obj[0]);
    // console.log(json_keys);

    // build the header row
    var i = 0;
    json_keys.forEach(function(key) {
        table_col = table_row.insertCell(i);
        table_col.innerHTML = "<b>" + key + "</b>";
        i++;
    })
    
    for (var i=0; i<rows; i++) {
        table_row = table_body.insertRow(i);
        for (var j=0; j<cols; j++) {
            table_col = table_row.insertCell(j);
            table_col.innerHTML = json_obj[i][json_keys[j]];
        }
    }

    table_display.appendChild(table);
}