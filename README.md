# Microblog

Following Miguel Grinberg's [The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) to familiarize myself with flask and python development.

## Installation

See Part 1 of tutorial

`pip3 install virtualenv`

`git clone` this repo 

`cd microblog`

`python3 -m venv flask`

install dependent packages

	$ flask/bin/pip install flask
	$ flask/bin/pip install flask-login
	$ flask/bin/pip install flask-openid
	$ flask/bin/pip install flask-mail
	$ flask/bin/pip install flask-sqlalchemy
	$ flask/bin/pip install sqlalchemy-migrate
	$ flask/bin/pip install flask-whooshalchemy
	$ flask/bin/pip install flask-wtf
	$ flask/bin/pip install flask-babel
	$ flask/bin/pip install guess_language
	$ flask/bin/pip install flipflop
	$ flask/bin/pip install coverage



## Usage

Modify run.py for running in localhost - currrently configured to run in cloud IDE

To run

	cd microblog
	./run.py

May need to 
	`chmod a+x run.py`

Access from a browser depening on host/port configuration in run.py

## History

- [x] [Part I: Hello, World!](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [ ] [Part II: Templates](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates)
- [ ] [Part III: Web Forms](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms)
- [ ] [Part IV: Database](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database)
- [ ] [Part V: User Logins](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins)
- [ ] [Part VI: Profile Page And Avatars](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vi-profile-page-and-avatars)
- [ ] [Part VII: Unit Testing](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vii-unit-testing)
- [ ] [Part VIII: Followers, Contacts And Friends](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-viii-followers-contacts-and-friends)
- [ ] [Part IX: Pagination](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ix-pagination)
- [ ] [Part X: Full Text Search](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-x-full-text-search)
- [ ] [Part XI: Email Support](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xi-email-support)
- [ ] [Part XII: Facelift](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xii-facelift)
- [ ] [Part XIII: Dates and Times](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-dates-and-times)
- [ ] [Part XIV: I18n and L10n](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiv-i18n-and-l10n)
- [ ] [Part XV: Ajax](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xv-ajax)
- [ ] [Part XVI: Debugging, Testing and Profiling](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xvi-debugging-testing-and-profiling)
- [ ] [Part XVII: Deployment on Linux (even on the Raspberry Pi!)](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xvii-deployment-on-linux-even-on-the-raspberry-pi)
- [ ] [Part XVIII: Deployment on the Heroku Cloud](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xviii-deployment-on-the-heroku-cloud)

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## Credits

Miguel Grinberg Tutorial

## License

MIT