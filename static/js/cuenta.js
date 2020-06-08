var firebaseConfig = {
  apiKey: "AIzaSyCsMmlRB1c_Yhe0o2gSK5JBd7_unqAG_cY",
  authDomain: "learntorecycle-4e853.firebaseapp.com",
  databaseURL: "https://learntorecycle-4e853.firebaseio.com",
  projectId: "learntorecycle-4e853",
  storageBucket: "learntorecycle-4e853.appspot.com",
  messagingSenderId: "121502769795",
  appId: "1:121502769795:web:aea4acf3816a06c9b971b6",
  measurementId: "G-ETLEWRXM1Z",
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
const database = firebase.database();

var userJS = JSON.parse(localStorage.getItem("usuario"));
var ud = userJS.uid;
var user = firebase.database().ref("usuarios/");
var usuario;

user.on("value", function (data) {
  data.forEach(function (element) {
    var use = element.val();
    if (use.uid == ud) {
      usuario = use;
      console.log(use);
    }
  });

  $(".img").append("<img id=imagen src='" + usuario.foto + "'/>");
  $(".campoN").append("<h5 id=nombre>" + usuario.nombre + "</h5>");
  $(".campoE").append("<h5 id=email>" + usuario.email + "</h5>");
});

$("#update").click(function () {
  var uid = usuario.uid;
  var foto = usuario.foto;
  var nombre = document.getElementById("nombre").value;
  var correo = document.getElementById("email").value;

  if (nombre == "" || correo == "") {
    alert("Campos Vacios");
  } else {
    update(uid, foto, nombre, correo);
  }
});

function update(uide, photo, name, correo) {
  var usu = {
    uid: uide,
    nombre: name,
    email: correo,
    foto: photo,
  };
  firebase
    .database()
    .ref("usuarios/" + usu.uid)
    .set(usu);

  localStorage.clear();
  localStorage.setItem("usuario", JSON.stringify(usu));
}

$("#logout").click(function () {
  localStorage.clear();
});

$("#delete").click(function () {
  var id = usuario.uid;
  eliminar(id);
});

function eliminar(id) {
  firebase
    .database()
    .ref("usuarios/" + id)
    .remove();
}
