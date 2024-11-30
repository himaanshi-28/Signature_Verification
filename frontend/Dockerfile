FROM node:18-slim

WORKDIR /app

COPY package*.json ./

RUN npm install -g npm@9.6.0
RUN npm install --save-dev @babel/plugin-proposal-private-property-in-object

COPY . .

RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]
