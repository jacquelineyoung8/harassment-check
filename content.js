// document.addEventListener('DOMContentLoaded', function() {
//   var phrase = "";
//   document.addEventListener("keypress", updatePhrase, false);
// }, false);

var phrase = "";

function updatePhrase(e){
  console.log("----------");
  var key = e.key;
  console.log("before: "+ phrase);
  phrase += key;
  console.log("after: "+phrase);
};

function backspace(e){
  if (e.keyCode == 8 || e.keyCode == 46){
    phrase = phrase.slice(0, phrase.length - 1);
    console.log("phrase is: " + phrase);
  }
};

document.addEventListener("keypress", updatePhrase, false);
document.addEventListener("keydown", backspace, false);

chrome.runtime.sendMessage({harassing-content: phrase}, function(response) {
  console.log("request sent");
});
