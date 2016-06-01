(function (ng) {
    var mod = ng.module('projectModule');

    mod.service('projectService', ['$http', 'projectContext', function ($http, context) {

    this.getProjects = function () {
                return $http({
                    method: 'GET',
                    url: 'http://127.0.0.1:8000/project/'
                });
    };

    this.deleteProject = function (id) {
                return $http({
                    method: 'DELETE',
                    url: 'http://127.0.0.1:8000/project/',
                    data:{
                        pk:id
                    }
                });
        };
    }]);


})(window.angular);