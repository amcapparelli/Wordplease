# Wordplease

Wordplease is a blogging app developed with Python/Django by Alejandro Capparelli

## Install

pip install -r requirements.txt

## APP Routes

- /signup

- /login

- /admin

all blogs: 
- /blogs

all posts from author`s blog: 
- /blogs/[username] 

sigle post from author`s blog:

- /blogs/[username]/[id]


## API Routes

GET  single user:   
- /api/1.0/users/<int:pk>

POST  new user:  
- /api/1.0/users/signup

GET  all blogs:   
- /api/1.0/blogs  | query params: "author=[username]", "order=[blog_title]"

GET  all posts from blog:   
- /api/1.0/blog/<username> 

GET, PUT, DELETE single post:
- /api/1.0/blog/<username>/<int:pk>