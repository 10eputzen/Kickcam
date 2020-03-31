angular.module('app')

.controller('MainController', ['$scope','$location','$filter','$rootScope','dataService','Fullscreen','spinnerService','hotkeys','toastr',
	function($scope,$location,$filter,$rootScope,dataService,Fullscreen,spinnerService,hotkeys,toastr) {

		var now = new Date();
		if (!artyom.isRecognizing()) 
		  	//console.log("Not Listening")
			//StartArtyomOneCommand();

			$scope.formData = {
				audio: "chariots",
				duration: "2",
				frames: "1.0",
				date: $filter('date')(now, "yyyy-MM-dd HH:MM:ss"),
				filePath: "",
			};
			$scope.buttonPlay = false;
			$scope.showError = false;
			$scope.hideVideo = false;
			

			$scope.change = function () {
				console.log($scope.formData)
			};

			$scope.playReplay = function() {
				$scope.buttonPlay = true;
				now = new Date();
				$scope.formData.date = $filter('date')(now, "yyyy-MM-dd HH:mm:ss");			
				postReplay($scope.formData);	
				
			};

			function postReplay(data) {
				$scope.showError = false;
				spinnerService.show('replaySpinner');
				$scope.hideVideo = false;
				dataService.postData(data,'replay/').then(postReplayComplete,handleError);
			}

			function postReplayComplete(data) {
				$scope.formData = data.data;
				
				storeReplayData($scope.formData);	
				if ($scope.formData.filePath && $scope.formData.filePath !='empty') {
					spinnerService.hide('replaySpinner');
					$location.path('replay');
				}

				if (!$scope.formData.filePath) {
					toastr.info('Video is already been converted', 'Note');
				}

				if ($scope.formData.filePath =='empty') {
					toastr.error('VideoPath is empty', 'Error');
					spinnerService.hide('replaySpinner');
					$scope.buttonPlay = false;
				}
				else
					toastr.error('Other Error', 'Error');
			//$scope.goFullscreen();
		}


		$scope.goFullscreen = function () {
			if (Fullscreen.isEnabled())
				Fullscreen.cancel();
			else
				Fullscreen.all();
		      // Set Fullscreen to a specific element (bad practice)
		      // Fullscreen.enable( document.getElementById('img') )
		  }

		  function storeReplayData(replayData) {		
		  	dataService.storeReplayData(replayData);
		  }

		  hotkeys.add({
		  	combo: 'space',
		  	description: 'Play Replay',
		  	callback: function() {
		  		$scope.playReplay();
		  	}
		  });


		  artyom.addCommands({
			  	indexes:["Kicker Replay", "kicker replay"],
			  	action: function(i){
			    // i = index of the recognized option
			    $scope.playReplay();
			}
		});


		  function handleError(data) {
		  	spinnerService.hide('replaySpinner');
		  	$scope.buttonPlay = false;
		  	$scope.showError = true;
		  	console.error(data);
		  }

		$rootScope.$on('websocket', function(event, data) {
			$scope.playReplay();
		});

		}
		])

.controller('ReplayController', ['$scope','$location','$rootScope','Fullscreen','dataService','toastr','hotkeys',
	function($scope,$location,$rootScope,Fullscreen,dataService,toastr,hotkeys) {
		
		//StartArtyomOneCommand();
		//$scope.videoPath = 'video/currentReplay/currentReplay.mp4';
		$scope.videoPath = 'http://192.168.178.116/KickCam/html/video/currentReplay/currentReplay.mp4';

		$scope.formData = {};
		var audioPath = "audio/benny.mp3";
		$scope.selectedSongPath = audioPath;

		function setAudioPath(song) {
			audioPath = "audio/" + song +".mp3"; 
			return audioPath;
		}


		getReplayData();
		$scope.goFullscreen = function () {
			if (Fullscreen.isEnabled())
				Fullscreen.cancel();
			else
				Fullscreen.all();
	      // Set Fullscreen to a specific element (bad practice)
	      // Fullscreen.enable( document.getElementById('img') )
	  }


	  function getReplayData() {
	  	var replay = {};
	  	replay = dataService.getReplayData();

	  	if (_.isEmpty(replay)) {
	  		toastr.info('You are watching the last recorded replay', 'Note');
	  		console.log("Replay not available.")
	  	}

	  }

	  hotkeys.add({
	  	combo: 'space',
	  	description: 'Back to live',
	  	callback: function() {
	  		backToLive()
	  	}
	  });

	  $scope.goFullscreen = function () {
	  	if (Fullscreen.isEnabled())
	  		Fullscreen.cancel();
	  	else
	  		Fullscreen.all();
	      // Set Fullscreen to a specific element (bad practice)
	      // Fullscreen.enable( document.getElementById('img') )
	  }


	  artyom.addCommands({
	  	indexes:["Kicker Live", "Kicker Life"],
	  	action: function(i){
		    // i = index of the recognized option
		    console.log("Live");
		    backToLive();
		}
	});

	  artyom.addCommands({
	  	indexes:["Replay Fullscreen", "Fullscreen", "Full Screen"],
	  	action: function(i){
		    // i = index of the recognized option
		    $scope.goFullscreen();
		}
	});

	  function backToLive() {   	
	  	$rootScope.$apply(function() {
	  		$location.path('live');
	  	});
	  }

		$rootScope.$on('websocket', function(event, data) {
			backToLive();
		});

	}
	])


.controller('FeatureController', ['$scope','$rootScope','$location','dataService','toastr',
	function($scope,$rootScope,$location,dataService,toastr) {

		$scope.feature = {
			name: null,
			content: null,
		};

		getFeatureData();


		$scope.submitForm = function(isValid) {
		    // check to make sure the form is completely valid
		    if (isValid) {
		      //postFeature($scope.user)
		      postFeature($scope.feature)
		  }

		};

		function postFeature(data) {
			dataService.postData(data,'features/').then(postFeaturesComplete,handleError);
		}

		function postFeaturesComplete(data) {
			toastr.success('Message submitted', 'Success');
			$scope.feature = {
				name: null,
				content: null,
			};
		}



		function getFeatureData() {
			dataService.getFeatureData('features/').then(getFeatureDataComplete,handleError);
		}

		function getFeatureDataComplete(data) {

			$scope.featureList = data.data;
			console.log($scope.features);
			if (_.isEmpty($scope.features)) {
				console.log("Feature not available.")
			}
		}


		function handleError(data) {
			toastr.error('Oh my god ... you broke the internet!', 'Error');
			console.error(data);
		}

		  function backToLive() {   	
		  	$rootScope.$apply(function() {
		  		$location.path('live');
		  	});
		  }

		$rootScope.$on('websocket', function(event, data) {
			backToLive();
		});

	}
	])


.controller('SoundController', ['$scope','$rootScope','$location','toastr','ngAudio',
	function($scope,$rootScope,$location,toastr,ngAudio) {

	$scope.templates =
    [ 
    { name: 'werner.html', url: 'templates/werner.html'},
    { name: 'fussball.html', url: 'templates/fussball.html'},
    { name: 'fun.html', url: 'templates/fun.html'},
    { name: 'songs.html', url: 'templates/songs.html'}
    ];
  	$scope.template = $scope.templates[0];

  	$scope.changeTemplate = function(index) {
		$scope.template = $scope.templates[index];
		$("#submenu .nav a").on("click", function(){
		$("#submenu .nav").find(".active").removeClass("active");
		$(this).parent().addClass("active");
	});
	}

	$scope.onTouchstart = function($event) {
	   console.log('touchstart event called');
	}

	$scope.onTouchmove = function($event) {
	   console.log('touchmove event called');
	}

	var path = 'audio/sounds/';
	var sound = false;

	$scope.changeSound = function(fileName) {
		var fileName = path + fileName + '.mp3';
		playSound(fileName);	
	}
	function playSound(audio){
		if ($scope.sound)
			$scope.sound.stop();
		$scope.sound = ngAudio.load(audio);
		if ($scope.sound)
			$scope.sound.play();
	}

	function isPlaying(audelem) {
		return !audelem.paused; 
	}

}
])
