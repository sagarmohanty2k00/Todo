 // Your web app's Firebase configuration
 var firebaseConfig = {
    apiKey: "AIzaSyDCcNMSgm8uy2vTEZfjBYzWNtmAbg7LqjE",
    authDomain: "todo-72de0.firebaseapp.com",
    databaseURL: "https://todo-72de0.firebaseio.com",
    projectId: "todo-72de0",
    storageBucket: "todo-72de0.appspot.com",
    messagingSenderId: "1032354726639",
    appId: "1:1032354726639:web:c6a9685c06c77af722911a"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);

  const auth = firebase.auth()