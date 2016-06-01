(function (ng) {
    var mod = ng.module('loginModule');

    mod.service('loginService', ['$http', 'loginContext', function ($http, context) {

        this.logIn = function (username,password) {
            return $http({
                method: 'POST',
                //url: 'https://ancient-plains-90032.herokuapp.com/login',
                url: 'http://127.0.0.1:8000/login',
                data: {
                    username: username,
                    password: password
                }
            });
        };

    }]);
})(window.angular);