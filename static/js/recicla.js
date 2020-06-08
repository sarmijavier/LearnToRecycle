function validarExt() {
  var archivoInput = document.getElementById("archivoInput");
  var archivoRuta = archivoInput.value;
  var extPermitidas = /(.mp4|.MP4|.JPG|.jpg|.png|.PNG)$/i;
  if (!extPermitidas.exec(archivoRuta)) {
    alert("Extension no permitida");
    archivoInput.value = "";
    return false;
  } else {
    if (archivoInput.files && archivoInput.files[0]) {
      var visor = new FileReader();
      visor.onload = function (e) {
        document.getElementById("visorArchivo").innerHTML =
          '<embed src="' + e.target.result + '" width="300" height="300">';
      };
      visor.readAsDataURL(archivoInput.files[0]);
    }
  }
}

