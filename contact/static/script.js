var myApp = angular.module('myApp', ['ngRoute'])

//ng-route config
.config(function($routeProvider, $locationProvider) {
    $routeProvider
        .when('/home', {
            templateUrl: 'default.html',
        })
        .when('/contact-info/:contact_id', {
            templateUrl: 'contact_info.html',
            controller: 'contactInfoCtrl'
        })
        .when('/add', {
            templateUrl: 'contact_form.html',
            controller: 'addContactCtrl'
        })
        .when('/edit/:contact_id', {
            templateUrl: 'contact_form.html',
            controller: 'editContactCtrl'
        })
        .otherwise({ redirectTo: '/home' });
})

// controllers
.controller('navCtrl', function($scope) {
    $scope.nav = {
        navItems: ['home', 'add'],
        selectedIndex: 0,
        navClick: function($index) {
            $scope.nav.selectedIndex = $index;
        }
    };
})

.controller('homeCtrl', function($scope, ContactService, $http) {
    $scope.contacts = [];
    ContactService.getContacts().success(function(data) {
        $scope.contacts = data.data;
    });

    $scope.removeContact = function(item) {
        var c_id = item.id;
        var index = $scope.contacts.indexOf(item);
        $http.delete('/contact/' + c_id).then(function(response) {
            var index = $scope.contacts.indexOf(item);
            $scope.contacts.splice(index, 1);
        });
        $scope.removed = 'Contact successfully removed.';
    };

})

.controller('contactInfoCtrl', function($scope, $routeParams, $filter) {
    var c_id = $routeParams.contact_id;
    $scope.currentContact = $filter('filter')($scope.contacts, { id: c_id })[0];
})

.controller('addContactCtrl', function($scope, $location, $http) {
    //needed to show the correct button on the contact form
    $scope.path = $location.path();
    $scope.addContact = function() {
        var contact = $scope.currentContact;
        $http.post('/add', contact).then(function(response) {
            $scope.contacts.push(response.data.data);
        });
        $scope.added = 'Contact successfully added.';
    };
    $scope.updateContact = function() {
        var contact = $scope.currentContact;
        $http.put('/contact/' + contact.id, contact).then(function(response) {
            console.log("Updated!");
        });
        $scope.updated = 'Contact successfully updated.';
    };

})

.controller('editContactCtrl', function($scope, $routeParams, $filter) {
    $scope.c_id = $routeParams.contact_id;
    $scope.currentContact = $filter('filter')($scope.contacts, { id: $scope.c_id })[0];
})

// directives
.directive('contact', function() {
    return {
        restrict: 'E',
        replace: true,
        templateUrl: 'contact.html'
    }
})

// services
.factory('ContactService', function($http) {
    return {
        getContacts: function() {
            return $http({
                url: '/get_contacts',
                method: 'GET'
            })
        }
    }
});
