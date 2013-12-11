<html lang="en">

	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>hbt</title>
		<link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.0.2/css/bootstrap.min.css">
		<link rel="stylesheet" href="/static/css/welcome.css">
	</head>

  <body>

    <div class="container text-center">
		<h1>hbt</h1>
		<form class="form-signup" action="/signup" method="post">
			<h2 class="form-signup-heading text-center">sign up</h2>
			<input type="text" class="form-control" placeholder="username" name="username" required="" autofocus="" value="{{username}}">
			<input type="password" class="form-control" placeholder="password" name="password" required="">
			<input type="password" class="form-control" placeholder="reenter password" name="verify" required="">
			<label class="error">{{username_error}}{{password_error}}{{verify_error}}</label>
			<button class="btn btn-lg btn-primary btn-block" type="submit">sign up</button>
		</form>
		<p>or</p>
		<a type="button" href="/signin" class="btn btn-default btn-sm">sign in</a>
	</div>

    </div> <!-- /container -->
  
	</body>
</html>