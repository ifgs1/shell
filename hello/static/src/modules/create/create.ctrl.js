/**
 * Created by IvanGarcia on 20/02/2016.
 */
(function (ng) {
    var mod = ng.module('createModule');

    mod.controller('createCtrl', ['$scope', 'createService', '$window', function ($scope, createService, $window) {

        function responseError(response) {
            console.log(response);
        }

          this.registerProject = function(){
            return createService.registerProject({
                'name':angular.element('#name').val(),
                'description':angular.element('#description').val(),
                'estimatedPrice':angular.element('#estimatedPrice').val(),
                'image':angular.element('#image').val()

            }).then(function (response) {
                $window.location.href = '/#/project';
            }, responseError);
        };
    }]);
})(window.angular);
