const image_input = document.getElementById("input_image");

var uploaded_image = "";
image_input.addEventListener("change", function () {
  console.log(image_input.value);
  alert(image_input.value);
});
