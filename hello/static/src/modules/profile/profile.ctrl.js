(function (ng) {
    var mod = ng.module('profileModule');

    mod.controller('profileCtrl', ['$scope', 'profileService', function ($scope, profileService) {

        $scope.independent = {};
        $scope.success = '';

        function responseError(response) {
            console.log(response);
            this.success = 'ERROR';
        }

        this.editProfile = function () {
            return profileService.editProfile($scope.independent).then(function (response) {
                $scope.success = 'OK';
            }, responseError);
        };

        this.getInfo = function () {
            profileService.getJobs().then(function (response) {
                $scope.jobs = response.data;
            }, responseError);

            profileService.getProfile().then(function (response) {
                console.log(response.data[0]);
                $scope.independent = response.data[0];
            }, responseError);

        };

    }]);
})(window.angular);
