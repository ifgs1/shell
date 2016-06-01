(function (ng) {
    var mod = ng.module('designModule');

    mod.controller('designCtrl', ['$scope', 'designService','$routeParams', function ($scope, designService,$routeParams) {

        $scope.error = false;

        function responseError(response) {
            console.log(response);
        }

        this.getDesigns = function () {
            return designService.getDesigns($routeParams.projectId).then(function (response) {
                $scope.designs = response.data;
            }, responseError);
        };

    }]);
})(window.angular);
