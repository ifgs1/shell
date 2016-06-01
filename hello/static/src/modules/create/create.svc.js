/**
 * Created by IvanGarcia on 20/02/2016.
 */
(function (ng) {
    var mod = ng.module('createModule');

    mod.service('createService', ['$http', 'createContext', function ($http, context) {
      this.registerProject = function (data) {
            return $http({
                method: 'POST',
                //url: 'https://ancient-plains-90032.herokuapp.com/independents',
                url: 'http://127.0.0.1:8000/project/',
                data:data
            });
        };
    }]);
})(window.angular);