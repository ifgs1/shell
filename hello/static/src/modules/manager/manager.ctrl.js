(function (ng) {
    var mod = ng.module('managerModule');

    mod.controller('managerCtrl', ['$scope', 'managerService', '$window', function ($scope, managerService, $window) {

        $scope.passwordMatchError=false;
        $scope.userExists=false;

        function responseError(response) {
            if(response.status==400){
                $scope.userExists=true;
            }
            console.log(response);
        }

        /*
        this.getIndependents = function () {
            return managerService.getIndependents().then(function (response) {
                $scope.independents = response.data;
            }, responseError);
        };*/

        this.registerManager = function(){
            if(angular.element('#password').val() != angular.element('#confirm_password').val()){
                $scope.passwordMatchError=true;
                return;
            }
            return managerService.registerManager({
                'company':angular.element('#company').val(),
                'email':angular.element('#email').val(),
                'password':angular.element('#password').val()
            }).then(function (response) {
                console.log(response)
                $window.location.href = '/#/main';
                $window.alert('La página de su empresa es '+ response.data.url)
            }, responseError);
        };

        /*
        this.getJobs = function () {
            return independentsService.getJobs().then(function (response) {
                $scope.jobs = response.data;
            }, responseError);
        };*/

    }]);
})(window.angular);
