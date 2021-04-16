# Dharma Dictionary

## Local

### Install dependencies

```bash
$ npm install
```

### Starts the development server with hot reload at localhost:3000

```bash
$ npm run dev
```

### Builds the app for production and launch server

```bash
$ npm run build
$ npm run start
```

### Generate static project

```bash
$ npm run generate
```

<!-- After building, the start script starts a Node.js server that supports hybrid
pages, serving both statically generated and server-side rendered pages, and
API Routes. -->
<!-- `npm i && next start` -->

## Docker

### Starts the development server

first-run dev mode
`docker-compose up --build`
run dev mode
`docker-compose up`

### Builds the app for production

builds the production application
first-run
`docker-compose -f docker-compose-build.yml up --build`
run
`docker-compose -f docker-compose-build.yml up`

### Generate the app for production

generate the production application
first-run
`docker-compose -f docker-compose-generate.yml up --build`
run
`docker-compose -f docker-compose-generate.yml up`

### Runs the built app in production mode

After building, the start script starts a Node.js server that supports hybrid
pages, serving both statically generated and server-side rendered pages, and
API Routes.
first-run
`docker-compose -f docker-compose-start.yml up --build`
run
`docker-compose -f docker-compose-start.yml up`

## Technology Stack

[Nuxt.js](https://nuxtjs.org)

[axioss](https://axios.nuxtjs.org/)

[tailwindcss](https://tailwindcss.com/)

[tailwindcss.nuxtjs](https://tailwindcss.nuxtjs.org/)

[google-fonts-module](https://github.com/nuxt-community/google-fonts-module)
