import '../styles/globals.scss'
import Head from 'next/head'

function MyApp({ Component, pageProps }) {
  return <>
    <Head>
      <meta name="viewport"
            content="minimum-scale=1, initial-scale=1, width=device-width"
      />
      <title>Словарь буддийской терминологии</title>
      <link rel="shortcut icon" href="/favicon.ico"/>
    </Head>
    <Component {...pageProps} />
    </>
}

export default MyApp
