var objs = [];
var objCount = 0;
var sorted;
var cam = 0;

var stop = false;

function drawPoly(points, fillColor) {
  var old = points[points.length-1];
  
  setStrokeColor(fillColor);
  for (var i = 0; i < points.length; i++) {
    line(old.x, old.y, points[i].x, points[i].y);
    old = points[i];
  }
}

// Function to create a invisible image for draw functions to reffer to withouth having to send a new request. In other words, asset caching.
function cacheAsset(refID, url) {
  image(refID, url, 320, 450);
  hideElement(refID);
}

// Function to create a Camera object.
function createCamera(x, y, z, rot_x, rot_y, rot_z, near, far, fpscap) {
  createCanvas("canvas");
  cam = {x:x, y:y, z:z, rot_x:rot_x, rot_y:rot_y, rot_z:rot_z, near:near, far:far, id:"canvas", fpscap: fpscap};
  return cam;
}

// Adds an object to the world.
function createPoint(pos, img) {
  objs.push({x: pos.x, y:pos.y, z:pos.z, id: 'obj_' + String(objCount), img: img});
  objCount += 1;
}

// Turns the camera and point 3d coordinate into a 2d screen pos.
function projection(x, y, z) {
  if (z > cam.near || z < cam.far) {
    var z_div = 300/z;
    var screen_coords = {x: x*z_div, y: y*z_div};
    return {x: 160+screen_coords.x, y: 225+screen_coords.y, s: 100*z_div};
  } else {
    return {x: 0, y: 0, s: 0};
  }
}

//rotate a point arount (0, 0).
function rotate(x, z, direction) {
  return {x: (z*Math.sin(direction))+(x*Math.cos(direction)), y: (z*Math.cos(direction))-(x*Math.sin(direction))};
}

// Sorts objects by distance to camera.
function quickSort(arr, leftPos, rightPos, arrLength) {
  var initialLeftPos = leftPos;
  var initialRightPos = rightPos;
  var direction = true;
  var pivot = rightPos;
  while ((leftPos - rightPos) < 0) {
    if (direction) {
      if (Math.pow(arr[pivot].x-cam.x, 2)+Math.pow(arr[pivot].y-cam.y, 2)+Math.pow(arr[pivot].z-cam.z, 2) < Math.pow(arr[leftPos].x-cam.x, 2)+Math.pow(arr[leftPos].y-cam.y, 2)+Math.pow(arr[leftPos].z-cam.z, 2)) {
        quickSort.swap(arr, pivot, leftPos);
        pivot = leftPos;
        rightPos--;
        direction = !direction;
      } else
        leftPos++;
    } else {
      if (Math.pow(arr[pivot].x-cam.x, 2)+Math.pow(arr[pivot].y-cam.y, 2)+Math.pow(arr[pivot].z-cam.z, 2) <= Math.pow(arr[rightPos].x-cam.x, 2)+Math.pow(arr[rightPos].y-cam.y, 2)+Math.pow(arr[rightPos].z-cam.z, 2)) {
        rightPos--;
      } else {
        quickSort.swap(arr, pivot, rightPos);
        leftPos++;
        pivot = rightPos;
        direction = !direction;
      }
    }
  }
  if (pivot - 1 > initialLeftPos) {
    quickSort(arr, initialLeftPos, pivot - 1, arrLength);
  }
  if (pivot + 1 < initialRightPos) {
    quickSort(arr, pivot + 1, initialRightPos, arrLength);
  }
  return arr;
}
quickSort.swap = function (arr, el1, el2) {
  var swapedElem = arr[el1];
  arr[el1] = arr[el2];
  arr[el2] = swapedElem;
};

// Converts degrees to radians.
function degsToRads(deg) {
  return deg * Math.PI / 180;
}

// Converts radians to degrees
function radsToDegs(rad) {
  return rad * 180 / Math.PI;
}

// Updates the screen.
function broadcast() {
  clearCanvas();
  for(var i = 0; i < objCount; i++) {
    if (stop) {
      stop = false;
      break;
    }
    var item = sorted[i];
    var rotatedxz = rotate(item.x-cam.x, item.z-cam.z, 0 - cam.rot_y);
    var rotatedyz = rotate(item.y-cam.y, rotatedxz.y, 0 - cam.rot_x);
    var pos = projection(rotatedxz.x, rotatedyz.x, rotatedyz.y);
    var nPos = {x: pos.s/2, y: pos.s/2};
    if (((pos.x + nPos.x > 0) && ((pos.x - nPos.x < 320))) && ((pos.y + nPos.y > 0) && ((pos.y - nPos.y < 450)))) {
      drawImage(item.img, pos.x-nPos.x, pos.y-nPos.y, pos.s, pos.s);
    }
  }
}

// Runs all threaded loops.
function run() {
  // Update screen
  var old;
  var fps;
  var start;
  timedLoop(1000/cam.fpscap, function(){
    start = getTime();
    if (old !== cam) {
      sorted = quickSort(objs, 0, objs.length - 1, objs.length).reverse();
      broadcast();
      // manualObject(
      //   objs,
      //   [[0, 1], [1, 2], [2, 0]],
      //   [[0, 1, 2]]
      // );
    } else {
      old = cam;
    }
    fps = 1000/(getTime() - start);
    if (fps >= cam.fpscap) {
      fps = cam.fpscap;
    }
  });
  
  // Show FPS
  timedLoop(1000/cam.fpscap, function(){
    console.log("FPS: " + Math.round(fps));
  });
}

// Adds a simple camera move script.
function simpleMoveScript(screen) {
  onEvent(screen, "keypress", function(event) {
    stop = true;
    var look = degsToRads(1);
    switch(event.key) {
      // Foward
      case "w":
        cam.x += 5*Math.sin(cam.rot_y);
        cam.z += 5*Math.cos(cam.rot_y);
        break;
      // Backward
      case "s":
        cam.x += -5*Math.sin(cam.rot_y);
        cam.z += -5*Math.cos(cam.rot_y);
        break;
      // Sidestep Left
      case "a":
        cam.x += -5*Math.cos(cam.rot_y);
        cam.z += 5*Math.sin(cam.rot_y);
        break;
      // Sidestep Right
      case "d":
        cam.x += 5*Math.cos(cam.rot_y);
        cam.z += -5*Math.sin(cam.rot_y);
        break;
      // Raise
      case "q":
        cam.y -= 5;
        break;
      // Lower
      case "e":
        cam.y += 5;
        break;
      // Look Left
      case "j":
        cam.rot_y -= look;
        break;
      // Look Right
      case "l":
        cam.rot_y += look;
        break;
      // Look Up
      case "i":
        cam.rot_x -= look;
        break;
      // Look Down
      case "k":
        cam.rot_x += look;
        break;
    }
    stop = false;
  });
}

// A generic demo scene
function demoScene() {
  cacheAsset('point', "https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Location_dot_red.svg/1024px-Location_dot_red.svg.png");
  createPoint({x: 100, y: 100, z: 300}, 'point');
  createPoint({x: -100, y: 100, z: 300}, 'point');
  createPoint({x: 100, y: -100, z: 300}, 'point');
  createPoint({x: -100, y: -100, z: 300}, 'point');
  createPoint({x: 100, y: 100, z: 100}, 'point');
  createPoint({x: -100, y: 100, z: 100}, 'point');
  createPoint({x: 100, y: -100, z: 100}, 'point');
  createPoint({x: -100, y: -100, z: 100}, 'point');

  var demoCam = createCamera(0, 0, 0, 0, 0, 0, 30, 500, 10);
  simpleMoveScript("screen");
  
//   drawPoly([{x: 20, y: 20}, {x: 70, y: 40}, {x: 320, y: 400}, {x: 100, y: 200}], 'red');
  
  run();
}

demoScene();
