(function() {
    var app = angular.module('inventory', [ ]);
        app.config(function($interpolateProvider) { 
            $interpolateProvider.startSymbol('[['); 
            $interpolateProvider.endSymbol(']]');
        });

    app.controller('InventoryController', ['$scope', '$http',
        function ($scope, $http) {
          $http.get('/json').success(function(data) {
            $scope.records = data;
            $scope.orderCol = 'title';
        });

    }]);

/*
    var pages = [
    {
        name: 'Totally awesome page',
        url: 'http://natlib.govt.nz',
        description: 'This page is super amazing',
        owner: 'Reuben Schrader',
        canClick: true,
    },
    {
        name: 'Wonderful page',
        url: 'http://natlib.govt.nz/ww100',
        description: 'Hmm, serious war page',
        owner: 'Reuben Schrader',
        canClick: false,
    }
    ];
    */
})();
