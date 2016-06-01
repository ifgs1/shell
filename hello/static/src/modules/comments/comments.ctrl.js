(function (ng) {
    var mod = ng.module('commentsModule');

    mod.controller('commentsCtrl', ['$scope', '$routeParams', 'commentsService', '$window', function ($scope, $routeParams, commentsService, $window) {

        function responseError(response) {
            console.log(response);
        }

        this.registerComment = function(){
            return commentsService.registerComment({
                'idIndependent':$routeParams.idIndependent,
                'comment':angular.element('#comment').val(),
                'userEmail':angular.element('#userEmail').val()
            }).then(function (response) {
                $window.location.href = '/#/independents';
            }, responseError);
        };

    }]);
})(window.angular);