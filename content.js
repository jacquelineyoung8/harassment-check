// document.addEventListener('DOMContentLoaded', function() {
//   var phrase = "";
//   document.addEventListener("keypress", updatePhrase, false);
// }, false);

var phrase = "";
var timeoutVar;
 // var key = e.key;
 // console.log("before: "+ phrase);
 // phrase += key;
 // console.log("after: "+phrase);
function updatePhrase(e){
  var key = e.key;
  // console.log("before: "+ phrase);
  phrase += key;
	if (timeoutVar) {
		clearTimeout(timeoutVar);
	}
	timeoutVar = setTimeout(function(){
		var xhttp = new XMLHttpRequest();
    	xhttp.onreadystatechange = function() {
    	if (this.readyState == 4 && this.status == 200) {
     		console.log(this.responseText);
    	};
  	};
  xhttp.open("POST", "http://localhost:5000/analyze", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send("inputtext="+phrase);
  }, 500);  

};

// function backspace(e){
//   if (e.keyCode == 8 || e.keyCode == 46){
//     phrase = phrase.slice(0, phrase.length - 1);
//     console.log("phrase is: " + phrase);
//   }
// };

document.addEventListener("keypress", updatePhrase, false);
// document.addEventListener("keydown", backspace, false);


// console.log("----------");
  // var key = e.key;
 // console.log("before: "+ phrase);
  // phrase += key;
 // console.log("after: "+phrase);