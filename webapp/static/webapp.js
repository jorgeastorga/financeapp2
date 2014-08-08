var angapp = angular.module('myApp', []);
angapp.config(function($interpolateProvider){
$interpolateProvider.startSymbol('{[{').endSymbol('}]}');
});
