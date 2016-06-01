/**
 * Created by IvanGarcia on 21/02/2016.
 */
(function (ng) {
    var mod = ng.module('editModule');

    mod.service('editService', ['$http', 'editContext', function ($http, context) {

       this.getProject = function (idProject) {
            return $http({
                method: 'GET',
                url: 'http://127.0.0.1:8000/project/'+idProject
            });
        }

          this.editProject = function (project) {
            return $http({
                method: 'PUT',
                url: 'http://127.0.0.1:8000/project',
                data:{
                    name: project.fields.name,
                    description: project.fields.description,
                    image: project.fields.image,
                    pk: project.pk,


                }
            });
        };

    }]);
})(window.angular);