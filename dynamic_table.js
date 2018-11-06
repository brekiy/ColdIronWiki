function makeTableFromJSON(filepath) {
    // access the JSON from the Codex repository
    var url = "https://xiaohuynh.github.io/Codex/" + filepath;
    var Httpreq = new XMLHttpRequest();
    Httpreq.open("GET", url, false);
    Httpreq.send();
    var json_obj = JSON.parse(Httpreq.responseText);
    console.log(json_obj);
}