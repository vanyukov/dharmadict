import React from "react";
import Head from "next/head";

export default function Header({children}) {
    return (
        <>
            <Head>
                <title>Словарь буддийской терминологии</title>
                <link rel="shortcut icon" href="favicon.ico"/>
            </Head>
            <header>

            </header>
            <main>
                {children}
            </main>
        </>
    )
}