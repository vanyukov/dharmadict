Dharma Dictionary
==============

## Local

### Starts the development server
`npm i && next dev`

### Builds the app for production
`npm i && next build`
 builds the production application in the .next folder.
 
### Runs the built app in production mode
After building, the start script starts a Node.js server that supports hybrid 
pages, serving both statically generated and server-side rendered pages, and 
API Routes.
`npm i && next start`

## Docker

### Starts the development server
first-run dev mode
`docker-compose up --build`
run dev mode
`docker-compose up`

### Builds the app for production
builds the production application in the .next folder.
first-run
`docker-compose -f docker-compose-build.yml up --build`
run
`docker-compose -f docker-compose-build.yml up`
 
### Runs the built app in production mode
After building, the start script starts a Node.js server that supports hybrid 
pages, serving both statically generated and server-side rendered pages, and 
API Routes.
first-run
`docker-compose -f docker-compose-start.yml up --build`
run
`docker-compose -f docker-compose-start.yml up`


## Technology Stack

### Next.js
[nextjs.org](https://nextjs.org)

### React.js
[reactjs.org](https://reactjs.org/)

### MATERIAL-UI
[material-ui.com/ru/](https://material-ui.com/ru/)

### Material Иконки
[material-ui.com/ru/components/material-icons/](https://material-ui.com/ru/components/material-icons/)

