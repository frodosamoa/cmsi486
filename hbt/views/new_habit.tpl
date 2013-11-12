<!DOCTYPE html>
<html>
	<head>
		<title>Habits</title>
		<link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.0.2/css/bootstrap.min.css">
	</head>
	<body>
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

	<button type="submit" class="btn btn-success"> Add habit</button>



	<script src="//code.jquery.com/jquery.js"></script>
	<script src="//netdna.bootstrapcdn.com/bootstrap/3.0.2/js/bootstrap.min.js"></script>
	</body>
</html>