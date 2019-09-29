(function() {
  let width = 320;    
  let height = 0;     
  
  let streaming = false;
  
  let video = null;
  let canvas = null;
  let photo = null;
  let startbutton = null;

  let stop = false;
  let frame_list = [];

  function startup() {
    video = document.getElementById('video');
    canvas = document.getElementById('canvas');
    photo = document.getElementById('photo');
    startbutton = document.getElementById('startbutton');
    stopbutton = document.getElementById('stopbutton');

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
      alert("Attention Tracking has begun. Click stop to terminate it.")
      takepicture();
      stop = false;
      ev.preventDefault();
    }, false);
    clearphoto();

    stopbutton.addEventListener('click', function(ev){
      stop = true;
      ev.preventDefault();
    }, false);
    clearphoto();


  }


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
          },
          complete: function () {
            if (stop){
              console.log("Stop button clicked. Recording finished.");
              alert("Terminating Attention Detection. Insights and Recommendations available in Analytics Section");
              window.location.href = '/home';
            }
            else{
              console.log("Continuing recording.");
              setTimeout(takepicture, 2000);
            }

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