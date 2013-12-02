<!DOCTYPE html>
<html>
	<head>
		<title>Habits</title>
		<link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.0.2/css/bootstrap.min.css">
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
	        </div>
	      </div>
	    </div>

	    <div class="container" style="padding-top: 70px;">
			<h2>New habit</h2>
			<form action="/newhabit" method="POST">
			<h4>Name</h4>
			<input type="text" name="name" size="120" value="{{name}}"><br>
			<h4>Times<h4>
			<input type="text" name="times" size="120" value="{{times}}"><br>
			<h4>Occurence</h4>
			<input type="text" name="occurence" size="120" value="{{occurence}}"><br>
			<h4>Reminders</h4>
			<input type="text" name="reminders" size="120" value="{{reminders}}"><br>
			<h4>Categories</h4>
			<input type="text" name="categories" size="120" value="{{categories}}"><br>
			<br>
			<button type="submit" class="btn btn-success"> Add habit</button>
			</form>
		</div>



	<script src="//code.jquery.com/jquery.js"></script>
	<script src="//netdna.bootstrapcdn.com/bootstrap/3.0.2/js/bootstrap.min.js"></script>
	</body>
</html>