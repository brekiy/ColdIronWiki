var codex_url = 'https://brekiy.github.io/Codex/';

// pulls a specified JSON file and runs another function on the data
function grabJSON(filepath, mode) {
  // access the JSON from the Codex directory
  // i could have done this with jquery, but i wanted to see what building
  // the request looks like in vanilla js
  var url = codex_url + filepath;
  var Httpreq = new XMLHttpRequest();
  Httpreq.open('GET', url);
  Httpreq.send(null);
  var json_obj;
  Httpreq.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      // if the file is ready and successful, do stuff
      // console.log(Httpreq.responseText);
      json_obj = JSON.parse(Httpreq.responseText);
      switch(mode) {
        case 0:
          makeTableFromJSON(json_obj);
          break;
        case 1:
          // searching for creatures
          var keys = ['name', 'category'];
          searchObjectsInJSON(json_obj, keys);
          break;
      }
    } else if (this.status == 404) {
      alert('JSON file not found, recheck the filepath :(');
    }
  }
}

// given a json object, create a table in html and append it to a div
// labeled 'dynamic_table'
function makeTableFromJSON(json_obj) {
  // grab the table display element and set up for the table
  var table_display = document.getElementById('dynamic_table');
  var table = document.createElement('table');
  var table_body = table.createTBody();
  var table_header = table.createTHead();

  // cleaning the old table is part of setup
  while(table_display.firstChild) {
    table_display.removeChild(table_display.firstChild);
  }

  // get the number of rows and columns we have
  var rows = json_obj.length;
  if (rows < 1) {
    alert('Retrieved an empty JSON object! :(');
  }
  var cols = Object.keys(json_obj[0]).length;
  // console.log('DEBUG -> ROWS: ' + rows + ', COLS: ' + cols);

  // start some variables outside the loops and reuse them
  var table_row = table_header.insertRow(0); 
  var table_col;
  var json_keys = Object.keys(json_obj[0]);
  // console.log(json_keys);

  // build the header row
  var i = 0;
  json_keys.forEach(function(key) {
    table_col = table_row.insertCell(i);
    table_col.innerHTML = '<b>' + key + '</b>';
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

// given a json object, search through it for elements that match a search key
// really only used for creatures at the moment, will refactor to be generic later
function searchObjectsInJSON(json_obj, search_keys) {
  var query = document.getElementById('search_bar').value;
  var list_display = document.getElementById('dynamic_list');
  // clear the old list
  while (list_display.firstChild) {
    list_display.removeChild(list_display.firstChild);
  }
  if (query) { 
    // create the fuse object with the keys we want to search for
    console.log('query is not null, searching');
    var fuse = new Fuse(json_obj, { keys: search_keys, threshold: 0.0 });
    // search the json with the query in the search bar
    var results = fuse.search(query);
  } else {
    console.log('query is null, listing everything');
    results = json_obj;
  }
  
  console.dir(results);
  // format the results into html, and append them to our designated div
  // TODO: could make it so another parameter is passed in, so we could have
  // search on multiple divs instead of just 1
  list_display.appendChild(searchResults(results));
}

// given a bunch of json search results, return the HTML markup for them
// really only used for the bestiary at the moment
function searchResults(results) {
  var list = document.createElement('ul');
  for (var elem in results) {
    console.log(elem);
    creature = results[elem];
    console.log(creature);
    var list_node = document.createElement('li');
    //var link_text = document.createTextNode();
    var link = document.createElement('a');
    link.innerHTML = creature.name + ' (' + creature.size + " " + creature.category + ')';
    link.href = codex_url + '/bestiary/' + creature.name + '.html';
    console.log(link);
    list_node.appendChild(link);
    list.appendChild(list_node);
  }
  return list;
}