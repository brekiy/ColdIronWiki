function modifier(object) {
  var score = object.value;
  score /= 2;
  score -= 5;
  score = Math.floor(score);
  var output = document.getElementById(object.id + '-mod');
  if(score >= 0 ) score = '+' + score;
  output.value = score.toString();
}

function calculate(){
  var skills = {
    "acrobatics": "agi,mgt",
    "alchemy": "int",
    "athletics": "mgt,for",
    "coercion": "spr,chr",
    "deception": ""
  }
}