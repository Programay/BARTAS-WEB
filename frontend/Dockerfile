FROM node:lts-alpine

WORKDIR /frontend

ENV PATH /frontend/node_modules/.bin:$PATH

# RUN npm install create-vue@3.6.0 -g

COPY package.json .
COPY package-lock.json .
RUN npm install

CMD ["npm", "run", "dev"]
