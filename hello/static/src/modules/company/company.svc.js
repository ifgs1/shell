(function (ng) {
    var mod = ng.module('companyModule');

    mod.service('companyService', ['$http', 'companyContext', function ($http, context) {

        this.getProjects = function (id) {
            return $http({
                method: 'GET',
                url: 'http://127.0.0.1:8000/company/'+id
            });
        };

    }]);
})(window.angular);