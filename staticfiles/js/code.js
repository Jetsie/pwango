textLabel("label","Hello World!");

timedLoop(1000, function() {
  setPosition("label", randomNumber(0,700), randomNumber(0,500));
});
