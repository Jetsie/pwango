textLabel("label","Hello World");

timedLoop(1000, function() {
  setPosition("label", randomNumber(0,320), randomNumber(0,450));
});
