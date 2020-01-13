var nodemailer = require('nodemailer');

var transporter = nodemailer.createTransport({
  service: 'Gmail',
  auth: {
    user: 'someEmail@gmail.com', // change to your email
    pass: 'phoneyPassword' // change to your password. BE SURE TO NOT UPLOAD TO GITHUB!!!
  }
});

var mailOptions = {
  from: 'someEmail@gmail.com',
  to: 'anotherEmail@gmail.com',
  subject: 'Sending you an email with node.js',
  text: 'You is a boop!'
};

transporter.sendMail(mailOptions, function(error, info) {
  if (error) {
    console.log(error);
  } else {
    console.log('Email sent: ' + info.response);
  }
});
