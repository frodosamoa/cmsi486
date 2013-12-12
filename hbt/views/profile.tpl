<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>hbt</title>
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
	              <a href="#" class="dropdown-toggle" data-toggle="dropdown">{{user['username']}}<b class="caret"></b></a>
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
	    	<div class"row">
		    	<h1 class="text-center">{{title}}</h1>
				<h2><span class="glyphicon glyphicon-user"></span> {{user['username']}} <small>{{user['dateJoined']}}</small></h2>
			</div>
			<div class="row">
				<div class="col-md-3">
					<h4>your habits</h4>
					<ol>
						%for habit in habits:
							<li>{{habit['name']}}</li>
						%end
					</ol>
				</div>
				<div class="col-md-3">
					<h4>your categories</h4>
					<ol>
						%for cat in categories:
							<li>{{cat}}</li>
						%end
					</ol>
				</div>
				<div class="col-md-3">
					<h4>best habits</h4>
					<ol>
						%for habit in best_habits:
							<li>{{habit}}</li>
						%end
					</ol>
				</div>
				<div class="col-md-3">
					<h4>worst habits</h4>
					<ol>
						%for habit in worst_habits:
							<li>{{habit}}</li>
						%end
					</ol>
				</div>
		</div>



	<script src="//code.jquery.com/jquery.js"></script>
	<script src="//netdna.bootstrapcdn.com/bootstrap/3.0.2/js/bootstrap.min.js"></script>
	</body>
</html>