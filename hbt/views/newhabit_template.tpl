<!DOCTYPE html>
<html>
<head>
<title>Habits</title>
</head>
<body>

<h1>New habit</h1>

<form action="/newhabit" method="POST">
<h2>Name</h2>
<input type="text" name="name" size="120" value="{{name}}"><br>
<h2>Times<h2>
<input type="text" name="times" size="120" value="{{times}}"><br>
<h2>Occurence</h2>
<input type="text" name="occurence" size="120" value="{{occurence}}"><br>
<h2>Reminders</h2>
<input type="text" name="reminders" size="120" value="{{reminders}}"><br>

<input type="submit" value="Submit">
</body>
</html>