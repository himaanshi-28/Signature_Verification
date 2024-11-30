FROM node:18-slim

WORKDIR /app

COPY package*.json ./

RUN npm install -g npm@latest

RUN npm install

RUN npm install react-scripts --save && npm audit fix

COPY . .

RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]
