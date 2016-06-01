(function (ng) {
    var mod = ng.module('createDesignModule');

    mod.service('createDesignService', ['$http', 'createDesignContext', function ($http, context) {

        this.createDesign = function (data) {
            return $http({
                method: 'POST',
                //url: 'https://ancient-plains-90032.herokuapp.com/login',
                url: 'http://127.0.0.1:8000/design',
                data: data
            });
        };

    }]);
})(window.angular);