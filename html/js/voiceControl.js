var microphone = false;
function StartArtyomOneCommand(){
	if (!microphone) {
		artyom.fatality();// use this to stop any of
	    setTimeout(function(){// if you use artyom.fatality , wait 250 ms to initialize again.
	         artyom.initialize({
	            lang:"en-GB",// A lot of languages are supported. Read the docs !
	            continuous:true,// Artyom will listen forever
	            listen:true, // Start recognizing
	            debug:true, // Show everything in the console
	            speed:1 // talk normally
	        });
	    },250);
	    angular.element(document.getElementById("microphoneButton")).removeClass("mcIcon_mute");
		angular.element(document.getElementById("microphoneButton")).addClass("mcIcon_red")
		microphone = true;
	}
	else {
		StopArtyom()
		

	}

}


function StopArtyom(){
	console.log("Stop Listening");
	angular.element(document.getElementById("microphoneButton")).removeClass("mcIcon_red");
	angular.element(document.getElementById("microphoneButton")).addClass("mcIcon_mute")
	microphone = false;
    artyom.fatality();
}


artyom.addCommands({
  indexes:["Stop Voice", "Kicker Shut up"],
  action: function(i){
  	StopArtyom()
  }
});

artyom.addCommands({
  indexes:["Kicker Benny Hill", "Kicker Benni Hill"],
  action: function(i){
  	var audio = new Audio('audio/benny.mp3');
	audio.play();
  }
});












