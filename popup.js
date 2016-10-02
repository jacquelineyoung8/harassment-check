document.addEventListener('DOMContentLoaded', function() {
  function checkPhrase(){
    var input = document.getElementById("message_text").value;
    console.log(input);
  }

document.getElementById("submitText").addEventListener("click", checkPhrase, false);
});

