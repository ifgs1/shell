(function (ng) {
    var mod = ng.module('managerModule');

    /*mod.config(function($httpProvider, $cookies){
        $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
    })*/

    mod.service('managerService', ['$http', 'managerContext', function ($http, context) {

        /*
        this.getIndependents = function () {
            return $http({
                method: 'GET',
                //url: 'https://ancient-plains-90032.herokuapp.com/independents'
                url: 'http://127.0.0.1:8000/independents/'
            });
        };*/

        this.registerManager = function (data) {
            return $http({
                method: 'POST',
                //url: 'https://ancient-plains-90032.herokuapp.com/independents',
                url: 'http://127.0.0.1:8000/register/',
                data:data
            });
        };
        /*
        this.getJobs = function () {
            return $http({
                method: 'GET',
                url: 'https://ancient-plains-90032.herokuapp.com/jobs'
                //url: 'http://127.0.0.1:8000/jobs'
            });
        };*/

    }]);
})(window.angular);