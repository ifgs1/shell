(function (ng) {
    var mod = ng.module('editModule');

    mod.controller('editCtrl', ['$scope','$routeParams', 'editService', '$window', function ($scope,$routeParams,editService, $window) {
        $scope.projects= {};

        function responseError(response) {
            console.log(response);
        }
        this.getProject = function () {
            editService.getProject($routeParams.idProject).then(function (response) {
                $scope.projects = response.data[0];
            }, responseError);

        };
          this.editProject = function () {

            return editService.editProject($scope.projects).then(function (response) {
                $scope.success = 'OK';
                  if($scope.success === 'OK'){
                    window.location.assign('#/project');
                    window.location.reload(true);
                }else{
                    $scope.error = true;
                }
            }, responseError);
        };

    }]);
})(window.angular);
