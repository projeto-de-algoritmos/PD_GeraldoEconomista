FROM node:14-alpine

WORKDIR /frontend

RUN yarn global add @quasar/cli

COPY package*.json ./

# COPY yarn.lock ./

RUN yarn

COPY . ./

CMD ["yarn", "quasar", "dev"]
