app
.controller("profecionCtrl",function($scope,APIProfecion){

	$scope.lista = []

	list = function(){
		APIProfecion.list().then(function(r){
			$scope.lista =r.data;

		},function(err){
			console.log("error "+err);
		});

	};

});

