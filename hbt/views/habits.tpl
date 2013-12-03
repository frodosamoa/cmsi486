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
	            <li><a href="/">habits</a></li>
	            <li><a href="/categories">categories</a></li>
	            <li><a href="/graphs">graphs</a></li>
	          </ul>
	          <ul class="nav navbar-nav navbar-right">
	            <li class="dropdown">
	              <a href="#" class="dropdown-toggle" data-toggle="dropdown">support <b class="caret"></b></a>
	              <ul class="dropdown-menu">
	                <li><a href="#">email</a></li>
	              </ul>
	            </li>
	           	<li><a href="/login">logout</a></li>
	          </ul>
	        </div><!--/.nav-collapse -->
	      </div>
	    </div>

	    <div class="container">
	    	<div class="row">
	    		<div class="col-md-4">
					<h1>habits</h1>
					<button type="button" href="/newhabit" class="btn btn-danger">New habit</button>
					<div id="habit-list">
						<table class="table">
							<thead>
								<tr>
									<td>Name</td>
									<td>Interval</td>
									<td>Reminders</td>
									<td>Categories</td>
								</tr>
							</thead>
				            <tbody>
								%for habit in myhabits:
								<tr>
								<td>{{habit['name']}}</td>
								<td>{{habit['interval']['times']}} times {{habit['interval']['occurence']}}</td>
								<td>{{habit['reminders']}}</td>
								<td>
								%for category in habit['categories']:
								{{category}},
								%end
								</td>
								</tr>
								%end
							</tbody>
						</table>
					</div>
				</div>
				<div class="col-md-8">
				</div>
			</div>
		</div>

		<script src="//code.jquery.com/jquery.js"></script>
		<script src="//netdna.bootstrapcdn.com/bootstrap/3.0.2/js/bootstrap.min.js"></script>
	</body>
</html>