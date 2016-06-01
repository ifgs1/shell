(function (ng) {
    var mod = ng.module('profileModule');

    mod.service('profileService', ['$http', 'profileContext', function ($http, context) {

        this.editProfile = function (independent) {
            return $http({
                method: 'POST',
                url: 'https://ancient-plains-90032.herokuapp.com/profile',
                //url: 'http://127.0.0.1:8000/profile',
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

        this.getProfile = function () {
            return $http({
                method: 'GET',
                url: 'https://ancient-plains-90032.herokuapp.com/profile'
                //url: 'http://127.0.0.1:8000/profile'
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