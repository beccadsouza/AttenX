(function() {
  let width = 320;    
  let height = 0;     
  
  let streaming = false;
  
  let video = null;
  let canvas = null;
  let photo = null;
  let startbutton = null;

  function startup() {
    video = document.getElementById('video');
    canvas = document.getElementById('canvas');
    photo = document.getElementById('photo');
    startbutton = document.getElementById('startbutton');

    navigator.mediaDevices.getUserMedia({video: true, audio: false})
    .then(function(stream) {
      video.srcObject = stream;
      video.play();
    })
    .catch(function(err) {
      console.log('hakunamatata');
      alert("Video won't stream without webcam permission.")
    });

    video.addEventListener('canplay', function(ev){
      if (!streaming) {
        height = video.videoHeight / (video.videoWidth/width);
        if (isNaN(height)) {
          height = width / (4/3);
        }

        video.setAttribute('width', width);
        video.setAttribute('height', height);
        canvas.setAttribute('width', width);
        canvas.setAttribute('height', height);
        streaming = true;
      }
    }, false);

    startbutton.addEventListener('click', function(ev){
      takepicture();
      ev.preventDefault();
    }, false);
    clearphoto();
  }

  var frame_list = [];

  function takepicture() {
    let context = canvas.getContext('2d');
    if (width && height) {
      canvas.width = width;
      canvas.height = height;
      context.drawImage(video, 0, 0, width, height);
      let data = canvas.toDataURL('image/png');
      let arr = canvas.getContext('2d').getImageData(0, 0, width, height);
      $.ajax({
          type: 'POST',
          url: '/capture/',
          data: {
              'list' : JSON.stringify([arr]),
              'height':height,
              'width':width,
          }
        });
    } else {
      clearphoto();
    }
  }

  function clearphoto() {
    let context = canvas.getContext('2d');
    context.fillStyle = "#AAA";
    context.fillRect(0, 0, canvas.width, canvas.height);

    let data = canvas.toDataURL('image/png');
    photo.setAttribute('src', data);
  }

  window.addEventListener('load', startup, false);

})();