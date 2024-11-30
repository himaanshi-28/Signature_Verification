FROM node:18

WORKDIR /app

COPY package*.json ./
RUN npm install --save-dev @babel/plugin-proposal-private-property-in-object
RUN npm install

COPY . .

RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]
