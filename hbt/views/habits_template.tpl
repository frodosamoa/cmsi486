<!DOCTYPE html>
<html>
<head>
<title>Habits</title>
</head>
<body>

<h1>Habits</h1>

%for habit in myhabits:
<h2>{{habit['name']}}</h2>
<h3>{{habit['interval']['times']}} time(s) {{habit['interval']['occurence']}}</h3>
<h3>{{habit['reminders']}}</h3>
%end
</body>
</html>