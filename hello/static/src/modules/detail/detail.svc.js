(function (ng) {
    var mod = ng.module('detailModule');

    /*mod.config(function($httpProvider, $cookies){
        $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
    })*/

    mod.service('detailService', ['$http', 'detailContext', function ($http, context) {

        this.editDetail = function (independent) {
            return $http({
                method: 'POST',
                url: 'https://ancient-plains-90032.herokuapp.com/detail',
                //url: 'http://127.0.0.1:8000/detail',
                data:{
                    name: independent.fields.name,
                    last_name: independent.fields.lastName,
                    experience: independent.fields.yearsOfExperience,
                    phone_number: independent.fields.phoneNumber,
                    email: independent.fields.email,
                    image:  independent.fields.imageFileUrl,
                    job:  independent.fields.job

                }
            });
        };

        this.getDetail = function () {
            return $http({
                method: 'GET',
                url: 'https://ancient-plains-90032.herokuapp.com/detail'
                //url: 'http://127.0.0.1:8000/detail'
            });
        }

        this.getJobs = function () {
            return $http({
                method: 'GET',
                url: 'https://ancient-plains-90032.herokuapp.com/jobs'
                //url: 'http://127.0.0.1:8000/jobs'
            });
        };

    }]);
})(window.angular);

