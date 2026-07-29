# Git Cheat Sheet for Bioinformatics

Install Git (if not installed)

Configuring git username and email
```
$ git config --global user.name "username"
$ git config --global user.email "email"
```

Clone a repository
```
$ git clone https://github.com/rajanbit/BBL434-Bioinformatics-Lab-2026.git
```

State of the working/current repository and staging area
```
$ git status .
```

Add new or changed files in current repository to git staging area
```
$ git add .
```

Capture snapshot
```
$ git commit -m "my first commit with command line"
```

Generate personal access token from github.com
```
Profile photo -> Settings -> Developer settings -> Personal access tokens -> Generate new token -> Name token -> Select expiration time -> Select all the scopes -> Generate token
```

Copy token from clipboard and paste into a local file

Push changes into github repository
```
$ git push -u origin main
```
Authentication:- username: github_username; password: personal access token
