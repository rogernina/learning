app
.factory("API",function($resource){
	var url = "http://localhost:9001/api/dper/Profeciones/"
	return{

		 Profecion: $resource(url, { 'id': '@id' }, {
            "update": { method: 'PUT' },
            "list": {
                method: 'GET'            
            },
           
        }),
		

	};


});
