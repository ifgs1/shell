(function (ng) {
    var mod = ng.module('mainModule');

    mod.controller('mainCtrl', ['$scope', 'mainService', function ($scope, mainService) {

        function responseError(response) {
            console.log(response);
        }

        this.isLogged = function () {
            return mainService.isLogged().then(function (response) {
                $scope.message = response.data;
            }, responseError);
        };

        this.logOut = function () {
            return mainService.logOut().then(function (response) {
                window.location.assign('#/main');
                window.location.reload(true);
            }, responseError);
        };

    }]);
})(window.angular);
