FROM node:18-slim

WORKDIR /app

COPY package*.json ./

RUN npm install -g npm@latest

RUN npm install

RUN npm cache clean --force

COPY . .

RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]
