import Head from 'next/head'
import React from "react";
import PropTypes from 'prop-types';
import { ThemeProvider } from '@material-ui/core/styles';
import CssBaseline from '@material-ui/core/CssBaseline';
import theme from '@/styles/theme';
import '@/styles/globals.scss'

export default function MyApp({ Component, pageProps }) {
  React.useEffect(() => {
    // Remove the server-side injected CSS.
    const jssStyles = document.querySelector('#jss-server-side');
    if (jssStyles) {
      jssStyles.parentElement.removeChild(jssStyles);
    }
  }, []);
  return <>
    <Head>
      <meta name="viewport"
            content="minimum-scale=1, initial-scale=1, width=device-width"
      />
      <title>Словарь буддийской терминологии</title>
      <link rel="shortcut icon" href="/favicon.ico"/>
      {/* PWA primary color */}
      <meta name="theme-color" content={theme.palette.primary.main} />
    </Head>
    <ThemeProvider theme={theme}>
      {/* CssBaseline kickstart an elegant, consistent, and simple baseline to build upon. */}
      <CssBaseline />
      <Component {...pageProps} />
    </ThemeProvider>
    </>
}

MyApp.propTypes = {
  Component: PropTypes.elementType.isRequired,
  pageProps: PropTypes.object.isRequired,
};