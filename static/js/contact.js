// Initialize Firebase (ADD YOUR OWN DATA)
var config = {
  apiKey: "AIzaSyDUN72bR1bk7MrFjsGCnE5gpp9dkz3rbtU",
    authDomain: "formtest293.firebaseapp.com",
    databaseURL: "https://formtest293.firebaseio.com",
    projectId: "formtest293",
    storageBucket: "formtest293.appspot.com",
    messagingSenderId: "843774785344",
    appId: "1:843774785344:web:156550203b20eaed21aca5"
};
firebase.initializeApp(config);

// Reference messages collection
var messagesRef = firebase.database().ref('messages');

// Listen for form submit
document.getElementById('contactForm').addEventListener('submit', submitForm);

// Submit form
function submitForm(e){
  e.preventDefault();

  // Get values
  var name = getInputVal('name');
  var email = getInputVal('email');
  var phone = getInputVal('phone');
  var message = getInputVal('message');

  // Save message
  saveMessage(name, email, phone, message);

  // Show alert
  document.querySelector('.alert').style.display = 'block';

  // Hide alert after 3 seconds
  setTimeout(function(){
    document.querySelector('.alert').style.display = 'none';
  },3000);

  // Clear form
  document.getElementById('contactForm').reset();
}

// Function to get get form values
function getInputVal(id){
  return document.getElementById(id).value;
}

// Save message to firebase
function saveMessage(name, email, phone, message){
  var newMessageRef = messagesRef.push();
  newMessageRef.set({
    name: name,
    email:email,
    phone:phone,
    message:message
  });
}


// // Get all form fields
// const formFields = [...document.querySelectorAll('#contactForm input, #contactForm textarea')];

// // Add event listener to the submit button
// submitButton.addEventListener('click', (e) => {
//   // Prevent form submission
//   e.preventDefault();

//   // Check that all fields have a value
//   let isFormValid = formFields.every(field => field.value !== '');

//   // If form is valid, run showAlert function
//   if (isFormValid) {
//     showAlert();
//   } else {
//     // Show an alert
//     alert('Please fill out all the required fields.');
//   }
// });

//   function showAlert() {
//   alert("Your request submitted !");
// }
