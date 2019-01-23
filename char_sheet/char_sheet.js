function hideOtherDivs(name) {
  var divs = ['core-bits', 'specializations', 'posessions', 'biography'];
  var x = document.getElementById(name);
  for (var i = 0; i < divs.length; i++) {
    console.log(divs[i] + ' ' + i);
    if (x.id !== divs[i]) {
      console.log("didn't match!");
      document.getElementById(divs[i]).style.display = 'none';
    } else {
      console.log("match!");
      document.getElementById(divs[i]).style.display = 'flex';
    }
  }
}

// fills modifiers for the SPAMFIC stats
function modifier(object) {
  var score = object.value;
  score = Math.floor(score/2 - 5);
  var output = document.getElementById(object.id + '-mod');
  if(score >= 0 ) score = '+' + score;
  output.value = score.toString();
}

function weight() {
  var cur_weight = 0;
  for (var i = 1; i <= 26; i++) {
    cur_weight += parseFloat(document.getElementById('inv-' + i + '-weight').value);
  }
  // add the weight of our money
  cur_weight += (parseInt(document.getElementById('1-note').value) + parseInt(document.getElementById('10-note').value) + parseInt(document.getElementById('50-note').value) + parseInt(document.getElementById('100-note').value)) / 100;
  document.getElementById('inv-weight').value = cur_weight.toFixed(2);
}

function wealth() {
  // update wealth
  document.getElementById('cur-wealth').value = 
    parseInt(document.getElementById('1-note').value) 
    + 10 * parseInt(document.getElementById('10-note').value) 
    + 50 * parseInt(document.getElementById('50-note').value) 
    + 100 * parseInt(document.getElementById('100-note').value);
}

// fills modifiers for the skills, action points, willpower, wounds, and encumbrance
function calculate() {
  var skills = {
    'acrobatics': ['agi', 'mgt'],
    'alchemy': ['int'],
    'athletics': ['mgt', 'for'],
    'coercion': ['chr'],
    'deception': ['chr'],
    'investigation': ['int', 'per'],
    'lore': ['int'],
    'medicine': ['int'],
    'observation': ['per'],
    'sabotage': ['int'],
    'sneak': ['agi'],
    'survival': ['for', 'int']
  };

  var spamfic_mods = {
    'spr': parseInt(document.getElementById('spirit-mod').value),
    'per': parseInt(document.getElementById('perception-mod').value),
    'agi': parseInt(document.getElementById('agility-mod').value),
    'mgt': parseInt(document.getElementById('might-mod').value),
    'for': parseInt(document.getElementById('fortitude-mod').value),
    'int': parseInt(document.getElementById('intelligence-mod').value),
    'chr': parseInt(document.getElementById('charisma-mod').value),
  };

  var spamfic = {
    'spr': parseInt(document.getElementById('spirit').value),
    'per': parseInt(document.getElementById('perception').value),
    'agi': parseInt(document.getElementById('agility').value),
    'mgt': parseInt(document.getElementById('might').value),
    'for': parseInt(document.getElementById('fortitude').value),
    'int': parseInt(document.getElementById('intelligence').value),
    'chr': parseInt(document.getElementById('charisma').value),
  };
  // fill skill modifiers
  for (var skill in skills) {
    relevant_stats = skills[skill];
    var mod = -99999;
    for(var stat in relevant_stats){
      var key = relevant_stats[stat];
      if(spamfic_mods[key] > mod) mod = spamfic_mods[key];
    }
    var isSkilled = document.getElementById(skill + '-skilled').checked;
    var isExpert = document.getElementById(skill + '-expert').checked;
    if (isSkilled) mod += 4;
    else if (isExpert) mod += 6;
    var output = document.getElementById(skill + '-mod');
    if (mod >= 0) mod = '+' + mod;
    output.value = mod.toString();
  }
  // fill secondary derived stats
  var ap = document.getElementById('action-points');
  ap.value = Math.floor(spamfic['per']/4) + Math.floor(spamfic['agi']/1.5);
  var wp = document.getElementById('willpower');
  wp.value = Math.floor(spamfic['spr']) + Math.floor(spamfic['chr']/4);
  var guard = document.getElementById('guard');
  guard.value = Math.floor(spamfic['per']/2.5) + Math.floor(spamfic['agi']/2);
  var wounded = document.getElementById('wounded');
  wounded.value = spamfic['for'];
  var very_wounded = document.getElementById('very-wounded');
  very_wounded.value = 2*spamfic['for'] + Math.floor(spamfic['mgt']/2);
  var dead = document.getElementById('dead');
  dead.value = 3*spamfic['for'] + spamfic['mgt'];
  var encumbered = document.getElementById('encumbered');
  encumbered.value = Math.floor(1.5*spamfic['mgt']);
  var very_encumbered = document.getElementById('very-encumbered');
  very_encumbered.value = Math.floor(2.5*spamfic['mgt']);
  var over_encumbered = document.getElementById('over-encumbered');
  over_encumbered.value = 3*spamfic['mgt'];
}

// downloads the character sheet as a JSON object
function download(){
  var fields = document.querySelectorAll('.sheet');
  var data = {};
  for (var i = 0; i < fields.length; i++) {
    var field = fields[i];
    if (field.type === 'radio'){
      data[field.id] = field.checked;
    } else {
      data[field.id] = field.value;
    }
  }
  var filename = 'undefined'
  if(data['name'].length > 0) filename = data['name'];
  data = JSON.stringify(data, null, 2);
  var file = document.createElement('a');
  file.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(data));
  file.setAttribute('download', filename + '.json');
  file.style.display = 'none';
  document.body.appendChild(file);
  file.click();
  document.body.removeChild(file);
}

// prompts client for a json of their character to upload
function upload() {
  var file = document.getElementById('fileupload').files;
  if (file.length) {
    file = file[0];
    var reader = new FileReader();
    reader.onload = function(event) {
      try {
        var text = reader.result;
        data = JSON.parse(text);
        for (var key in data) {
          var field = document.getElementById(key);
          if (field) {
            //look this over
            if (field.type == 'radio')
              field.checked = Boolean(data[key]);
            else {
              field.value = data[key];
            }
          }
        }
      } catch (err) {
        alert(err);
      }
    }
    reader.readAsText(file);
  } else {
    alert('Select a file to upload.');
  }
  calculate();
}