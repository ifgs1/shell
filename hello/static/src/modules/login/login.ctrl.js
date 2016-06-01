(function (ng) {
    var mod = ng.module('loginModule');

    mod.controller('loginCtrl', ['$scope', 'loginService', function ($scope, loginService) {

        $scope.user = {};

        $scope.error = false;

        function responseError(response) {
            console.log(response);
        }

        this.logIn = function () {
            return loginService.logIn($scope.user.username,$scope.user.password).then(function (response) {
                $scope.message = response.data;
                if($scope.message.message === 'OK'){
                    window.location.assign('#/project');
                    window.location.reload(true);
                }else{
                    $scope.error = true;
                }
            }, responseError);
        };

    }]);
})(window.angular);
