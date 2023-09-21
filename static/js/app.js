const submit = document.getElementById("form1");

submit.addEventListener("submit", function (event) {
  event.preventDefault();
  message = document.getElementById("chat-value").value;
  const para = document.createElement("p");
  para.style.cssText = "color: navy;";
  const node = document.createTextNode(message);
  para.appendChild(node);
  const element = document.getElementById("chat-answer");
  element.appendChild(para);

  fetch("", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({
      csrfmiddlewaretoken: document.querySelector("[name=csrfmiddlewaretoken]")
        .value,
      message: message,
    }),
  });
});
