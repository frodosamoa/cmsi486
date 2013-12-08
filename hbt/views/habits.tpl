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

		%def habit_row():
			<tr>
		%	for habit in myhabits:
				<td><strong>{{habit['name']}}</strong></td>
		%	end
			</tr>
		%end

	    <div class="container">
			<h1 class="text-center">{{title}}</h1>
			<a id="add-habit" type="button" href="/newhabit" class="btn btn-success btn-sm">new habit</a>
        	%if days == 0:
	        	<p id="dust" class="text-center">... empty dust ...</p>
        	%end
			<div id="habit-history">
				<table id="habit-name-row-table" class="table table-hover table-bordered table-nonfluid">
		            <tbody>
						%habit_row()
					</tbody>
				</table>
				<table id="habit-table" class="table table-hover table-bordered table-nonfluid">
		            <tbody>

		            	%habit_row()
		            	%for x in range(days + 1):
							%today = datetime.datetime.now()
							%current = datetime.timedelta(days=x)
							%days = today - current	
							<tr>							
			            	%for habit in myhabits:
			            		%active = datetime.datetime.strptime(habit['dateCreated'], "%Y-%m-%d").date()
			            		
			            		%if days.date() >= active:
									<td>{{days.date()}}</td>
								%else:
									<td disabled="disabled">--</td>
								%end
							%end
							</tr>
						%end
					</tbody>
				</table>
			</div>

		</div>

		<script src="//code.jquery.com/jquery.js"></script>
		<script src="//netdna.bootstrapcdn.com/bootstrap/3.0.2/js/bootstrap.min.js"></script>
		<script src="/static/js/habits.js"></script>
	</body>
</html>