(function (ng) {
    var mod = ng.module('projectModule');

    mod.controller('projectCtrl', ['$scope', 'projectService', '$window', function ($scope, projectService, $window) {

        function responseError(response) {
            console.log(response);
        }

        this.deleteProject = function (pk) {
            return projectService.deleteProject(pk).then(function (response) {
                window.location.reload(true);
            }, responseError);
        };

        this.getProjects = function () {
            return projectService.getProjects().then(function (response) {
                $scope.projects = response.data;
            }, responseError);
        };

        $scope.edit = function(taskId){
         console.log("Task Id is "+taskId);
            $scope.objeto = taskId
             $scope.objeto = {
            name: taskId.name,
            image:taskId.image,
            description:taskId.description,

        };

            window.location.assign('#/edit');

        };

    }]);
})(window.angular);
