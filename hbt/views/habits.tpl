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
			</div>
		  </div>
		</div>

		%def habit_row(head=False):			
			%if head:
				<thead>
				<tr>
				<th class="date-column"></th>
				%for habit in myhabits:
					<th class="habit-name-row"><strong>{{habit['name']}}</strong></th>
				%end
				</tr>
				</thead>
			%else:
				<tr>
				<td class="date-column"></td>
				%for habit in myhabits:
					<td class="habit-name-row"><strong>{{habit['name']}}</strong></td>
				%end
				</tr>
			%end
		%end

		<div class="container">
			<div class="row">
				<h1 class="text-center">{{title}}</h1>
			</div>
			<div class="row">
				<form class="form-horizontal" role="form" action="/" method="POST">
					<div class="col-md-3">
						<div id="habit-actions">
							<a id="add-habit" type="button" href="/newhabit" class="btn btn-success btn-sm">new habit</a>
							<button id="update-habits" type="submit" class="btn btn-info btn-sm">update habits</button>
						</div>
					</div>
					<div class="col-md-9">
						<div id="habit-history">
							%if max_days == -1:
								<p id="dust" class="text-center">... empty dust ...</p>
							%else:
								<table id="habit-name-row-table" class="table table-nonfluid">
									%habit_row()
								</table>
								<table id="habit-table" class="table table-hover table-bordered table-nonfluid">
									%habit_row(True)
									<tbody>
										%today = datetime.datetime.now()
										%for x in range(max_days):
											%days_between = today - datetime.timedelta(days=x)
											<tr>	
												<td class="date-column" disabled="disabled">{{days_between.strftime("%a %b %d")}}</td>					
											%for habit in myhabits:
												%active = datetime.datetime.strptime(habit['dateCreated'], "%Y-%m-%d").date()
												%if days_between.date() >= active:
													%habit_id = habit['name'].replace(' ', '-').replace('\'', '') + "-" + unicode(days_between.date())
													%if habit['completedIntervals'][str(x)]:
														<td name="{{habit_id}}" class="success"><span class="glyphicon glyphicon-ok complete"></span></td>
													%else:
														<td name="{{habit_id}}" class="danger"><span class="glyphicon glyphicon-remove todo"></span></td>
													%end
														<input type="hidden" id="{{habit_id}}" name="{{habit_id}}" value="{{str(habit['completedIntervals'][str(x)]).lower()}}">
												%else:
													<td disabled="disabled" class="active"></td>
												%end
											%end
											</tr>
										%end
									</tbody>
								</table>
							%end
						</div>
					</div>
				</form>
			</div>
		</div>


		<script src="//code.jquery.com/jquery.js"></script>
		<script src="//netdna.bootstrapcdn.com/bootstrap/3.0.2/js/bootstrap.min.js"></script>
		<script src="/static/js/habits.js"></script>
	</body>
</html>