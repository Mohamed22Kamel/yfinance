const submit = document.getElementById("send-m");
submit.addEventListener("click", function (event) {
  message = document.getElementById("chat-value").value;
  alert(message);
});
