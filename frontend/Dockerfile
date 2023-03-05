FROM node:18.14.2-alpine

WORKDIR /frontend

ENV PATH /frontend/node_modules/.bin:$PATH


COPY package.json .
COPY package-lock.json .
RUN npm install

CMD ["npm", "run", "dev"]
