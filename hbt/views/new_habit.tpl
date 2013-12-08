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
			<h2>new habit</h2>
			<form id="new" action="/newhabit" method="POST">
			<h4>name</h4>
			<input type="text" name="name" size="120" value="{{name}}"><br>
			<h4>interval</h4>
			<input type="checkbox">
			<div class="btn-toolbar">
				<div id="occurence" class="btn-group" data-toggle="buttons">
					<label class="btn btn-default">
						<input type="checkbox" name="once" id="once">once
					</label>
					<label class="btn btn-default">
						<input type="checkbox" name="twice" id="twice">twice
					</label>
					<label id="thrice" class="btn btn-default">
						<input type="checkbox" name="thrice" id="thrice">thrice
					</label>
				</div>
				<div id="interval" class="btn-group" data-toggle="buttons">
					<label id="daily" class="btn btn-default">
						<input type="checkbox" name="daily" id="daily">daily
					</label>
					<label id="weekly" class="btn btn-default">
						<input type="checkbox" name="weekly" id="weekly">weekly
					</label>
					<label id="monthly" class="btn btn-default">
						<input type="checkbox" name="monthly" id="monthly">monthly
					</label>
				</div>
			</div>
			<h4>reminders</h4>
			<input type="text" name="reminders" size="120" value="{{reminders}}"><br>
			<h4>categories</h4>
			<input type="text" name="categories" size="120" value="{{categories}}"><br>
			<br>
			<button type="submit" class="btn btn-success">add habit</button>
			</form>
		</div>



	<script src="//code.jquery.com/jquery.js"></script>
	<script src="//netdna.bootstrapcdn.com/bootstrap/3.0.2/js/bootstrap.min.js"></script>
	</body>
</html>