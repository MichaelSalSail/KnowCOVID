import firebase from 'firebase';

const get_fire_cred=require('./fire_cred.js');

var firebaseConfig = {
    apiKey: get_fire_cred.fire_user,
    authDomain: "login-9e602.firebaseapp.com",
    databaseURL: "https://login-9e602.firebaseio.com",
    projectId: "login-9e602",
    storageBucket: "login-9e602.appspot.com",
    messagingSenderId: "977634506194",
    appId: "1:977634506194:web:c226f383c7dcd3f344840b"
  };

  const fire = firebase.initializeApp(firebaseConfig);

  export default fire;