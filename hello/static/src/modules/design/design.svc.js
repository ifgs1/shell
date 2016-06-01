(function (ng) {
    var mod = ng.module('designModule');

    mod.service('designService', ['$http', 'designContext', function ($http, context) {

        this.getDesigns = function (projectId) {
            return $http({
                method: 'GET',
                url: 'http://127.0.0.1:8000/getDesigns/'+projectId
            });
        };

    }]);
})(window.angular);