(function (ng) {

    var helpApp = ng.module('helpApp', [
        'ngRoute',
        'managerModule',
        'profileModule',
        'mainModule',
        'loginModule',
        'commentsModule',
        'detailModule',
        'projectModule',
        'createModule',
        'createDesignModule',
        'editModule',
        'designModule',
        'companyModule'

    ]);

    helpApp.config(['$routeProvider', function ($routeProvider) {

        $routeProvider
            .when('/main', {
                templateUrl: 'static/src/modules/main/main.tpl.html',
                controller: 'managerCtrl',
                controllerAs: 'ctrl'
            })
            .when('/profile', {
                templateUrl: 'static/src/modules/profile/profile.tpl.html',
                controller: 'profileCtrl',
                controllerAs: 'ctrl'
            })
            .when('/login', {
                templateUrl: 'static/src/modules/login/login.tpl.html',
                controller: 'loginCtrl',
                controllerAs: 'ctrl'
            })
            .when('/register', {
                templateUrl: 'static/src/modules/manager/registration.tpl.html',
                controller: 'managerCtrl',
                controllerAs: 'ctrl'
            })
            .when('/comments/:idIndependent', {
                templateUrl: 'static/src/modules/comments/comments.tpl.html',
                controller: 'commentsCtrl',
                controllerAs: 'ctrl'
            })
            .when('/detail/:idIndependent', {
                templateUrl: 'static/src/modules/detail/detail.tpl.html',
                controller: 'detailCtrl',
                controllerAs: 'ctrl'
            })
            .when('/project', {
                templateUrl: 'static/src/modules/project/project.tpl.html',
                controller: 'projectCtrl',
                controllerAs: 'ctrl'
            })
            .when('/create', {
                templateUrl: 'static/src/modules/create/create.tpl.html',
                controller: 'createCtrl',
                controllerAs: 'ctrl'
            })
            .when('/createDesign/:projectId', {
                templateUrl: 'static/src/modules/createDesign/createDesign.tpl.html',
                controller: 'createDesignCtrl',
                controllerAs: 'ctrl'
            })
            .when('/edit/:idProject', {
                templateUrl: 'static/src/modules/edit/edit.tpl.html',
                controller: 'editCtrl',
                controllerAs: 'ctrl'
            })
            .when('/design/:projectId', {
                templateUrl: 'static/src/modules/design/design.tpl.html',
                controller: 'designCtrl',
                controllerAs: 'ctrl'
            })
            .when('/company/:companyName/:companyId', {
                templateUrl: 'static/src/modules/company/company.tpl.html',
                controller: 'companyCtrl',
                controllerAs: 'ctrl'
            })
            .otherwise('/main');

    }]);
})(window.angular);
