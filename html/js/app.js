(function() {
    angular.module('app', [
        'ngRoute', 
        'FBAngular',
        'angularSpinners',
        'toastr',
        'cfp.hotkeys',
        'ngAudio'
        ])
        //.value('serviceUrl', 'http://localhost:8000/')
        //.value('serviceUrl', 'http://celonis-ubuntu:8000/')
        .value('serviceUrl', 'http://192.168.178.31:8000/')

        .config(['$routeProvider',
            function($routeProvider) {
                $routeProvider
                .when('/live', {
                    templateUrl: 'templates/live.html',
                    controller: 'MainController'
                })
                .when('/replay', {
                    templateUrl: 'templates/replay.html',
                    controller: 'ReplayController'
                })
                .when('/features', {
                    templateUrl: 'templates/features.html',
                    controller: 'FeatureController'
                })
                .when('/sounds', {
                    templateUrl: 'templates/sounds.html',
                    controller: 'SoundController'
                })
                .otherwise({
                    templateUrl: 'templates/live.html',
                    controller: 'MainController'
                });
            }

            ])

        .controller('NavCtrl', 
            ['$scope', '$location','$rootScope','Fullscreen', function ($scope, $location,$rootScope,Fullscreen) {
              $scope.navClass = function (page) {
            var currentRoute = $location.path().substring(1) || 'live';
            return page === currentRoute ? 'active' : '';
            };

            $scope.loadHome = function () {
                
                requestFullscreen();
                $location.url('/live');
            };
            
            $scope.loadLive = function () {
                
                $location.url('/live');
            };
            
            $scope.loadReplay = function () {
                
                $location.url('/replay');
            };
            
            $scope.loadFeatures = function () {
                
                $location.url('/features');
            };

            $scope.loadSounds = function () {
                $location.url('/sounds');

            };
            $scope.webSocket = function() {
                $rootScope.$emit('websocket', [1]);
            }

            function requestFullscreen() {
                if (Fullscreen.isEnabled())
                    Fullscreen.cancel();
                else
                    Fullscreen.all();
            }

            ////////////// Let us open a web socket////////////
            //startWebsocket();
            function startWebsocket() {
                var socketLocation = "ws://"+websocketUrl+"/websocket";
                var ws = new WebSocket(socketLocation);
                ws.onopen = function() {
                    ws.send("Connection opened");
                    console.log("Socket Opened")
                };
                ws.onmessage = function (evt) { 
                    var received_msg = evt.data;

                    if (received_msg ==666) {
                        $scope.webSocket();
                    }

                };
                ws.onclose = function() { 
                   console.log("Connection is closed...");
                   setTimeout(function(){startWebsocket()}, 5000);
                };
            }
            ////////////////////////////////////////////////////

        }]);
    })();