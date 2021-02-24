import React from "react";
import Head from "next/head";
import Link from "next/link";

export default function Header({children}) {
    return (<>
        <Head>
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"/>
            <title>Словарь буддийской терминологии</title>
            <link rel="shortcut icon" href="/favicon.ico"/>
        </Head>
        <header>
            <nav>
                <Link href="/">
                    Главная
                </Link>
            </nav>
        </header>
        <main>
            <div className="container">
                {children}
            </div>
        </main>
    </>
    )
}