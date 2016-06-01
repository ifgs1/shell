(function (ng) {
    var mod = ng.module('commentsModule');

    /*mod.config(function($httpProvider, $cookies){
        $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
    })*/

    mod.service('commentsService', ['$http', 'commentsContext', function ($http, context) {

        this.registerComment = function (data) {
            return $http({
                method: 'POST',
                url: 'https://ancient-plains-90032.herokuapp.com/comments/:idIndependent' ,
                //url: 'http://127.0.0.1:8000/comments/:idIndependent' ,
                data:data
            });
        };

    }]);
})(window.angular);