# Developers documentation
## Building project:
1. Ask project owner for contributor status.
2. Create ssh key:
   1. Linux - Coming soon
   2. Windows 10/11 - open cmd type `ssh-keygen` and go through configuration step (you can leave blank and press enter a couple of times)
3. Clone [repository](https://github.com/oskarmay/BARTAS-WEB)
4. Go to project files and run `make build` and after successful build `make run`


#### Commands
Project Setup
```make setup```

Project Run
```make run```

db makemigration
```make makemigration```

db migrate
```make migrate```

#### For more cool commands look at [Makefile](Makefile).

---
## Setting up developer tools:
### Pre-commit
#### Used hooks
- black (BE)
- isort (BE)
- eslint (FE)
- prettier (FE)

#### Installation step
1. Open system terminal and type `pip install pre-commit`
2. After this make setup shuld do the rest
