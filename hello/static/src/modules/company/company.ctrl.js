(function (ng) {
    var mod = ng.module('companyModule');

    mod.controller('companyCtrl', ['$scope', 'companyService','$routeParams', function ($scope, companyService,$routeParams) {

        $scope.error = false;

        function responseError(response) {
            console.log(response);
        }

        this.getProjects = function () {
            return companyService.getProjects($routeParams.companyId).then(function (response) {
                $scope.projects = response.data;
            }, responseError);
        };

    }]);
})(window.angular);
