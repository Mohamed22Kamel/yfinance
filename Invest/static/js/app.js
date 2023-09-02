const submit = document.getElementById("send-m");
submit.addEventListener("click", function (event) {
  message = document.getElementById("chat-value").value;

  const para = document.createElement("p");
  para.style.cssText = "color: navy;";
  const node = document.createTextNode(message);
  para.appendChild(node);
  const element = document.getElementById("chat-answer");
  element.appendChild(para);
});
