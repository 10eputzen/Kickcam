(function () {
    'use strict';

    angular.module('app')
        .factory('dataService', dataService);

    dataService.$inject = ['$http'];

    var replay = {};
    var feature = {};

    function dataService($http, serviceUrl){ 
        var services = {
            storeReplayData: storeReplayData,
            getReplayData: getReplayData,
            postData:postData,
            getFeatureData:getFeatureData,
        };
        return services;

        function storeReplayData(replayData) {
            replay = replayData
        };

        function getReplayData() {
        return replay;
        };

        function postData(replay,object) {

            return $http({
                url: apiUrl + object,
                method: 'POST',
                data: replay,
                headers: {
                    'Content-Type': 'application/json'
                },
            })
        };

        function getFeatureData(object) {
            console.log("GET FEATURE DATA")
            return $http({
                url: apiUrl + object,
                method: 'GET'
            });
        }
        



    }
})();


