<!DOCTYPE html>
<html>
	<head>
		<title>Habits</title>
		<link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.0.2/css/bootstrap.min.css">
	</head>
	<body>

	<h1>Habits</h1>
	<a href="/newhabit">New habit</a>


	%for habit in myhabits:
	<h2>{{habit['name']}}</h2>
	<h3>{{habit['interval']['times']}} time(s) {{habit['interval']['occurence']}}</h3>
	<h3>{{habit['reminders']}}</h3>
	%end

	<script src="//code.jquery.com/jquery.js"></script>
	<script src="//netdna.bootstrapcdn.com/bootstrap/3.0.2/js/bootstrap.min.js"></script>
	</body>
</html>