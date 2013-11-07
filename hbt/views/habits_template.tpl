<!DOCTYPE html>
<html>
<head>
<title>Habits</title>
</head>
<body>

<h1>Habits</h1>

%for habit in myhabits:
<h2>{{habit['name']}}</h2>
%end
</body>
</html>