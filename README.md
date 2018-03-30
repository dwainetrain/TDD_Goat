# TDD_Goat
Learning Test Driven Development with the Testing Goat

Challenges I've faced that the book doesn't address:

The biggest challenge is that the Harry uses nginx as his server, but the two servers I've used so far: one for deployment and one for continous intergration (CI) are both Apache. So for Dreamhost I created my own fabfile for deployment and configured the wsgi file there, and I also had to setup the hiding of secret information differently also.

Now that I'm heading into AWS territory, again Apache requires a different setup from the one that the book presents.
