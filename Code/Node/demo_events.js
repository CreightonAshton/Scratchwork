var events = require('events');
var eventEmitter = new events.EventEmitter();

// Create an event handler
var myEventEmitter = function() {
  console.log('I hear a scream');
}

// Assign the event handler to an event
eventEmitter.on('scream', myEventEmitter);

// Fire the scream event
eventEmitter.emit('scream');
