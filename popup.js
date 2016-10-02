document.addEventListener('DOMContentLoaded', function() {
 function checkPhrase(){
   var input = document.getElementById("message_text").value;
   //console.log(input);
   var xhttp = new XMLHttpRequest();
   xhttp.onreadystatechange = function() {
       if (this.readyState == 4 && this.status == 200) {
            //console.log(this.responseText);
            document.getElementById('input_text').innerHTML = this.responseText;

   }
 };
 xhttp.open("POST", "http://localhost:5000/analyze", true);
 xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
 xhttp.send("inputtext="+input);
 }


document.getElementById("submitText").addEventListener("click", checkPhrase, false);
});