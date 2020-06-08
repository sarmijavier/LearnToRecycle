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

var provider = new firebase.auth.GoogleAuthProvider();
var providerfb = new firebase.auth.FacebookAuthProvider();
var providertw = new firebase.auth.GithubAuthProvider();

$("#google").click(function () {
  firebase
    .auth()
    .signInWithPopup(provider)
    .then(function (result) {
      console.log(result.user);
      guardarDatos(result.user);
    });
});

$("#face").click(function () {
  firebase
    .auth()
    .signInWithPopup(providerfb)
    .then(function (result) {
      console.log(result.user);
      guardarDatos(result.user);
    });
});

$("#github").click(function () {
  firebase
    .auth()
    .signInWithPopup(providertw)
    .then(function (result) {
      console.log(result.user);
      guardarDatos(result.user);
    });
});

function guardarDatos(user) {
  console.log(user);
  var usuario = {
    uid: user.uid,
    nombre: user.displayName,
    email: user.email,
    foto: user.photoURL,
  };
  firebase
    .database()
    .ref("usuarios/" + user.uid)
    .set(usuario);
  document.getElementById("enviar").style.display = "block";
  localStorage.setItem("usuario", JSON.stringify(usuario));
}
