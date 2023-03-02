# Developers documentation
## Building project:
1. Ask project owner for contributor status.
2. Create ssh key:
   1. Linux - Coming soon
   2. Windows 10/11 - open cmd type `ssh-keygen` and go through configuration step (you can leave blank and press enter a couple of times)
3. Clone [repository](https://github.com/oskarmay/BARTAS-WEB)
4. Go to project files and run `docker compose build` and after successful build `docker compose up`

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
2. Go to project files and run `pre-commit install`
3. Run `pre-commit run` to check if everything go smooth