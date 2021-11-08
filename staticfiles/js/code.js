textLabel("label","Hello World");
playSpeech("Hello World!", "female", "English");
timedLoop(1000, function() {
  setPosition("label", randomNumber(0,320), randomNumber(0,450));
});
