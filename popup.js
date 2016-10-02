document.addEventListener('DOMContentLoaded', function() {
  function checkPhrase(){
    var input = document.getElementById("message_text").value;
    console.log(input);
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
    	if (this.readyState == 4 && this.status == 200) {
     		console.log(this.responseText);
    }
  };
  xhttp.open("POST", "http://localhost:5000/analyze", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send("inputtext=slut");
  }


document.getElementById("submitText").addEventListener("click", checkPhrase, false);
});

