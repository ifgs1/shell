(function (ng) {
    var mod = ng.module('mainModule');

    mod.service('mainService', ['$http', 'mainContext', function ($http, context) {

        this.isLogged = function () {
            return $http({
                method: 'GET',
                //url: 'https://ancient-plains-90032.herokuapp.com/islogged'
                url: 'http://127.0.0.1:8000/islogged'
            });
        };

        this.logOut = function () {
            return $http({
                method: 'GET',
                //url: 'https://ancient-plains-90032.herokuapp.com/logout'
                url: 'http://127.0.0.1:8000/logout'
            });
        };

    }]);
})(window.angular);