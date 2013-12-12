<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>hbt</title>
		<script src="/static/js/Chart.min.js"></script>
		<link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.0.2/css/bootstrap.min.css">
		<link rel="stylesheet" href="/static/css/hbt.css">
	</head>
	<body>

		<div class="navbar navbar-default navbar-fixed-top" role="navigation">
	      <div class="container">
	        <div class="navbar-header">
	          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
	            <span class="sr-only">Toggle navigation</span>
	            <span class="icon-bar"></span>
	            <span class="icon-bar"></span>
	            <span class="icon-bar"></span>
	          </button>
	          <a class="navbar-brand" href="/">hbt</a>
	        </div>
	        <div class="navbar-collapse collapse">
	          <ul class="nav navbar-nav">
	            <li><a href="/habits">habits</a></li>
	            <li><a href="/categories">categories</a></li>
	            <li><a href="/graphs">graphs</a></li>
	          </ul>
	          <ul class="nav navbar-nav navbar-right">
	          	<li><a></a></li>
	            <li class="dropdown">
	              <a href="#" class="dropdown-toggle" data-toggle="dropdown">{{username}}<b class="caret"></b></a>
	              <ul class="dropdown-menu">
	                <li><a href="/profile">profile</a></li>
    	           	<li><a href="/logout">logout</a></li>
	              </ul>
	            </li>
	          </ul>
	        </div><!--/.nav-collapse -->
	      </div>
	    </div>

	    <div class="container">
			<h1 class="text-center">{{title}}</h1>
	   		<canvas id="canvas" height="300" width="600"></canvas>
	   		<br><br>
	   		<div class="text-center">
			  	<div class="btn-group">
					<button type="button" class="btn btn-default">week</button>
					<button type="button" class="btn btn-default">month</button>
					<button type="button" class="btn btn-default">three months</button>
					<button type="button" class="btn btn-default">six months</button>
					<button type="button" class="btn btn-default">year</button>
				</div>
			</div>
		</div>


		<script>
			var lineChartData = {
			        labels : ["Jan","Feb","Mar","Apr","May","Jun","Jul"],
			        datasets : [
			                {
			                        fillColor : "rgba(151,187,205,0.5)",
			                        strokeColor : "rgba(151,187,205,1)",
			                        pointColor : "rgba(151,187,205,1)",
			                        pointStrokeColor : "#fff",
			                        data : [28,48,40,19,70,27,60]
			                }
			        ]
			}

			var myLine = new Chart(document.getElementById("canvas").getContext("2d")).Line(lineChartData);

		</script>
		<script src="//code.jquery.com/jquery.js"></script>
		<script src="//netdna.bootstrapcdn.com/bootstrap/3.0.2/js/bootstrap.min.js"></script>
	</body>
</html>