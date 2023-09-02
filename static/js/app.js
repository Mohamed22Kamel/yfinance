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

const image_input = document.getElementById("input_image");

var uploaded_image = "";
image_input.addEventListener("change", function () {
  console.log(image_input.value);
  alert(image_input.value);
});
